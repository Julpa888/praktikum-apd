# ini input nama, nim dan harga
nama=(input("Silahkan masukkan nama lengkap anda: ")) 
nim=(input("Silahkan masukkan NIM anda: "))
harga=(int(input("Silahkan masukkan harga makanan nya: Rp ")))

# rumus total harga disini bang/mba
pecel=(int(harga+(harga*5/100)))
mie=(int(harga+(harga*8/100)))
naspad=(int(harga+(harga*10/100)))

print()

print(f"Seorang mahasiswa dengan nama {nama} dan NIM {nim} ingin membeli makanan seharga Rp {harga}")
print()

# output makanan setelah pajak
print(85*"=")
print(f"< Jika {nama} ingin membeli Pecel Lele, maka dia harus membayar sebanyak Rp {pecel} >")
print(85*"-")
print(f"< Jika {nama} ingin membeli Mie Ayam, maka dia harus membayar sebanyak Rp {mie} >")
print(85*"-")
print(f"< Jika {nama} ingin membeli Nasi Padang, maka dia harus membayar sebanyak Rp {naspad} >")
print(85*"=")

print()