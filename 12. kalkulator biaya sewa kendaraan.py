import locale
locale.setlocale(locale.LC_ALL, 'id_ID')

tipe = input("pilih tipe kendaraan (1/2/3/4): ")

if tipe > "0" and tipe <= "4":
    if tipe == "1":
        kendaraan = "motor"
        tarif = 75000
        diskon = 5 / 100 
    elif tipe == "2":
        kendaraan = "mobil"
        tarif = 250000
        diskon = 10 / 100 
    elif tipe == "3":
        kendaraan = "minibus"
        tarif = 400000
        diskon = 12 / 100 
    elif tipe == "4":
        kendaraan = "bus"
        tarif = 800000
        diskon = 15 / 100 
else:
    print (f"tipe kendaraan tidak valid! masukkan angka 1 sampai 4")
    exit()
sewa = int(input("lama sewa kendaraan? "))
if sewa <= 0 or sewa > 30:
    print (f"pesan input tidak valid")
    exit()
elif sewa <= 7:
    print (f"tidak mendapat diskon")
    diskon = 0

biayasewa = sewa * tarif
diskon = diskon * biayasewa
total = biayasewa - diskon

print (f"=== RINCIAN BIAYA SEWA ===")
print (f"kendaraan          :{kendaraan}")
print (f"tarif per hari     :Rp{tarif:n}")
print (f"lama sewa          :{sewa} hari")
print (f"biaya sewa         :Rp{biayasewa:n}")
print (f"diskon             :Rp{diskon:n}")
print (f"total bayar        :Rp{int(total):n}")