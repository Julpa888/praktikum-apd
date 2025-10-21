#SET

# Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
#print(buah)
# for i in buah:
#     print(i, end=" ")

# angka=(1,1,2,3,3,4,5,6) #konversi

# unik=set(angka)
# print(unik)


#DICTIONARY

#buku1=kunci
#bumimanusia=vallue

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku)
# print(Daftar_buku["Buku1"])
# print(Daftar_buku.keys())


Biodata = {
    "Nama" : "Ananda Daffa Harahap",
    "NIM" : 2409106050,
    "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Algoritma", "Jaringan komputer"],
    "Mahasiswa_Aktif" : True,
    "Social Media" : {"Instagram" : "daffahrhap"
    }
}
print(Biodata.get("KRS")[1:-1])


# list_mahasiswa = dict(nama='dapupu', jurusan='informatika')
# print(list_mahasiswa)

# # for i,j in Biodata.items():
# #     # print(i) #key
# #     print(j) #vallue

# for i,j in Biodata.items():
#     print(i ":" j)

#key tidak error tapi jadi none jika key nya tidak ada

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("nama")}")
# print(Biodata.get('Nama'))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# Nilai = { 
#     "Matematika": 80, 
#     "B. Indonesia": 90, 
#     "B. Inggris": 81, 
#     "Kimia": 78, 
#     "Fisika": 80 
# } 

# Tanpa menggunakan items() 
# for i in Nilai: 
#     print(i) 

# print("")  # pemisah 

# # Menggunakan items() 
# for i, j in Nilai.items(): 
#     print(f"Nilai {i} anda adalah {j}")

#Sebelum Ditambah
#print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# # #Setelah Ditambah
# print(Film)

# hapus = Film.pop("The Conjuring")
# print(Film)
#update jika key belum ada di dictionary akan tetap nambah tapi lebih ribet
# #Sebelum Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'}
# #Setelah Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours':
# 'Thriller'}


# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror" 
# }

#Sebelum Ditambah 
# print(Film) 
# Film["Zombieland"] = "Comedy" 
# Film.update({"Hours" : "Thriller"}) 
# print("")
# #Setelah Ditambah
# print("Setelah ditambah")
# print(Film)

# print("j")

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])
# print(Musik["Neffex"][1][1])

# a = {10,11,12}
# b = {11,13,14}

# # c = a & b #irisan hanya print yang sama

# c=a|b #print gabungan tapi tidak duplikat
# print(c)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# # print(Nilai)
# # print("")
# #menggunakan setdefault #hanya print nilai
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)
# {'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
# 81}
# Nilai : 70
# {'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
# 81, 'Kimia': 70}

# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     for j in i :
#         print (j)
