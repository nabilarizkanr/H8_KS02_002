def segiempat():
    "Fungsi Menghitung Segiempat"
    panjang = int(input("Masukkan panjang segiempat : "))
    lebar = int(input("Masukkan lebar segiempat : "))
    luas_segiempat = panjang*lebar
    print("Panjang Segiempat : ",panjang)
    print("Lebar Segiempat : ",lebar)
    print("Luas Segiempat : ",luas_segiempat)

def segitiga():
    "Fungsi Menghitung Segitiga"
    alas = int(input("Masukkan Alas Segitiga : "))
    tinggi = int(input("Masukkan tinggi segitiga : "))
    luas_segitiga = (alas*tinggi)/2
    print("Alas Segitiga = ",alas)
    print("Tinggi Segitiga = ",tinggi)
    print("Luas Segitiga = ",luas_segitiga)

def persegi() :
    "Fungsi Persegi"
    sisi = int(input("Masukan sisi persegi : "))
    luas_persegi = sisi * sisi
    print("Sisi Persegi = ",sisi)
    print("Luas Persegi = ",luas_persegi)

def lingkaran() :
    "Fungsi Lingkaran"
    phi = 22/7
    jari_jari = int(input("Masukkan Jari-Jari Lingkaran : "))
    luas_lingkaran = phi * jari_jari * jari_jari
    print("Phi = ",phi)
    print("Jari-jari lingkaran = ",jari_jari)
    print("Luas Lingkaran = ",luas_lingkaran)