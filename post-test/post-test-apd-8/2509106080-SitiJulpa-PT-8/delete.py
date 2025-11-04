from storage import drama_korea
from read import drama_per_genre

hapus = {}

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
