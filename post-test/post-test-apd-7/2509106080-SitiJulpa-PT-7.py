import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")
def clear():
    input("\nTekan ENTER untuk kembali ke menu..."); cls()

is_admin = {}
hapus = {}

#USERNAME DAN PASSWORD TERDAFTAR
akun_admin = {
    "Julpa": "Pentol",
    "Triya": "Aslab",
    "Pernan": "123",
    "Nabil": "2025"
}
akun_member = {
    "Shasha": "Teman",
    "Aya": "Teman1",
    "Mariska": "Teman2",
    "Nisa": "1010",
    "Intan": "2345"
}

#DICTIONARY DRAMA KOREA DENGAN RATING DI ATAS 9.0
drama_korea = {
    "ROMANCE": ["Crash Landing on You", "Goblin", "Strong Woman Do Bong Soon"],
    "CRIME": ["Vincenzo", "Vagabond", "Taxi Driver"],
    "HISTORICAL": ["Alchemy of Souls", "Mr. Queen", "Hwarang"],
    "SCI-FI": ["Sweet Home", "All of Us Are Dead", "Duty After School"],
    "YOUTH": ["Weak Hero Class", "Study Group", "Twinkling Watermelon"]
}



def menu_awal():
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

#MENU REGISTRASI & LOGIN
def registrasi_login():
        global is_admin, akun_admin, akun_member
        clear()
        print("===== SILAHKAN REGISTRASI MEMBER! =====")
        while True:
            usn_baru = input("\nPilih username anda: ")
            pw_baru = input("Masukkan password: ")
            if usn_baru in akun_member or usn_baru in akun_admin:
                print("Username telah dipakai, silahkan pilih yang lain!"); clear()
                continue
            else:
                print("\n--- Registrasi member berhasil, selamat bergabung di komunitas! ---"); clear()

                print("===== SILAHKAN LOGIN =====")
                while True:
                        usn_login = input("\nSilahkan masukkan username: ")
                        pw_login = input("Silahkan masukkan password: ")
                        if usn_login != usn_baru or pw_login != pw_baru:
                            print("\nFormat salah, login gagal!"); clear()
                        else:
                            is_admin = False
                            print("\n--- Login berhasil, selamat datang member! ---"); clear()
                            return


#MENU LOGIN TANPA REGISTRASI
def login_tanpa_regis():
        global is_admin, akun_admin, akun_member
        clear()
        print("===== SILAHKAN LOGIN =====")
        while True:
                usn_login = input("\nSilahkan masukkan username: ")
                pw_login = input("Silahkan masukkan password: ")
                if usn_login in akun_admin and akun_admin[usn_login] == pw_login:
                    is_admin = True
                    print("\n--- Login berhasil, selamat datang admin! ---"); clear()
                    break
                elif usn_login in akun_member and akun_member[usn_login] == pw_login:
                    is_admin = False
                    print("\n--- Login berhasil, selamat datang member! ---"); clear()
                    break
                else:
                    print("\nFormat salah, login gagal!"); clear()




#FUNGSI MENU ADMIN
def menu_admin():
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

#FUNGSI MENU MEMBER
def menu_member():
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

#FUNGSI READ
def tampilkan_drama(drama_data):
    print("\n===== DAFTAR TOP DRAMA KOREA DARI BERBAGAI GENRE =====\n")
    for i, (genre, daftar) in enumerate(drama_data.items(), start=1):
        print(f"{i}. {genre} : ", end="")
        for j in range(len(daftar)):
            print(daftar[j], end=", " if j < len(daftar) - 1 else "")
        print()

#FUNGSI CREATE
def membuat_daftar(genre_nomor):
        global drama_korea
        daftar_genre = list(drama_korea.keys())
        try:
            nomor = genre_nomor
            if nomor < 1 or nomor > len(daftar_genre):
                raise KeyError 
            genre = daftar_genre[nomor - 1]
            judul_baru = input("Masukkan judul yang ingin ditambah: ")
            drama_korea[genre].append(judul_baru)
            print("\nData berhasil ditambah!\n")
            drama_per_genre(genre)
        except KeyError:
            print("\nGenre tidak valid! Pilih nomor genre yang tersedia.")

