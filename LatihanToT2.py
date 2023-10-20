print("\n================ Menghitung Lingkaran =================")
print("Program ini merupakan Perhitungan Bangun Datar Lingkaran")
r = int(input("\nMasukan nilai jari-jari : "))
phi = 3.14
luas = phi*r*r
kel = 2*phi*r
d = r*2

print("\nPilihan Menu! (1/2/3)")
print("1. Luas Lingkaran")
print("2. Keliling Lingkaran")
print("3. Nilai Diameter")

hitung = int(input("\nPilih Salah Satu! (1/2/3) : " ))

if hitung == 1:
    print("Nilai Luas Lingkaran : ",luas)
    print("Rumusnya adalah phi x r^2")
elif hitung == 2:
    print("Nilai Keliling Lingkaran : ",kel)
    print("Rumusnya adalah 2 x phi x r")
elif hitung == 3:
    print("Nilai Diameternya adalah : ",d)
    print("Rumusnya adalah 2 x r")

else:
    print("Pilihan Salah")

if luas >= 350:
    print("\nLingkaran terlalu besar")
else:
    print("\nLingkaran sesuai")