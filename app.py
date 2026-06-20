import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import LocalRAGPipeline
from src.generator import generate_response
from src.escalator import should_escalate, generate_handoff

st.set_page_config(
    page_title="Persona Adaptive Support Agent",
    page_icon="🤖"
)

st.title("🤖 Persona-Adaptive Customer Support Agent")

query = st.text_area(
    "Enter Customer Message"
)

if st.button("Submit"):

    if query.strip():

        persona_data = classify_persona(query)
        persona = persona_data["persona"]

        st.subheader("Detected Persona")
        st.success(persona)

        rag = LocalRAGPipeline()

        # Debug: Show document count
        st.write("Documents in DB:", rag.collection.count())

        docs = rag.retrieve(query)

        st.subheader("Retrieved Sources")

        sources = []

        for doc in docs:
            st.write("•", doc["source"])
            sources.append(doc["source"])

        if should_escalate(query):

            st.error("Conversation Escalated To Human Agent")

            handoff = generate_handoff(
                persona,
                query,
                sources
            )

            st.subheader("Human Handoff Summary")
            st.json(handoff)

        else:

            response = generate_response(
                query,
                persona,
                docs
            )

            st.subheader("Generated Response")
            st.write(response)