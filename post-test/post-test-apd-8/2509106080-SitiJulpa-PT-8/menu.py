from colorama import Fore, Style
import inquirer
import os

ungu = Fore.MAGENTA

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def clear():
    input("\nTekan ENTER untuk kembali ke menu..."); cls()

def menu_awal():
    print(f"{ungu}"
        "\n======================================================================\n"
        "|      SELAMAT DATANG DI BLOG DAFTAR DRAMA KOREA FAVORIT DUNIA!      |\n"
        "======================================================================\n"
        f"{Style.RESET_ALL}"
    )
    pertanyaan = [
        inquirer.List(
            "menu",
            message=f"{ungu}HALAMAN MENU!{Style.RESET_ALL}",
            choices=["LOGIN", "REGISTRASI", "KELUAR"]
        )
    ]
    opsi = inquirer.prompt(pertanyaan)["menu"]
    return opsi

def menu_admin():
    print(f"{ungu}\n----- DAFTAR DRAMA KOREA FAVORIT DUNIA -----\n{Style.RESET_ALL}")
    pertanyaan = [
        inquirer.List(
            "menu",
            message=f"{ungu}SILAHKAN PILIH MENU!{Style.RESET_ALL}",
            choices=["Menampilkan Daftar","Membuat Daftar","Mengganti Daftar","Menghapus Daftar","Keluar"]
        )
    ]
    menu = inquirer.prompt(pertanyaan)["menu"]
    return menu

def menu_member():
    print(f"{ungu}\n----- DAFTAR DRAMA KOREA FAVORIT DUNIA -----\n{Style.RESET_ALL}")
    pertanyaan = [
        inquirer.List(
            "menu",
            message=f"{ungu}SILAHKAN PILIH MENU!{Style.RESET_ALL}",
            choices=["Menampilkan Daftar","Mengganti Daftar","Menghapus Daftar","Keluar"]
        )
    ]
    menu = inquirer.prompt(pertanyaan)["menu"]
    return menu
