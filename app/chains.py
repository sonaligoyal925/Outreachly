import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="openai/gpt-oss-20b"
        )

    def extract_jobs(self, cleaned_text):
        """
        Extract job postings from scraped career page text in JSON format.
        """
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing:
            - role
            - experience
            - skills
            - description

            Only return valid JSON (no extra text or preamble).

            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")

        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        """
        Write a cold email from Sonali at synQue offering a dedicated engineer for the job role.
        """
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Sonali, a Business Development Executive at synQue, a Software Development company.
            synQue provides **dedicated software development engineers** to companies,
            helping them save time, effort, and costs associated with hiring, onboarding, and training.

            In this scenario, you have identified that the company is hiring for the above position.
            Write a short, professional, and persuasive cold email offering synQue's capability
            to immediately provide a highly skilled engineer matching their needs.

            Emphasize:
            - Saving hiring/onboarding/training costs and time
            - synQue’s proven track record and quality assurance
            - Quick availability and smooth integration with their team

            Include the most relevant portfolio items from these links: {link_list}

            Do NOT provide a preamble. Write in a friendly but professional tone.

            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
