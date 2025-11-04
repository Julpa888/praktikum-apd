from storage import drama_korea
from read import drama_per_genre

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
