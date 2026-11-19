kendaraan = (input("mobil atau motor? "))
jam = int(input("berapa jam parkirnya? "))
if kendaraan == "motor" and jam < 24:
     harga = 2000 * jam
elif kendaraan == "motor" and jam > 24:
     harga = 100000
if kendaraan == "mobil" and jam < 24:
     harga = 5000 * jam
elif kendaraan == "mobil" and jam > 24:
     harga = 100000
if jam > 5: 
     diskon = harga * (15 / 100)
     harga -= diskon
karcis = input("tunjukkan karcisnya ")
if karcis == "tidak ada":
     harga += 50000
member = input("apakah kamu punya member?")
if member == "ada":
     harga -= 2000
print (f"total harga {harga}")
     


