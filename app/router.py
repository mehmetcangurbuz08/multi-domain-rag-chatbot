import re
from typing import Literal, Tuple, Dict
from app.retriever import Retriever

# Anahtar kelime listeleri
HEALTH_KWS = [
    r"\b(patient|clinic|treatment|diagnosis|symptom|medicine|hastalık|tedavi|ateş|öksürük|kanser|şeker)\b",
]

FASHION_KWS = [
    r"\b(outfit|sneaker|trend|dress|fabric|style|kombin|moda|elbise|pantolon|ayakkabı)\b",
]

def keyword_score(q: str) -> Tuple[float, float]:
    ql = q.lower()
    h = sum(bool(re.search(p, ql)) for p in HEALTH_KWS)
    f = sum(bool(re.search(p, ql)) for p in FASHION_KWS)
    return float(h), float(f)

def pick_domain(q: str, retr: Retriever) -> Tuple[Literal["healthcare", "fashion"], Dict]:
    # 1) keyword sinyali
    kh, kf = keyword_score(q)

    # 2) retrieval sinyali
    both = retr.search_all(q, k=1)
    rh = both["healthcare"][0]["score"] if both["healthcare"] else 0.0
    rf = both["fashion"][0]["score"] if both["fashion"] else 0.0

    # 3) skorları birleştir
    h_score = 1.2 * kh + rh
    f_score = 1.2 * kf + rf

    domain = "healthcare" if h_score >= f_score else "fashion"
    hits = retr.search_domain(domain, q, k=3)

    return domain, {
        "domain_score": {"healthcare": h_score, "fashion": f_score},
        "hits": hits
    }
