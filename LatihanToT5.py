tb = int(input("Masukkan tinggi Badan Kamu : "))
bb = int(input("Masukkan Berat Badan Kamu : "))

#kalkulasi berat badan dan tinggi badan
kalkulasi = tb+bb-100

if kalkulasi == kalkulasi-100:
    print("berat badan kamu IDEAL")
elif kalkulasi >= kalkulasi-100:
    print("berat badan kamu berlebih")
elif kalkulasi <= kalkulasi-100:
    print("berat badan kurang")
else:
    print("obesitas")