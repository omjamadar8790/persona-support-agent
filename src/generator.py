import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_response(user_query, persona, context_chunks):

    context = "\n\n".join(
        [chunk["text"] for chunk in context_chunks]
    )

    if persona == "Technical Expert":
        style = """
Technical Support Engineer
Provide detailed explanations and troubleshooting.
"""

    elif persona == "Frustrated User":
        style = """
Customer Support Specialist
Provide empathy and simple action steps.
"""

    else:
        style = """
Business Support Manager
Provide concise business-focused responses.
"""

    prompt = f"""
{style}

Use ONLY the information below.

Context:
{context}

Question:
{user_query}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        fallback = f"""
Gemini generation unavailable.

Persona: {persona}

Relevant Sources:
"""

        for chunk in context_chunks:
            fallback += f"\n- {chunk['source']}"

        fallback += "\n\nRetrieved Information:\n"

        for chunk in context_chunks:
            fallback += f"\n{chunk['text']}\n"

        fallback += f"\n\nError: {str(e)}"

        return fallback