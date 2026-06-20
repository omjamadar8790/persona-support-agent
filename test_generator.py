from src.classifier import classify_persona
from src.rag_pipeline import LocalRAGPipeline
from src.generator import generate_response

query = input("Ask something: ")

persona_data = classify_persona(query)

persona = persona_data["persona"]

print("\nDetected Persona:")
print(persona)

rag = LocalRAGPipeline()

results = rag.retrieve(query)

print("\nSources:")

for r in results:
    print("-", r["source"])

answer = generate_response(
    query,
    persona,
    results
)

print("\nResponse:\n")
print(answer)