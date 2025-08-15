import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input(
        "Enter the careers page URL:",
        value="https://jobs.nike.com/job/R-33460"
    )
    role_filter = st.text_input(
        "Search role (optional):",
        value="Principal Software Engineer"
    )

    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            portfolio.load_portfolio()

            jobs = llm.extract_jobs(data)

            if role_filter.strip():
                jobs = [
                    job for job in jobs
                    if role_filter.lower() in job.get('role', '').lower()
                ]

            if not jobs:
                st.warning(f"No jobs found matching: {role_filter}")
                return

            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
