import pandas as pd

#Filtering is keeping the rows that match a condition

df = pd.read_csv("data.csv")

# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

# heavy_pokemon = df[df["Weight"] >= 100]

# print(heavy_pokemon)

# fire_type = df[(df["Type1"] == "Fire") | (df["Type2"] == "Fire")]
# print(fire_type)
Grass_Poison = df[(df["Type1"] == "Grass") & (df["Type2"] == "Poison")]
print(Grass_Poison)

# legendary_pokemon = df[df["Legendary"] == 1]

# print(legendary_pokemon)