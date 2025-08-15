import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        """
        Load portfolio CSV data into the ChromaDB collection if not already loaded.
        """
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        """
        Query portfolio links relevant to the given skills.
        Returns a list of URLs.
        """
        if not skills:
            return []
        results = self.collection.query(query_texts=skills, n_results=2)
        metadatas = results.get('metadatas', [])

        return [meta["links"] for sublist in metadatas for meta in sublist if "links" in meta]
