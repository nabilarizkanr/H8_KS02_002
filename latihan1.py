import bentuk2D

print("Perhitungan 2 Dimensi")
print("1. Segiempat")
print("2. Segitiga")
print("3. Persegi")
print("4. Lingkaran")

ulang = "Y"
while ulang == "Y" or ulang == "y" :
    pilihan = input("Masukkan Pilihan Anda : ")

    if pilihan == '1' :
        bentuk2D.segiempat()

    elif pilihan == '2' :
        bentuk2D.segitiga()

    elif pilihan == '3' :
        bentuk2D.persegi()

    elif pilihan == '4' :
        bentuk2D.lingkaran()
        
    else :
        print("Tidak ada di Pilihan")

    ulang = input("Apakah Anda ingin mengulang? ")

else :
    print("Program Selesai")
    exit