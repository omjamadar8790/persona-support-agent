import os
import chromadb
from dotenv import load_dotenv
from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

class LocalRAGPipeline:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.chroma_client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.chroma_client.get_or_create_collection(
            name="support_kb"
        )

    def get_embedding(self, text):
        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values

    def ingest_document(self, filename, content):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_text(content)

        for i, chunk in enumerate(chunks):

            embedding = self.get_embedding(chunk)

            self.collection.add(
                ids=[f"{filename}_{i}"],
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[{
                    "source": filename,
                    "chunk": i
                }]
            )

    def load_all_documents(self, data_folder="data"):

        for file in os.listdir(data_folder):

            path = os.path.join(data_folder, file)

            if file.endswith(".txt") or file.endswith(".md"):

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                print(f"Ingesting {file}")

                self.ingest_document(
                    file,
                    content
                )

    def retrieve(self, query, top_k=3):

        query_embedding = self.get_embedding(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        retrieved = []

        docs = results["documents"][0]
        metas = results["metadatas"][0]

        for doc, meta in zip(docs, metas):

            retrieved.append({
                "source": meta["source"],
                "text": doc
            })

        return retrieved