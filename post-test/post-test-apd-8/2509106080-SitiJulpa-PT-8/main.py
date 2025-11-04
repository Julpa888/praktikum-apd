from menu import menu_awal, menu_admin, menu_member, cls, clear, ungu, Style
import autentikasi
from create import membuat_daftar
from read import tampilkan_drama
from update import mengganti_daftar
from delete import menghapus_daftar
from storage import drama_korea
import sys

opsi = menu_awal()
if opsi == "LOGIN":
    autentikasi.login()
elif opsi == "REGISTRASI":
    autentikasi.registrasi()
    autentikasi.login()


if autentikasi.is_admin:
    while True:
        menu = menu_admin()
        if menu == "Menampilkan Daftar":
            tampilkan_drama(drama_korea); clear()
        elif menu == "Membuat Daftar":
            tampilkan_drama(drama_korea)
            membuat_daftar(int(input("\nPilih genre (1-5): "))); clear()
        elif menu == "Mengganti Daftar":
            tampilkan_drama(drama_korea)
            mengganti_daftar(int(input("\nPilih genre (1-5): "))); clear()
        elif menu == "Menghapus Daftar":
            tampilkan_drama(drama_korea)
            menghapus_daftar(int(input("\nPilih genre (1-5): "))); clear()
        elif menu == "Keluar":
            sys.exit()

else:
    while True:
        menu = menu_member()
        if menu == "Menampilkan Daftar":
            tampilkan_drama(drama_korea); clear()
        elif menu == "Mengganti Daftar":
            tampilkan_drama(drama_korea)
            mengganti_daftar(int(input("\nPilih genre (1-5): "))); clear()
        elif menu == "Menghapus Daftar":
            tampilkan_drama(drama_korea)
            menghapus_daftar(int(input("\nPilih genre (1-5): "))); clear()
        elif menu == "Keluar":
            sys.exit()
