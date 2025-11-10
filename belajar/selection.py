import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

#selection by column

# print(df["Name"]) ##mencari berdasarkan kolom Name

# multiple column
# print(df[["Name", "Height", "Weight"]].to_string())

# SELECTION BY ROWS

# print(df.loc["Eevee" : "Flareon", ["Height", "Weight"]])

# memilih data dari A - B

# print(df.iloc[0:11:2, 0:3])  ##argumen pertama untuk menentukan banyak rows, argumen kedua banyak kolom


pokemon = input("masukkan nama pokemon: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")