import pandas as pd

df = pd.read_csv("pokemon.csv")

group = df.groupby("Type 1")
legend = df.groupby("Legendary")

# print(group["Type 1"].count())
# print(group["Attack"].mean())

table_agg = group.agg (
    CountName = ('Name', 'count'),
    Avgattack = ('Attack', 'mean')
)
print(table_agg)

print(legend["HP"].sum())

