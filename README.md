# Multi-Domain RAG Chatbot

FastAPI-based **multi-domain Retrieval-Augmented Generation (RAG) chatbot** with FAISS vector store and Groq-powered generation.

The chatbot automatically detects the query's domain (e.g., Healthcare or Fashion), retrieves top relevant documents from the appropriate vector store, and generates a domain-specific answer.

## 🚀 Features

- **Multi-domain support** → Healthcare & Fashion (easily extendable)
- **Domain detection** based on query content
- **FAISS** in-memory vector store for fast retrieval
- **Groq API** for fast and low-latency generation
- **FastAPI** REST service with auto-generated Swagger UI (`/docs`)
- **Stateless** request handling — no conversation history needed

## 📂 Project Structure

.
├── app
│ ├── api.py # FastAPI endpoints
│ ├── retriever.py # Vector DB retrieval logic
│ ├── router.py # Domain detection
│ ├── generator.py # Groq-powered answer generation
│ └── data/ # Domain-specific documents
├── requirements.txt
└── README.md

## 🛠 Installation

1. **Clone the repo**
   git clone https://github.com/<your-username>/multi-domain-rag-chatbot.git
   cd multi-domain-rag-chatbot

2. **Create virtual environment**
   python -m venv .venv
   source .venv/bin/activate # macOS/Linux
   .venv\Scripts\activate # Windows

3. **Install dependencies**
   pip install -r requirements.txt

4. **Set your Groq API key**
   export GROQ_API_KEY="your_groq_api_key" # macOS/Linux
   setx GROQ_API_KEY "your_groq_api_key" # Windows (permanent)

## ▶️ Running the API

uvicorn app.api:app --reload --port 8000

- API runs at: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

## 📌 Example Request

POST /chat  
Request body:
{
"query": "Fever and cough, what should I do?"
}

Example response:
{
"domain": "healthcare",
"answer": "If you have fever and cough, check for red flags such as shortness of breath...",
"source": [
{ "id": "healthcare-1", "doc": "fever_cough_triage.txt", "score": 0.69 }
]
}

## 📄 License

Private repository — All rights reserved.
