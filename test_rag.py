from src.rag_pipeline import LocalRAGPipeline

rag = LocalRAGPipeline()

# Load all documents into ChromaDB
rag.load_all_documents()

# Test retrieval
results = rag.retrieve(
    "How do I reset my password?"
)

print("\nRetrieved Documents:\n")

for r in results:
    print("SOURCE:", r["source"])
    print(r["text"])
    print("-" * 50)