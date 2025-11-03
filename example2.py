import pandas as pd

data = {
    "ID" : [2001, 2002, 2003],
    "Nama_barang" : ["Mouse", "Keyboard", "Deskmate"],
    "Harga" : [2000, 5000, 3000]
}

df = pd.DataFrame(data, index = ["Barang 1", "Barang 2", "Barang 3"])

# add new column

df["Stok"] = [5,7,3]

# add new rows

new_rows = pd.DataFrame([{
    "ID" : 2004,
    "Nama_barang" : "Gamepad",
    "Harga" : 2500,
    "Stok" : 10
},{
    "ID" : 2005,
    "Nama_barang" : "Steering Wheel",
    "Harga" : 7000,
    "Stok" : 5
}],
    index = ["barang 4" , "barang 5"])

df = pd.concat([df, new_rows])

print(df)