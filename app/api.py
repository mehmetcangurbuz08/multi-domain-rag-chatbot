# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

from app.retriever import Retriever
from app.router import pick_domain
from app.generator import generate_answer

class ChatRequest(BaseModel):
    query: str

app = FastAPI(title="Multi-domain RAG (demo)")

# retriever'ı bir kez yükle (soğuk başlatma daha hızlı olsun)
retr = Retriever()

@app.get("/")
def health():
    return {"ok": True}

@app.post("/chat")
def chat(req: ChatRequest):
    q = req.query.strip()
    if not q:
        return {"answer": "Soru boş olamaz.", "source": []}

    domain, info = pick_domain(q, retr)
    hits = info["hits"]
    answer = generate_answer(domain, q, hits)
    sources = [{"id": h["id"], "doc": h["doc"], "score": h["score"]} for h in hits]

    return {
        "domain": domain,
        "answer": answer,
        "source": sources,
        "debug": info["domain_score"],  # ister kaldır
    }
