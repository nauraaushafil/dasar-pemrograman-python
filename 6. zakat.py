harta = int(input("berapakah harta kamu? "))
hutang = int(input("berapakah hutang kamu? "))
kekayaan = harta - hutang
print (kekayaan)
if kekayaan >= 1000000:
    haul = (input("apakah sudah masuk haul? " ))
    if haul == "sudah":
     zakat = kekayaan * 2.5 / 100
     print (f"anda perlu membayar zakat senilai = {zakat}")
    else:
     print ("anda tidak wajib zakat ")
elif kekayaan < 1000000:
    print ("anda tidak wajib zakat")
