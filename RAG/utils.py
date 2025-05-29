import os
import faiss
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_pdfs(folder_path):
    chunks = []
    sources = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, filename))
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            for i in range(0, len(text), 500):
                chunk = text[i:i+500]
                chunks.append(chunk)
                sources.append(filename)
    return chunks, sources

def create_faiss_index(texts):
    embeddings = model.encode(texts)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings

def save_index(index, path="index.faiss"):
    faiss.write_index(index, path)

def load_index(path="index.faiss"):
    return faiss.read_index(path)

def embed_query(query):
    return model.encode([query])
