# Buat kamus (dictionary) untuk menyimpan data siswa
data_siswa = {}

# Fungsi untuk menambahkan data siswa
def tambah_siswa(nama, nilai):
    data_siswa[nama] = nilai
    print("Data siswa", nama, "telah ditambahkan.")

# Fungsi untuk menampilkan data semua siswa
def tampilkan_data_siswa():
    if len(data_siswa) == 0:
        print("Tidak ada data siswa yang tersedia.")
    else:
        print("Data Siswa:")
        for nama, nilai in data_siswa.items():
            print("Nama:", nama, "Nilai:", nilai)

# Fungsi untuk menghitung rata-rata nilai
def hitung_rata_rata():
    if len(data_siswa) == 0:
        print("Tidak ada data siswa yang tersedia.")
    else:
        total_nilai = sum(data_siswa.values())
        rata_rata = total_nilai / len(data_siswa)
        print("Rata-rata Nilai Siswa:", rata_rata)

# Fungsi utama
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Hitung Rata-rata Nilai")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            nilai = float(input("Masukkan nilai siswa: "))
            tambah_siswa(nama, nilai)
        elif pilihan == "2":
            tampilkan_data_siswa()
        elif pilihan == "3":
            hitung_rata_rata()
        elif pilihan == "4":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()