def segiempat(panjang,lebar):
    "Fungsi Menghitung Segiempat"
    luas_segiempat = panjang*lebar
    print("Panjang Segiempat : ",panjang)
    print("Lebar Segiempat : ",lebar)
    print("Luas Segiempat : ",luas_segiempat)

def segitiga(alas,tinggi):
    "Fungsi Menghitung Segitiga"
    luas_segitiga = (alas*tinggi)/2
    print("Alas Segitiga = ",alas)
    print("Tinggi Segitiga = ",tinggi)
    print("Luas Segitiga = ",luas_segitiga)

print("Perhitungan 2 Dimensi")
print("1. Segi Empat")
print("2. SegiTiga")

pilihan = input("Masukkan Pilihan Anda : ")
if pilihan == "1" :
    panjang = int(input("Masukkan panjang segiempat : "))
    lebar = int(input("Masukkan lebar segiempat : "))
    segiempat(panjang,lebar)

elif pilihan == "2" :
    alas = int(input("Masukkan Alas Segitiga : "))
    tinggi = int(input("Masukkan tinggi segitiga : "))
    segitiga(alas,tinggi)
else :
    exit
