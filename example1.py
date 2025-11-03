import pandas as pd


pokedex = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmender", "Charmeleon", "Charizard"]

series = pd.Series(pokedex, index = [1,2,3,4,5,6])

print(series)