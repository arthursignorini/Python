from fastapi import FastAPI
from pydantic import BaseModel
from utils import *
import openai
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="RAG da sua empresa")
texts, sources = load_pdfs("docs")
index, embeddings = create_faiss_index(texts)
save_index(index)

class Query(BaseModel):
    pergunta: str

@app.post("/query")
def consultar(query: Query):
    vector = embed_query(query.pergunta)
    D, I = index.search(np.array(vector), k=3)  # top 3 similares
    contextos = "\n\n".join([texts[i] for i in I[0]])

    prompt = f"""Você é um assistente inteligente que responde com base nos documentos da empresa.
Responda com base apenas nas informações abaixo:

{contextos}

Pergunta: {query.pergunta}
Resposta:"""

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "resposta": resposta['choices'][0]['message']['content'],
        "fontes": [sources[i] for i in I[0]]
    }
