from prettytable import PrettyTable
from storage import drama_korea

from prettytable import PrettyTable

def tampilkan_drama(drama_data):
    table = PrettyTable()
    table.field_names = ["No", "Genre", "Judul Drama"]
    no = 1
    for genre, daftar in drama_data.items():
        for judul in daftar:
            table.add_row([no, genre, judul])
            no += 1
    print("\n===== DAFTAR TOP DRAMA KOREA =====\n")
    print(table)


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
