# app/generator.py
from typing import List, Dict
from app.prompts import make_prompt

from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()  # .env varsa okusun

# Ortamdan anahtarı al
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# modeli ayarla
# (örneğin, "llama-3.1-8b-instant" veya "llama-3.1-70b-versatile")
MODEL = "llama-3.1-8b-instant"  # alternatif: "llama-3.1-70b-versatile"

def generate_answer(domain: str, query: str, passages: List[Dict]) -> str:
    if not passages:
        return f"{domain} için uygun kaynak bulamadım; soruyu biraz daha spesifikleştirebilir misin?"

    prompt = make_prompt(domain, query, passages)

    # Sistem talimatı: sadece verdiğimiz bağlamdan yararlan
    messages = [
        {"role": "system", "content": "You are a concise assistant. Use ONLY the provided context. If context is insufficient, say you don't know."},
        {"role": "user", "content": prompt},
    ]

    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.2,
        max_tokens=220,
    )
    return resp.choices[0].message.content.strip()
