nama="Siti Julpa"
NIM=2509106080

print("Selamat datang di program Pembelian Tiket Bioskop XX0")
print()

print("Silahkan login terlebih dahulu:")
for i in range(3):
    username=(str(input("Masukkan username: ")))
    password=(int(input("Masukkan password: ")))
    if username==nama and password==NIM:
        print()
        print("Selamat anda berhasil login!")
        break
    elif username==nama or password==NIM:
        print("Error: Format akun salah!")
    else:
        print("Error: Gagal login!")
else:
    print("Percobaan login telah habis!")
    exit()


while True:
    print()
    print("=============== OPSI PEMBAYARAN =================")
    print("1. Tiket Reguler dengan Harga per tiket Rp 50.000")
    print("2. Tiket VIP dengan Harga per tiket Rp 100.000")
    print("3. Tiket VVIP dengan Harga per tiket Rp 150.000")
    print("4. Keluar dari program")
    print(50*"=")
    print()
    opsi=int(input("Silahkan pilih opsi pembayaran: "))
    if opsi==1 or opsi==2 or opsi==3:
        jumlah=int(input("Silahkan masukkan jumlah tiket yang ingin dibeli: "))
        if opsi==1:
            jenis="Reguler"
            harga=50000
        elif opsi==2:
            jenis="VIP"
            harga=100000
        else:
            jenis="VVIP"
            harga=150000
        
        total=0
        totalBayar=0
        for i in range(jumlah):
            total+=harga
            totalBayar=total
        
        diskon=0
        print()
        if totalBayar>=300000:
            diskon=totalBayar*12/100
            bonus="Mendapat potongan harga 12%"
        elif totalBayar>=200000:
            diskon=totalBayar*8/100
            bonus="Mendapat potongan harga 8%"
        elif totalBayar>=150000:
            bonus="Mendapat poster film eksklusif!"
        else:
            bonus="Tidak mendapat bonus"
        
        totalAkhir=totalBayar
        totalAkhir=totalBayar-diskon
        print()
        print("====================== STRUK PEMBELIAN ======================")
        print(f"Jenis tiket                         : {jenis}")
        print(f"Jumlah tiket                        : {jumlah}")
        print(f"Benefit yang didapat                : {bonus}")
        print(f"Total yang harus anda bayar sebesar : Rp {int(totalAkhir)}")
        print()
        print("Terima kasih atas pembelian anda!")
        print(60*"=")
        print()
    else:
        break
