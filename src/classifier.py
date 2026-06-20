import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def classify_persona(user_message: str):

    prompt = f"""
You are a customer support persona classifier.

Classify the message into EXACTLY ONE category.

Technical Expert:
- Mentions APIs
- Logs
- Error codes
- Authentication
- Configuration
- Database integration
- Technical troubleshooting

Frustrated User:
- Emotional language
- Complaints
- Urgent requests
- Anger or frustration
- Uses phrases like:
  "nothing works"
  "fix this"
  "immediately"
  "frustrated"
  "annoyed"
  "urgent"

Business Executive:
- Focuses on business impact
- Operations
- Revenue
- Timelines
- Resolution estimates
- ROI

Return ONLY valid JSON.

Example:
{{
    "persona": "Frustrated User",
    "reason": "User expresses frustration and urgency."
}}

Message:
{user_message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    try:
        return json.loads(text)
    except Exception:
        return {
            "persona": "Frustrated User",
            "reason": "Fallback classification"
        }

if __name__ == "__main__":

    test = input("Enter message: ")

    result = classify_persona(test)

    print("\nDetected Persona:")
    print(result)