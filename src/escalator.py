import json

SENSITIVE_TOPICS = [
    "refund",
    "billing",
    "charge",
    "payment",
    "legal",
    "lawsuit",
    "account deletion"
]

def should_escalate(user_query):

    query = user_query.lower()

    for item in SENSITIVE_TOPICS:
        if item in query:
            return True

    return False

def generate_handoff(persona, user_query, docs):

    return {
        "persona": persona,
        "issue": user_query,
        "documents_used": docs,
        "attempted_steps": [],
        "recommendation": "Human review required."
    }