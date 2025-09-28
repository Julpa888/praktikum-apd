harga = int(input("Masukkan harga belanjaan:"))

if harga>10000:
    print("Anda mendapatkan diskon 20%")
elif harga>50000:
    print("Anda mendapatkan diskon 10%")
else:
    print("Anda tidak mendapat diskon")