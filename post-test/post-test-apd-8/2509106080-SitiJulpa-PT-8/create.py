from storage import drama_korea
from read import drama_per_genre

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
