print("1. Segiempat")
print("2. Segitiga")
print("3. Persegi")
print("4. Lingkaran")

pilihan = input("Masukkan Pilihanmu : ")
if pilihan == "1" :
    panjang = input("Masukkan panjang Segiempat : ")
    lebar = input("Masukkan Lebar Segiempat: ")
    luas_segiempat = int(panjang) * int(lebar)
    print("Panjang Segiempat = ",panjang)
    print("Lebar Segiempat = ",lebar)
    print("Luas Segiempat = ",luas_segiempat)


elif pilihan == "2" :
    alas = input("Masukkan Alas Segitiga: ")
    tinggi = input("Masukkan Tinggi Segitiga : ")
    sisi = input("Masukkan Sisi Segitiga : ")
    luas_segitiga = int(alas) * int(tinggi)/2
    keliling_segitiga = 3*int(sisi)
    print("Alas Segitiga = ",alas)
    print("Tinggi Segitiga = ",tinggi)
    print("Luas Tinggi Segitiga = ",luas_segitiga)
    print("Keliling Segitiga = ", keliling_segitiga)


elif pilihan == "3" :
    sisipersegi = input("Masukkan Sisi Persegi : ")
    luas_persegi = int(sisi) * int(sisi)
    print("Sisi Persegi = ",sisipersegi)
    print("Luas Persegi = ",luas_persegi)

elif pilihan == "4" :
    jarijari = input("Masukkan Jari-jari Lingkarang : ")
    phi = 22/7 
    luas_lingkaran = phi * int(jarijari) * int(jarijari)
    print("Jari-jari Lingkaran = ",jarijari)
    print("Luas Lingkaran = ",luas_lingkaran)

else :
    print("TIDAK ADA DI MENU")