#FUNGSI UPDATE
def mengganti_daftar(genre_nomor): 
            global drama_korea
            daftar_genre = list(drama_korea.keys())
            try:
                nomor = genre_nomor
                if nomor < 1 or nomor > len(daftar_genre):
                    raise KeyError
                genre = daftar_genre[nomor - 1]
                daftar = drama_korea[genre]
                index = int(input(f"Masukkan index judul yang ingin diubah (0-{len(daftar)-1}): "))
                if index < 0 or index >= len(daftar):
                    raise IndexError
                judul_baru = input("Silahkan masukkan judul baru: ")
                daftar[index] = judul_baru
                print("\nData berhasil diubah!\n")
                drama_per_genre(genre)
            except KeyError:
                print("\nGenre tidak valid!")
            except IndexError:
                print("\nIndex tidak valid!")

#FUNGSI DELETE
def menghapus_daftar(genre_nomor):
                global hapus, drama_korea
                daftar_genre = list(drama_korea.keys())
                try:
                    nomor = genre_nomor
                    if nomor < 1 or nomor > len(daftar_genre):
                        raise KeyError
                    genre = daftar_genre[nomor - 1]
                    daftar = drama_korea[genre]
                    index = int(input(f"Silahkan masukkan index yang ingin dihapus (0-{len(daftar)-1}): "))
                    if index < 0 or index >= len(daftar):
                        raise IndexError
                    hapus = daftar.pop(index)
                    print("\nData berhasil dihapus!\n")
                    drama_per_genre(genre)
                except KeyError:
                    print("\nGenre tidak valid!")
                except IndexError:
                    print("\nIndex tidak valid!")

#FUNGSI REKURSIF UNTUK MENAMPILKAN GENRE + JUDUL DI CRUD
def tampilkan_judul(daftar, index=0):
    if index == len(daftar):
        return ""
    if index == len(daftar) - 1:
        return daftar[index]
    else:
        return daftar[index] + ", " + tampilkan_judul(daftar, index + 1)

def drama_per_genre(genre):
    daftar = drama_korea[genre]
    hasil = tampilkan_judul(daftar)
    print(f"{genre}: {hasil}")



### PROGRAM UTAMA ###
while True:
    menu_awal()
    try:
        opsi = int(input("\nSilahkan pilih opsi (1/2): ")) 
    except ValueError:
        print("Input yang anda masukkan bukan angka"); clear()
        continue

    if opsi == 1:
        login_tanpa_regis()
    elif opsi == 2:
        registrasi_login()
    else:
        print("Pilihan tidak valid."); clear()
        continue
    break

if is_admin == True:
    while True:
        menu_admin()
        try:
            menu = int(input("\n(Silahkan pilih opsi 1-5): "))
            if menu == 1:
                tampilkan_drama(drama_korea); clear()
            elif menu == 2:
                tampilkan_drama(drama_korea)
                membuat_daftar(int(input("\nPilih genre (1-5): "))); clear()
            elif menu == 3:
                tampilkan_drama(drama_korea)
                mengganti_daftar(int(input("\nPilih genre (1-5): "))); clear()
            elif menu == 4:
                tampilkan_drama(drama_korea)
                menghapus_daftar(int(input("\nPilih genre (1-5): "))); clear()
            elif menu == 5:
                break
            else:
                print("\nError! Pilihan tidak valid!")
        except ValueError:
            print("Yang anda masukkan bukan angka")

if is_admin == False:
    while True:
        menu_member()
        try:
            menu = int(input("\n(Silahkan pilih opsi 1-4): "))
            if menu == 1:
                tampilkan_drama(drama_korea); clear()
            elif menu == 2:
                tampilkan_drama(drama_korea)
                mengganti_daftar(int(input("\nPilih genre (1-5): "))); clear()
            elif menu == 3:
                tampilkan_drama(drama_korea)
                menghapus_daftar(int(input("\nPilih genre (1-5): "))); clear()
            elif menu == 4:
                break
            else:
                print("\nError! Pilihan tidak valid!")
        except ValueError:
            print("Yang anda masukkan bukan angka")
