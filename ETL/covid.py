import requests
import pandas as pd

url = "https://covid19-brazil-api.vercel.app/api/report/v1"
res = requests.get(url).json()
df = pd.DataFrame(res["data"])
print(df[["uf", "cases", "deaths"]])

print(df[["cases", "deaths"]].describe())

df["taxa_mortalidade"] = df["deaths"] / df["cases"]
print(df[["uf", "taxa_mortalidade"]].sort_values(by="taxa_mortalidade", ascending=False))