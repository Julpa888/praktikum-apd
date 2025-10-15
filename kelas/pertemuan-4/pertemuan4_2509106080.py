# ulangi = 10
# for i in range (ulangi):
#     print(f'Perulangan ke {i}')

# for i in range (1, 10):
#     print(f'Perulangan ke {i}')

# for i in range (1, 10, 2): #step 2
#     print(f'Perulangan ke {i}')

# for i in range (10, 1, -1): #terbalik
#     print(f'Perulangan ke {i}')

# simpan = [1, 'Dapupu', 4.00, True] #for pada list
# for i in simpan:
#     print(i)

# mahasiswa=[] #print mahasiswa nya
# for i in "mahasiswa":
#     print(i)

# for i in 123: #error
#     print(i)

def tugas(a,b): #parameter pak awang
    for i in range(b):
        print(a, end="")
    print()
tugas('@',9)
tugas('%',15)
tugas('@',30)


# for i in range(1, 5):
#     for j in range(1,i+1,):
#         print(i, end="")
#     # print("")
#     print(" =", i*i)

# def tugas('@',7)
    

# for i in range(1):
#     for j in range(1, i+1):
#         print("1", end=" ")
#     print("")

#WHILE LOOP

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
# print(f"Total perulangan: {hitung}")

#break

# angka = [2, 5, 8, 12, 15, 7, 20]

# print("Mencari angka pertama yang lebih besar dari 10...")

# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#     break

# print("Program selesai.")

# while True:
#     print("MENU")
#     print("1. fitur 1")
#     print("2. fitur 2")
#     opsi=int(input("Masukkan opsi: "))
#     if opsi==1:
#         print("1. Fitur 1")
#     elif opsi==2:
#         print("2. Fitur 2")
#     elif opsi==3:
#         print("2. Fitur 2")
#         break
#     else:
#         print("Pilihan invalid")