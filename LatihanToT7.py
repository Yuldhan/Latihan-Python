print("\n=========== Menghitung Kebutuhan Kalori ============")
tb = float(input("\nMasukkan Tinggi Badan (cm): "))
bb = float(input("Masukkan Berat badan (kg) : "))
usia = float(input("Masukkan Usia (Tahun)     : "))

bmr = 66.5+(13.7*bb)+(5*tb)-(6.8*usia)
print ("="*52)
print("nilai BMR (Basal Metabolic Rate) kamu adalah ",round (bmr,2))
print("="*52)
print("Pilihan Menu! (1/2/3)")
print("1. Aktivitas Ringan")
print("2. Aktivitas Sedang")
print("3. Aktivitas Tinggi")

aktiv = int(input("\nPilih Salah Satu! (1/2/3) : " ))
print ("="*52)
if aktiv == 1:
    print ("Kebutuhan Kalori Kamu = ",round (bmr*1.2,2), "kkal")
elif aktiv == 2:
    print ("Kebutuhan Kalori Kamu = ",round (bmr*1.3,2), "kkal")
elif aktiv == 3:
    print ("Kebutuhan Kalori Kamu = ",round (bmr*1.4,2), "kkal")
else:
    print("Pilihan tidak tersedia")
print ("="*52)

