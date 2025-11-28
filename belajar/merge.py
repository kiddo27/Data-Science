import pandas as pd


data_mahasiswa = {
    "nim" : [101,102,103,104,105,107,109,111],
    "nama" : ["Andi", "Budi", "Chika", "Dewi", "Eka", "Gita", "Indah", "Zul"],
    "fakultas_kode" : ["FASILKOM", "FE", "FASILKOM", "FMIPA", "FE", "FASILKOM", "FMIPA", "FAPERTA"]
}

data_fakultas = {
    "fakultas_kode" : ["FASILKOM","FE","FMIPA","FATETA"],
    "nama_fakultas" : ["Fakultas Ilmu Komputer", "Fakultas Ekonomi", "Fakultas MIPA", "Fakultas Teknologi Pertanian"],
    "gedung" : ["Gedung A", "Gedung B", "Gedung C", "Gedung D"]
}

mahasiswa = pd.DataFrame(data_mahasiswa)

fakultas = pd.DataFrame(data_fakultas)


inner_join = pd.merge(mahasiswa,fakultas, on="fakultas_kode",how="inner")

left_join = pd.merge(mahasiswa,fakultas, on="fakultas_kode" ,how="left")

right_join = pd.merge(mahasiswa, fakultas,on="fakultas_kode" ,how="right")

right_join_group = right_join.groupby("nama_fakultas")


print(inner_join)

print(left_join)

print(right_join_group["nama"].count())
