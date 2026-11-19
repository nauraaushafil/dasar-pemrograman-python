import locale
locale.setlocale(locale.LC_ALL, 'id_ID')

tipe = input("pilih kategori (1/2/3/4): ")
if tipe > "0" and tipe <= "4":
    if tipe == "1":
        jenispelanggan = (f"rumah tangga")
        tarif = 3500
        biayaadmin = 10000
    elif tipe == "2":
        jenispelanggan = (f"usaha kecil")
        tarif = 5000
        biayaadmin = 15000
    elif tipe == "3":
        jenispelanggan = (f"industri")
        tarif = 7500
        biayaadmin = 25000
    elif tipe == "4":
        jenispelanggan = (f"hotel")
        tarif = 9000
        biayaadmin = 40000
else:
    print(f"kategori tidak valid! masukkan angka 1 sampai 4")
    exit()

jumlah = int(input("jumlah pemakaian air (m³): "))
if jumlah <= 0:
    print("error: pemakaian harus lebih dari 0 m3")
    exit()
biayapemakaian = jumlah * tarif
ppn = 5 / 100 * biayapemakaian
total = biayapemakaian + biayaadmin + ppn
print (f"=== RINCIAN TAGIHAN AIR ===")
print (f"Kategori           :{jenispelanggan}")
print (f"Tarif              :Rp{tarif:n}/m³")
print (f"Pemakaia           :{jumlah} m³")
print (f"Biaya pemakaian    :Rp{biayapemakaian:n}")
print (f"Administrasi       :Rp{biayaadmin:n}")
print (f"PPN (5%)           :Rp{ppn:n}")
print (f"Total tagihan      :Rp{total:n}")