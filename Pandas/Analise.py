import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('vendas.csv')

# Visualizando as 5 primeiras linhas
print("Primeiras 5 linhas dos dados:")
print(df.head())

# Conversão de 'Data' para o formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Calcular a coluna 'Total' como quantidade * preço
df['Total'] = df['Quantidade'] * df['Preço']

# Excluir linhas com valores ausentes (caso existam)
df = df.dropna()

# Exibir estatísticas básicas de todas as colunas numéricas
print("\nEstatísticas básicas:")
print(df.describe())

# Agrupar os dados por 'Produto' e calcular a soma total de vendas por produto
agrupado_produto = df.groupby('Produto')['Total'].sum().reset_index()

# Exibir os totais de vendas por produto
print("\nTotal de vendas por produto:")
print(agrupado_produto)

# Filtrar as vendas realizadas em 2023-01-01
vendas_01_01 = df[df['Data'] == '2023-01-01']

# Exibir as vendas de 2023-01-01
print("\nVendas realizadas em 2023-01-01:")
print(vendas_01_01)

# Calcular a média de vendas por dia
media_por_dia = df.groupby(df['Data'].dt.date)['Total'].mean().reset_index()

# Exibir a média de vendas por dia
print("\nMédia de vendas por dia:")
print(media_por_dia)

# Salvar a análise de vendas por produto em um novo CSV
agrupado_produto.to_csv('total_vendas_por_produto.csv', index=False)

