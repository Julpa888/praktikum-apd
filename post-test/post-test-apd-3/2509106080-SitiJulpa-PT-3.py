biayaLangganan=1500000
nama=(str(input("Silahkan masukkan nama pengguna: ")))
NIM=(int(input("Silahkan masukkan NIM pengguna: ")))

print()

if nama=="Siti Julpa" and NIM==2509106080:
    print("Selamat anda berhasil login!")
    
    opsiPaket=(str(input("Silahkan pilih paket langganan aplikasi streaming musik yang ingin anda beli: ")))
    if opsiPaket=="Paket Bronze":
        totalBayar=(int(biayaLangganan+(biayaLangganan*1/100)))
        print(f"[Total yang harus dibayar adalah Rp {totalBayar}]")
        print("[Dengan keuntungan yang didapat yaitu akses dasar ke lagu-lagu populer]")
    elif opsiPaket=="Paket Silver":
        totalBayar=(int(biayaLangganan+(biayaLangganan*3/100)))
        print(f"[Total yang harus dibayar adalah Rp {totalBayar}]")
        print("[Dengan keuntungan yang didapat yaitu akses lagu premium dan playlist kustom]")
    elif opsiPaket=="Paket Gold":
        totalBayar=(int(biayaLangganan+(biayaLangganan*5/100)))
        print(f"[Total yang harus dibayar adalah Rp {totalBayar}]")
        print("[Dengan keuntungan yang didapat yaitu akses lagu premium, playlist kustom, dan mode offline]")
    else: 
        totalBayar=(int(biayaLangganan+(biayaLangganan*7/100)))
        print(f"[Total yang harus dibayar adalah Rp {totalBayar}]")
        print("[Dengan keuntungan yang didapat yaitu akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis]")

# error kalau hanya salah satu yang salah
elif nama=="Siti Julpa" or NIM==2509106080:
    print("Error: Nama atau NIM salah!")
# error kalau keduanya salah
else:
    print("Error: Akun tidak tersedia!")

print()