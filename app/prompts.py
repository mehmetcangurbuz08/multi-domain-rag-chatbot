# app/prompts.py
HEALTH_TEMPLATE = """You are a helpful assistant for healthcare Q&A.
Use the context to answer briefly and clearly.
Context:
{context}

User question: {query}
Answer:"""

FASHION_TEMPLATE = """You are a helpful assistant for fashion styling.
Use the context to answer briefly and clearly.
Context:
{context}

User question: {query}
Answer:"""

def make_prompt(domain: str, query: str, passages: list[dict]) -> str:
    ctx = "\n---\n".join(p["text"] for p in passages)
    if domain == "healthcare":
        return HEALTH_TEMPLATE.format(context=ctx, query=query)
    return FASHION_TEMPLATE.format(context=ctx, query=query)
