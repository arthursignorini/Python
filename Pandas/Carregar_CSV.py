import pandas as pd

df = pd.read_csv(r"C:\Users\phpmm\Documents\Puc\GITHUB\Python\Pandas\dados.csv")
print(df.head()) # head mostra as 5 primeiras linhas
print(df.describe()) # estatísticas básicas


# describe
#             ID  Quantidade        Preço
# count  5.000000    5.000000     5.000000 Número de valores não nulos em cada coluna
# mean   3.000000    2.600000  1170.000000 Média 
# std    1.581139    1.516575  1373.681186 Desvio padrão
# min    1.000000    1.000000   150.000000 Menor valor da coluna
# 25%    2.000000    2.000000   200.000000 Primeiro quartil 
# 50%    3.000000    2.000000   800.000000 Segundo quartil
# 75%    4.000000    3.000000  1200.000000 Terceiro quartil
# max    5.000000    5.000000  3500.000000 Quarto quartil
