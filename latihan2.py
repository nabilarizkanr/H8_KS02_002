import bentuk3D

print("Perhitungan 3 Dimensi")
print("1. Kubus")
print("2. Balok")
print("3. Tabung")

ulang = "Y"
while ulang == "Y" or ulang == "y" :
    pilihan = input("Masukkan Pilihan Anda : ")

    if pilihan == '1' :
        bentuk3D.kubus()
    
    elif pilihan == '2' :
        bentuk3D.balok()
    
    elif pilihan == '3' :
        bentuk3D.tabung()

    else :
        print("Tidak Ada di Pilihan")

    ulang = input("Apakah Anda ingin mengulang? ")

else :
    print("Program Selesai")
    exit