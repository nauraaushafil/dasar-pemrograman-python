total = 0
jumlah = 0

for i in range (0,4):
    angka = float (input("input angka! "))
    total += angka
    jumlah += 1
    rata2 = total / jumlah
print (f"total        :{total}")
print (f"jumlah       :{jumlah}")
print (f"rata - rata  :{rata2}")