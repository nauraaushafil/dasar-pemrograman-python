jenis = (input("mau beli sepatu jenis apa? (sport, sekolah, dan boots) "))
if jenis == "sport":
    sepatu = 350000
elif jenis == "sekolah":
    sepatu = 250000
elif jenis == "boots":
    sepatu = 500000

jumlah = int(input("mau beli sepatu berapa sepatu? "))
if jumlah >= 5:
    diskon = (sepatu * jumlah) * 15/100
elif jumlah >= 3:
    diskon = (sepatu * jumlah) * 10/100
print (f"jadi diskon kamu adalah {diskon}")

member = (input("apakah punya kartu member? "))
if member == "punya":
    diskon1 = diskon * (5 / 100)
    diskon = diskon + diskon1
elif member == "tidak punya":
 total = (sepatu * jumlah) - diskon
if total > 1000000:
    print ("selamat anda mendapatkan kaos kaki gratis")
print(f"diskon kamu saat ini adalah {diskon}, jadi total belanja kamu adalah = {total}")


