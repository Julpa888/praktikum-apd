import os
clear_cmd="cls" if os.name == "nt" else "clear"

#USERNAME DAN PASSWORD TERDAFTAR
admin_usn=("Julpa", "Triya", "Pernan", "Nabil") #Izin pakai namanya ya abang/mba
admin_pw=("Pentol", "Aslab", "123", "2025")
usn=("Shasha", "Aya", "Mariska", "Nisa", "Intan")
pw=("Teman", "Teman1", "Teman2", "1010", "2345")

#LIST UTAMA DRAMA KOREA DENGAN RATING DI ATAS 9.0
romance=["Crash Landing on You", "Goblin", "Strong Woman Do Bong Soon"]
crime=["Vincenzo", "Vagabond", "Taxi Driver"]
historical=["Alchemy of Souls", "Mr. Queen","Hwarang"]
scifi=["Sweet Home", "All of Us Are Dead", "Duty After School"]
youth=["Weak Hero Class", "Study Group", "Twinkling Watermelon"]

#NESTED LIST UNTUK DIPANGGIL
list_genre=[
    ["ROMANCE",romance],
    ["CRIME",crime],
    ["HISTORICAL",historical],
    ["SCI-FI",scifi],
    ["YOUTH",youth]
]

daftar_genre=[romance, crime, historical, scifi, youth]

while True:
    print("""
        ======================================================================
        |      SELAMAT DATANG DI BLOG DAFTAR DRAMA KOREA FAVORIT DUNIA!      |      
        ======================================================================
        """)
    print("""
        HALAMAN MENU!
        1. LOGIN
        2. REGISTRASI
        """)
    opsi=int(input("\nSilahkan pilih opsi (1/2): ")) 
    input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
#MENU REGISTRASI & LOGIN
    if opsi==2:
        print("===== SILAHKAN REGISTRASI MEMBER! =====")
        while True:
            usn_baru=input("\nPilih username anda: ")
            pw_baru=input("Masukkan password: ")
            if usn_baru in usn or usn_baru in admin_usn:
                print("Username telah dipakai, silahkan pilih yang lain!")
                input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                continue
            else:
                print("\n--- Registrasi member berhasil, selamat bergabung di komunitas! ---")
                input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                print("===== SILAHKAN LOGIN =====")
                while True:
                    usn_login=input("\nSilahkan masukkan username: ")
                    pw_login=input("Silahkan masukkan password: ")
                    if usn_login!= usn_baru or pw_login!= pw_baru:
                        print("\nFormat salah, login gagal!")
                        input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                    else:
                        is_admin=False
                        print("\n--- Login berhasil, selamat datang member! ---")
                        input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                        break
            break
        break

#MENU LOGIN TANPA REGISTRASI
    elif opsi==1:
        print("===== SILAHKAN LOGIN =====")
        while True:
            usn_login=input("\nSilahkan masukkan username: ")
            pw_login=input("Silahkan masukkan password: ")
            if usn_login in admin_usn and pw_login in admin_pw: #Menu login admin
                is_admin=True
                print("\n--- Login berhasil, selamat datang admin! ---")
                input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                break
            elif usn_login in usn and pw_login in pw: #Menu login member
                is_admin=False
                print("\n--- Login berhasil, selamat datang member! ---")
                input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                break
            else:
                print("\nFormat salah, login gagal!")
                input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
        break

    else:
        print("Error! Pilihan tidak valid!")
        input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)


while True:
    print("\nMENU AKSES")
    print("""
    ==============================================
    |      DAFTAR DRAMA KOREA FAVORIT DUNIA      |
    ==============================================
    | 1. Menampikan Daftar                       |
    | 2. Membuat Daftar                          |
    | 3. Mengganti Daftar                        |
    | 4. Menghapus Daftar                        |
    | 5. Keluar                                  |
    ==============================================
    """)
    menu=int(input("\n(Silahkan pilih opsi 1-5): "))
    # input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)

#READ DATA
    if menu==1:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            for nomor, (nama, daftar) in enumerate(list_genre, start=1):
                print(f"{nomor}. {nama} :", end=" ")
                for i in range(len(daftar)):
                    print(daftar[i], end=", " if i != len(daftar)-1 else "\n")
            input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)

#CREATE DATA
    elif menu==2:
            if is_admin==False:
                print("\nUPSSS! Hanya bisa diakses oleh admin, silahkan pilih opsi lain!")
                continue
            elif is_admin==True:
                print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
                print()
                for nomor, (nama, daftar) in enumerate(list_genre, start=1):
                    print(f"{nomor}. {nama} :", end=" ")
                    for i in range(len(daftar)):
                        print(daftar[i], end=", " if i != len(daftar)-1 else "\n")
                nomor=int(input("\nPilih genre yang ingin ditambah (1-5): "))
                if nomor==1:
                    genre=romance
                elif nomor==2:
                    genre=crime
                elif nomor==3:
                    genre=historical
                elif nomor==4:
                    genre=scifi
                elif nomor==5:
                    genre=youth
                else:
                    print("\nNomor genre tidak valid!")
                    continue
                judul_baru=input("Masukkan judul yang ingin ditambah: ")
                genre.append(judul_baru)
                print()
                print(genre)
                print("\nData berhasil ditambahkan!")
                input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)

#UPDATE DATA
    elif menu==3:
            print("\n===== DAFTAR GENRE DAN ISINYA =====")
            print()
            for nomor, (nama, daftar) in enumerate(list_genre, start=1):
                print(f"{nomor}. {nama} :", end=" ")
                for i in range(len(daftar)):
                    print(daftar[i], end=", " if i != len(daftar)-1 else "\n")
            nomor=int(input("\nSilahkan pilih genre yang ingin diubah (1-5): "))
            judul_baru=input("Silahkan masukkan judul baru: ")
            if 1<=nomor<=len(daftar_genre):
                index=int(input("Masukkan index judul yang ingin diubah (0-2): "))
                daftar_genre[nomor-1][index]=judul_baru
                print("\nData berhasil diubah!")
            else:
                print("Nomor genre tidak valid!")
            input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)

#DELETE DATA
    elif menu==4:
            print("\n===== DAFTAR GENRE DAN ISINYA =====")
            print()
            for nomor, (nama, daftar) in enumerate(list_genre, start=1):
                print(f"{nomor}. {nama} :", end=" ")
                for i in range(len(daftar)):
                    print(daftar[i], end=", " if i != len(daftar)-1 else "\n")
            nomor=int(input("\nSilahkan pilih genre yang ingin dihapus (1-5): "))
            if nomor==1:
                genre=romance
            elif nomor==2:
                genre=crime
            elif nomor==3:
                genre=historical
            elif nomor==4:
                genre=scifi
            elif nomor==5:
                genre=youth
            else:
                print("\nNomor genre tidak valid!")
                continue
            index=int(input("Silahkan masukkan index yang ingin dihapus (0-2): "))
            genre.pop(index)
            print(genre)
            print("\nData berhasil dihapus!")
            input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)

#KELUAR
    elif menu==5:
            input("\nTekan ENTER untuk keluar server!..."); os.system(clear_cmd)
            break
    else:
        print("\nError! Pilihan tidak valid!")
        input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)

