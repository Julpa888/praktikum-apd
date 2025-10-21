import os
clear_cmd="cls" if os.name == "nt" else "clear"

#USERNAME DAN PASSWORD TERDAFTAR
akun_admin={
    "Julpa":"Pentol",
    "Triya":"Aslab",
    "Pernan":"123",
    "Nabil":"2025"
}
akun_member={
    "Shasha":"Teman",
    "Aya":"Teman1",
    "Mariska":"Teman2",
    "Nisa":"1010",
    "Intan":"2345"
}

#DICTIONARY DRAMA KOREA DENGAN RATING DI ATAS 9.0
drama_korea = {
    "ROMANCE": ["Crash Landing on You", "Goblin", "Strong Woman Do Bong Soon"],
    "CRIME": ["Vincenzo", "Vagabond", "Taxi Driver"],
    "HISTORICAL": ["Alchemy of Souls", "Mr. Queen", "Hwarang"],
    "SCI-FI": ["Sweet Home", "All of Us Are Dead", "Duty After School"],
    "YOUTH": ["Weak Hero Class", "Study Group", "Twinkling Watermelon"]
}

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
            if usn_baru in akun_member or usn_baru in akun_admin:
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
            if usn_login in akun_admin and akun_admin[usn_login]==pw_login: #Menu login admin
                is_admin=True
                print("\n--- Login berhasil, selamat datang admin! ---")
                input("\nTekan ENTER untuk melanjutkan..."); os.system(clear_cmd)
                break
            elif usn_login in akun_member and akun_member[usn_login]==pw_login: #Menu login member
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


if is_admin==True:
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

#READ DATA
        if menu == 1:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            for i, (genre, daftar) in enumerate(drama_korea.items(), start=1):
                print(f"{i}. {genre} : ", end="")
                for j in range(len(daftar)):
                    print(daftar[j], end=", " if j < len(daftar) - 1 else "")
                print()
            input("\nTekan ENTER untuk kembali ke menu...")
            os.system(clear_cmd)

#CREATE DATA
        elif menu == 2:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            for i, (genre, daftar) in enumerate(drama_korea.items(), start=1):
                print(f"{i}. {genre} : ", end="")
                for j in range(len(daftar)):
                    print(daftar[j], end=", " if j < len(daftar) - 1 else "")
                print()
            nomor = int(input("\nPilih genre yang ingin ditambah (1-5): "))
            daftar_genre = list(drama_korea.keys())
            if 1 <= nomor <= 5:
                genre = daftar_genre[nomor - 1]
                judul_baru = input("Masukkan judul yang ingin ditambah: ")
                drama_korea[genre].append(judul_baru)
                print()
                print(drama_korea[genre])
                print("\nData berhasil ditambahkan!")
            else:
                print("\nNomor genre tidak valid!")
            input("\nTekan ENTER untuk kembali ke menu...")
            os.system(clear_cmd)

#UPDATE DATA
        elif menu == 3:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            daftar_genre = list(drama_korea.keys())
            for i, genre in enumerate(daftar_genre, start=1):
                print(f"{i}. {genre} : ", end="")
                daftar = drama_korea[genre]
                for j in range(len(daftar)):
                    print(daftar[j], end=", " if j < len(daftar) - 1 else "")
                print()
            nomor = int(input("\nSilahkan pilih genre yang ingin diubah (1-5): "))
            if 1 <= nomor <= 5:
                genre = daftar_genre[nomor - 1]
                daftar = drama_korea[genre]
                index = int(input("Masukkan index judul yang ingin diubah (0-2): "))
                if 0 <= index < len(daftar):
                    judul_baru = input("Silahkan masukkan judul baru: ")
                    daftar[index] = judul_baru
                    print("\nData berhasil diubah!")
            else:
                print("\nNomor genre tidak valid!")
            input("\nTekan ENTER untuk melanjutkan...")
            os.system(clear_cmd)

