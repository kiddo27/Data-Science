import pandas as pd

df = pd.read_csv("pokemon.csv")

#selection by column

print(df["Name"].to_string())