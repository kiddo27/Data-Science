import pandas as pd

df = pd.read_csv("data.csv")

# mean gabisa ngitung kalau ada yang ga numerik, jadi tambahin numeric_only = true
# print(df.mean(numeric_only=True))

# sum
# print(df.sum(numeric_only=True))

# # mininum
# print(df.min(numeric_only=True))

# # maximum
# print(df.max(numeric_only=True))

# count => menghitung jumlah data setiap kolom, tanpa NaN value

# print(df.count())


# bisa juga menghitung untuk masing masing column

# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())
group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())