#DELETE DATA
        elif menu == 4:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            daftar_genre = list(drama_korea.keys())
            for i, genre in enumerate(daftar_genre, start=1):
                print(f"{i}. {genre} : ", end="")
                daftar = drama_korea[genre]
                for j in range(len(daftar)):
                    print(f"{daftar[j]}", end=", " if j < len(daftar) - 1 else "")
                print()
            nomor = int(input("\nSilahkan pilih genre yang judulnya ingin dihapus (1-5): "))
            if 1 <= nomor <= 5:
                genre = daftar_genre[nomor - 1]
                daftar = drama_korea[genre]
                index = int(input(f"Silahkan masukkan index yang ingin dihapus (0-2): "))
                0 <= index < len(daftar)
                hapus = daftar.pop(index)
                print()
                print(drama_korea[genre])
                print("\nData berhasil dihapus!")
            else:
                print("\nNomor genre tidak valid!")
            input("\nTekan ENTER untuk melanjutkan...")
            os.system(clear_cmd)

#KELUAR
        elif menu==5:
                input("\nTekan ENTER untuk keluar server!..."); os.system(clear_cmd)
                break
        else:
            print("\nError! Pilihan tidak valid!")
            input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)


elif is_admin==False:
    while True:
        print("\nMENU AKSES")
        print("""
        ==============================================
        |      DAFTAR DRAMA KOREA FAVORIT DUNIA      |
        ==============================================
        | 1. Menampikan Daftar                       |
        | 2. Mengganti Daftar                        |
        | 3. Menghapus Daftar                        |
        | 4. Keluar                                  |
        ==============================================
        """)
        menu=int(input("\n(Silahkan pilih opsi 1-4): "))

#READ DATA
        if menu == 1:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            for i, (genre, daftar) in enumerate(drama_korea.items(), start=1):
                print(f"{i}. {genre} : ", end="")
                for j in range(len(daftar)):
                    print(daftar[j], end=", " if j < len(daftar) - 1 else "")
                print()
            input("\nTekan ENTER untuk kembali ke menu...")
            os.system(clear_cmd)

#UPDATE DATA
        elif menu == 2:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            daftar_genre = list(drama_korea.keys())
            for i, genre in enumerate(daftar_genre, start=1):
                print(f"{i}. {genre} : ", end="")
                daftar = drama_korea[genre]
                for j in range(len(daftar)):
                    print(daftar[j], end=", " if j < len(daftar) - 1 else "")
                print()
            nomor = int(input("\nSilahkan pilih genre yang ingin diubah (1-5): "))
            if 1 <= nomor <= 5:
                genre = daftar_genre[nomor - 1]
                daftar = drama_korea[genre]
                index = int(input("Masukkan index judul yang ingin diubah (0-2): "))
                if 0 <= index < len(daftar):
                    judul_baru = input("Silahkan masukkan judul baru: ")
                    daftar[index] = judul_baru
                    print("\nData berhasil diubah!")
            else:
                print("\nNomor genre tidak valid!")
            input("\nTekan ENTER untuk melanjutkan...")
            os.system(clear_cmd)

#DELETE DATA
        elif menu == 3:
            print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====")
            print()
            daftar_genre = list(drama_korea.keys())
            for i, genre in enumerate(daftar_genre, start=1):
                print(f"{i}. {genre} : ", end="")
                daftar = drama_korea[genre]
                for j in range(len(daftar)):
                    print(f"{daftar[j]}", end=", " if j < len(daftar) - 1 else "")
                print()
            nomor = int(input("\nSilahkan pilih genre yang judulnya ingin dihapus (1-5): "))
            if 1 <= nomor <= 5:
                genre = daftar_genre[nomor - 1]
                daftar = drama_korea[genre]
                index = int(input(f"Silahkan masukkan index yang ingin dihapus (0-2): "))
                0 <= index < len(daftar)
                hapus = daftar.pop(index)
                print()
                print(drama_korea[genre])
                print("\nData berhasil dihapus!")
            else:
                print("\nNomor genre tidak valid!")
            input("\nTekan ENTER untuk melanjutkan...")
            os.system(clear_cmd)

#KELUAR
        elif menu==4:
                input("\nTekan ENTER untuk keluar server!..."); os.system(clear_cmd)
                break
        else:
            print("\nError! Pilihan tidak valid!")
            input("\nTekan ENTER untuk kembali ke menu..."); os.system(clear_cmd)