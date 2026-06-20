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
Classify this customer support message into ONE category:

1. Technical Expert
2. Frustrated User
3. Business Executive

Return ONLY JSON.

Format:
{{
    "persona": "",
    "reason": ""
}}

Message:
{user_message}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        try:
            return json.loads(text)

        except Exception:

            if "frustrat" in user_message.lower():
                return {
                    "persona": "Frustrated User",
                    "reason": "Fallback classification"
                }

            return {
                "persona": "Technical Expert",
                "reason": "Fallback classification"
            }

    except Exception as e:

        msg = user_message.lower()

        if any(word in msg for word in [
            "refund",
            "billing",
            "charge",
            "payment",
            "duplicate"
        ]):
            persona = "Frustrated User"

        elif any(word in msg for word in [
            "uptime",
            "timeline",
            "business",
            "operational",
            "executive"
        ]):
            persona = "Business Executive"

        else:
            persona = "Technical Expert"

        return {
            "persona": persona,
            "reason": f"Gemini unavailable: {str(e)}"
        }

if __name__ == "__main__":

    test = input("Enter message: ")

    result = classify_persona(test)

    print("\nDetected Persona:")
    print(result)