from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# teste entrada da API
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem vindo à minha API"}

# teste ler produtos
def test_lerProdutos():
    response = client.get("/produtos")
    assert response.status_code == 200

# teste cadastro de produto
def test_cadastrar_produto():
    novo_produto = {
        "id": 10,
        "nome": "Fone de ouvido",
        "preco": 99.90,
        "estoque": 30
    }

    response = client.post("/produtos", json=novo_produto)
    assert response.status_code == 200
    assert response.json()["nome"] == "Fone de ouvido"

# teste edição produto
def test_editar_produto():
    produtoAtualizado = {
        "id": 2,
        "nome": "Bola",
        "preco": 314,
        "estoque": 50
    }

    response = client.put("/produtos/1", json=produtoAtualizado)
    assert response.status_code == 200
    assert response.json()["nome"] == "Bola"