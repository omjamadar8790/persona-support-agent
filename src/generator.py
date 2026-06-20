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
You are a Technical Support Engineer.

Provide:
- Detailed explanation
- Root cause analysis
- Technical troubleshooting steps
- Configuration guidance
"""

    elif persona == "Frustrated User":
        style = """
You are a Customer Support Specialist.

Provide:
- Empathy
- Reassurance
- Simple language
- Clear action steps
"""

    else:
        style = """
You are a Business Support Manager.

Provide:
- Concise answer
- Business impact
- Resolution timeline
- Minimal technical details
"""

    prompt = f"""
{style}

IMPORTANT:
Use ONLY the provided context.

Context:
{context}

User Question:
{user_query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text