
def kubus() :
    s = int(input("Masukkan Sisi Kubus = "))
    volume_kubus = s * s * s
    luas_permukaan_kubus = 6 * (s *s)
    keliling_kubus = 12 * s
    luas_sisi = s * s
    print("Volume Kubus = ",volume_kubus)
    print("Luas Permukaan Kubus = ",luas_permukaan_kubus)
    print("Keliling Kubus = ",keliling_kubus)
    print("Luas salah satu sisi Kubus = ",luas_sisi)

def balok() :
    p = int(input("Masukkan Panjang Balok = "))
    l = int(input("Masukkan Lebar Balok = "))
    t = int(input("Masukkan Tinggi Balok = "))
    volume_balok = p *l * t
    luas_permukaan_balok = 2*(p*l + l*t + p*t)
    #diagonal_ruang = math.sqrt(p* p + l * l + t * t )
    keliling_balok = 4 * (p + l + t)
    print("Volume Balok = ",volume_balok)
    print("Luas Permukaan Balok = ",luas_permukaan_balok)
    print("Keliling Balok = ",keliling_balok)
    
def tabung():
    phi = 22/7
    r = int(input("Masukkan jari-jari tabung = "))
    h = int(input("Masukkan Tinggi Tabung = "))
    luas_permukaan_tabung = 2 * phi * r * r + 2 * phi * r * h
    volume_tabung = phi * r * r * h
    print("Luas Permukaan Tabung = ",luas_permukaan_tabung)
    print("Volume Tabung = ",volume_tabung)