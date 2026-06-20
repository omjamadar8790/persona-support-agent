\# Persona-Adaptive Customer Support Agent



\## Overview



This project is an AI-powered customer support agent that adapts its responses based on the customer's persona. The system detects customer type, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), generates persona-aware responses, and escalates unresolved issues to human support agents.



Supported Personas:



\* Technical Expert

\* Frustrated User

\* Business Executive



\---



\## Tech Stack



\### Language



\* Python 3.11



\### LLM



\* Google Gemini 2.5 Flash



\### Embeddings



\* Gemini Embedding Model



\### Vector Database



\* ChromaDB



\### Frameworks



\* Streamlit

\* LangChain Text Splitters



\### Other Libraries



\* python-dotenv

\* google-genai



\---



\## Architecture



User Query



↓



Persona Detection



↓



Knowledge Retrieval (RAG)



↓



Response Generation



↓



Escalation Check



↓



Human Handoff Summary



\---



\## Persona Detection Strategy



The system uses Gemini to classify incoming messages into one of three personas:



\### Technical Expert



Uses technical terminology and requests detailed explanations.



\### Frustrated User



Uses emotional language and urgent requests.



\### Business Executive



Focuses on outcomes, business impact, and resolution timelines.



\---



\## RAG Pipeline



1\. Load support documents from data folder.

2\. Split documents into chunks.

3\. Generate embeddings using Gemini.

4\. Store vectors in ChromaDB.

5\. Retrieve top relevant chunks.

6\. Provide retrieved context to Gemini.



Metadata includes:



\* Source document

\* Chunk number



\---



\## Escalation Logic



Escalation occurs when:



\* Billing issues are detected

\* Refund requests are detected

\* Legal or account-sensitive requests arise

\* No relevant documentation is available



The system generates a structured handoff summary for human agents.



\---



\## Setup



\### Clone Repository



git clone <repository-url>



cd persona-support-agent



\### Create Virtual Environment



python -m venv venv



venv\\Scripts\\activate



\### Install Dependencies



pip install -r requirements.txt



\### Configure Environment



Create .env file:



GEMINI\_API\_KEY=your\_api\_key\_here



\### Run Application



streamlit run app.py



\---



\## Example Queries



1\. I've been trying for two hours and nothing works!



2\. What are the header requirements for bearer token authentication?



3\. Our operational uptime is decreasing. When will this issue be resolved?



4\. I want an immediate refund for duplicate charges.



5\. My account remains locked after multiple login attempts.



\---



\## Knowledge Base



The project contains support articles covering:



\* Password reset

\* Billing policy

\* Payment failures

\* API troubleshooting

\* Browser cache issues

\* Subscription management

\* Account lockouts

\* Token authentication

\* Database integration

\* Uptime SLA



\---



\## Future Improvements



\* Multi-turn conversation memory

\* Confidence scoring

\* LangGraph workflow

\* Human approval workflow

\* Analytics dashboard

\* Sentiment analysis



\---



\## Author



Om Jamadar



