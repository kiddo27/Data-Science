import pandas as pd

data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}

# DataFrame(df) adalah tabel
df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

# untuk mengakses nya sama seperti series bisa pakai loc dan iloc


# add new column

df["Job"] = ["Cook", "N/A", "Cashier"]


# add new row

new_rows = pd.DataFrame([{
    "Name" : "Sandy",
    "Age" : 28,
    "Job": "Engineer"
}, {
    "Name" : "Mr.Krab",
    "Age" : 40,
    "Job" : "Manager"
}
],
    index = ["Employee 4", "Employee 5"])

df = pd.concat([df, new_rows])

print(df)