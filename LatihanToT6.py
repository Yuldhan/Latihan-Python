print ("\nINI ADALAH PROGRAM UNTUK MENGHITUNG UKURAN BAJU")
print ("="*48)
# Masukkan pengukuran tubuh pengguna
tinggi_badan = float(input("\nMasukkan tinggi badan (cm): "))
berat_badan = float(input("Masukkan berat badan (kg): "))
lingkar_dada = float(input("Masukkan lingkar dada (cm): "))
lingkar_pinggang = float(input("Masukkan lingkar pinggang (cm): "))
lingkar_pinggul = float(input("Masukkan lingkar pinggul (cm): "))

# Periksa ukuran baju berdasarkan pengukuran tubuh
ukuran_baju = ""

if tinggi_badan < 160:
    if berat_badan < 50:
        ukuran_baju = "S"
    elif berat_badan < 65:
        ukuran_baju = "M"
    else:
        ukuran_baju = "L"
elif tinggi_badan < 175:
    if lingkar_dada < 90:
        ukuran_baju = "S"
    elif lingkar_dada < 100:
        ukuran_baju = "M"
    else:
        ukuran_baju = "L"
else:
    if lingkar_pinggang < 80 and lingkar_pinggul < 100:
        ukuran_baju = "S"
    elif lingkar_pinggang < 90 and lingkar_pinggul < 110:
        ukuran_baju = "M"
    else:
        ukuran_baju = "L"

print ("="*48)
# Tampilkan ukuran baju yang sesuai
print("\nUkuran baju yang sesuai untuk Anda adalah:", ukuran_baju)