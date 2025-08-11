# 🤖 Multi-Domain RAG Chatbot

A **FastAPI-based**, multi-domain **Retrieval-Augmented Generation (RAG)** chatbot.  
The system automatically detects the domain of the incoming query (Healthcare / Fashion), retrieves the most relevant documents from the corresponding **FAISS** vector database, and generates a fast response using the **Groq API**.

## ✨ Features
- 🔍 **Automatic domain detection** (Healthcare & Fashion, easily extendable)
- ⚡ Fast in-memory search with **FAISS** vector store
- 🤖 **Groq API** for low-latency text generation
- 🚀 **FastAPI** REST service with auto-generated Swagger UI (`/docs`)
- 🛡 **Stateless** — no conversation history is stored
- 📂 **Easily extensible** domain architecture

## 📂 Project Structure
```plaintext
.
├── app
│   ├── __init__.py           # Package initializer
│   ├── api.py                # FastAPI endpoints
│   ├── embed.py              # Embedding creation logic
│   ├── generator.py          # Groq API answer generation
│   ├── models.py             # Pydantic models
│   ├── prompts.py            # Domain-specific prompts
│   ├── retriever.py          # FAISS vector retrieval logic
│   └── router.py             # Domain detection logic
├── data/
│       ├── fashion/          # Fashion domain documents
│       └── healthcare/       # Healthcare domain documents
└── indices/                  # Prebuilt FAISS vector index files
│       ├── fashion_meta.pkl
│       ├── fashion_vecs.npy 
│       ├── healthcare_meta.pkl
│       └── healthcare_vecs.npy     
├── scripts/
│   └── build_index.py        # Script to build FAISS indices
├── tests/                    # Unit tests
│   ├── retriever_test.py
│   └── router_test.py
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```
## ⚙️ Installation

### 1️⃣ Clone the repository
git clone https://github.com/<username>/multi-domain-rag-chatbot.git
cd multi-domain-rag-chatbot

### 2️⃣ Create a virtual environment
# macOS / Linux
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Set your Groq API key
# macOS / Linux
export GROQ_API_KEY="your_groq_api_key"

# Windows (PowerShell)
setx GROQ_API_KEY "your_groq_api_key"

## ▶️ Running the API
uvicorn app.api:app --reload --port 8000
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

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

## 🛠 Technologies Used
- FastAPI: https://fastapi.tiangolo.com/
- FAISS: https://faiss.ai/
- Groq API: https://groq.com/
- Pydantic: https://docs.pydantic.dev/

## 📜 License
This project is private. All rights reserved.
