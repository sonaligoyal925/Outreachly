# Outreachly – AI-Powered Cold Email Generator

Outreachly is a Streamlit web app that helps services companies automatically generate **personalized cold emails** by:
- Scraping job listings from a target company's careers page.
- Analyzing job descriptions using LLMs (via Groq API).
- Matching relevant portfolio links from a vector database.
- Crafting tailored outreach emails to maximize response rates.

---

## 🚀 Technologies Used

| Technology / Tool | Purpose | Why This Choice |
|-------------------|---------|-----------------|
| **Python** | Core programming language | Large ecosystem for web scraping, AI, and automation. |
| **Streamlit** | Web app framework | Quick to build, deploy, and share interactive apps without heavy frontend work. |
| **Groq API (LLM)** | AI text generation | High speed, cost-effective inference for generating natural-sounding emails. |
| **LangChain** | LLM orchestration | Simplifies chaining prompts, parsing, and memory management. |
| **BeautifulSoup4** | HTML parsing & scraping | Lightweight and effective for extracting job details from websites. |
| **Pandas** | Data handling | Easy manipulation and export of CSVs with job data and portfolio links. |
| **ChromaDb** | Vector database | Efficient semantic search for relevant portfolio examples. |
| **Requests** | HTTP requests | Simple and reliable for fetching HTML pages. |

---

## 📌 Skills Learned

During this project, I gained:
- **Prompt Engineering** for LLMs (Groq API + LangChain integration).
- **Web Scraping Best Practices** with BeautifulSoup.
- **Semantic Search** with vector databases (FAISS).
- **Streamlit UI Design** for interactive data workflows.
- Environment variable handling for API keys.
- CSV data structuring for machine learning pipelines.
- Writing clean, maintainable Python code for production.

---

## ⚙️ Setup Instructions

1. To get started we first need to get an API_KEY from here: [https://console.groq.com/keys](https://console.groq.com/keys).  
   Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created.

2. To get started, first install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the streamlit app:

    ```bash
    streamlit run app/main.py
    ```
