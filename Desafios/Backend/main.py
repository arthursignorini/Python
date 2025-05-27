from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Minha primeira API", description="Aprendendo backend com Python")

class Produto (BaseModel):
    id: int
    nome: str
    preco: float
    estoque: int

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "estoque": 10},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "estoque": 25},
    {"id": 3, "nome": "Teclado", "preco": 150.00, "estoque": 15}
]

@app.get("/")
def home():
    return {"mensagem":"Bem vindo à minha API"}

@app.get("/produtos")
def listarProdutos():
    return produtos

@app.get("/produtos/{produto_id}", response_model=Produto)
def buscarProduto(produto_id: int):
    for produto in produtos:
        if(produto["id"] == produto_id):
            return produto

@app.post("/produtos", response_model=Produto)
def cadastrarProduto(produto: Produto):
    for p in produtos:
        if (produtos["nome"] == produto.nome):
            raise HTTPException(status_code=400, detail="Já existe um produto com esse nome")

    novoProduto = produto.dict()
    produtos.append(novoProduto)

    return novoProduto


@app.put("/produtos/{produto_id}", response_model=Produto)
def atualizar_produto(produto_id: int, produto_atualizado: Produto):
    for i, produto in enumerate(produtos):
        if produto["id"] == produto_id:
            # Atualizar os dados
            produtos[i] = produto_atualizado.dict()
            return produtos[i]
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    for i, produto in enumerate(produtos):
        if produto["id"] == produto_id:
            produtos.pop(i)
            return {"mensagem": f"Produto {produto_id} deletado com sucesso"}
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")