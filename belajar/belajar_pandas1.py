import pandas as pd

# series adalah 1 dimensional labeled array, simplenya dia mirip kolom di excel

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index = ["a", "b", "c", "d", "e"])

#loc itu location

# print(series.loc["a"]) ini buat akses suatu nilai dari series

#untuk mengakses nilai dari suatu series bisa akses loc nya terus ubah value nya, contohnya kaya gini

#bisa juga akses nilainya kaya akses nilai array biasa pake iloc, contoh:

print(series.iloc[0])

series.loc["a"] = 200  

print(series) 

# ini buat filter nilai apa aja yang mau di print
print(series[series <= 200])