rute = input("mau ambil rute apa? (bali, singapore, tokyo) ")
kelas = input("ambil kelas apa? (economy, business, first class) ")
usia = int (input("usia berapa? "))
bagasi = int (input("mau tambahan bagasi berapa kg? "))
member = input ("punya member? ")

if rute == "bali":
    bali = 1000000
    if kelas ==  "economy":
        harga = bali
    elif kelas == "business":
        harga = bali + (bali * 0.5)
    elif kelas == "first class":
        harga = bali + (bali * 1)

elif rute == "singapore":
    singapore = 1500000
    if kelas ==  "economy":
        harga = singapore
    elif kelas == "business":
        harga = singapore + (singapore * 0.5)
    elif kelas == "first class":
        harga = singapore + (singapore * 1)

elif rute == "tokyo":
    tokyo = 5000000
    if kelas ==  "economy":
        harga = tokyo
    elif kelas == "business":
        harga = tokyo + (tokyo * 0.5)
    elif kelas == "first class":
        harga = tokyo + (tokyo * 1)

if usia <= 2:
    diskonusia = harga * 0.8
elif usia <= 12:
    diskonusia = harga * 0.2
elif usia > 60:
    diskonusia = harga * 15/100
else:
   (harga)

if bagasi > 20:
    bagasi = (bagasi - 20) * 100000

if member == "punya" and diskonusia > 2000000:
    diskonmember = diskonusia - 150000
else:
    diskonmember = 0

totaldiskon = diskonusia + diskonmember
totalsemua = harga - totaldiskon + bagasi


print (f"rute = {rute}")
print (f"kelas = {kelas}")
print (f"harga dasar = Rp{harga}")
print (f"total diskon = Rp{totaldiskon}")
print (f"total transaksi = Rp{harga} - Rp{totaldiskon} + Rp{bagasi} = Rp{totalsemua}")