import pwinput
from menu import clear
from storage import akun_admin, akun_member

is_admin = None

def registrasi():
        global is_admin, akun_admin, akun_member
        print("===== SILAHKAN REGISTRASI MEMBER! =====")
        while True:
            usn_baru = input("\nPilih username anda: ")
            pw_baru = pwinput.pwinput("Masukkan password: ")
            if usn_baru in akun_member or usn_baru in akun_admin:
                print("Username telah dipakai, silahkan pilih yang lain!"); clear()
                continue
            else:
                akun_member[usn_baru] = pw_baru
                print("\n--- Registrasi member berhasil, selamat bergabung di komunitas! ---"); clear()
                break


def login():
        global is_admin, akun_admin, akun_member
        print("===== SILAHKAN LOGIN =====")
        while True:
                usn_login = input("\nSilahkan masukkan username: ")
                pw_login = pwinput.pwinput("Silahkan masukkan password: ")
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
