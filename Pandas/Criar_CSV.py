import csv

# Dados para escrever no CSV
dados = [
    ["ID", "Produto", "Quantidade", "Preço"],
    [1, "Notebook", 2, 3500.00],
    [2, "Mouse", 5, 150.00],
    [3, "Teclado", 3, 200.00],
    [4, "Monitor", 1, 1200.00],
    [5, "Impressora", 2, 800.00],
]

# Criando um arquivo CSV
with open("vendas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")
