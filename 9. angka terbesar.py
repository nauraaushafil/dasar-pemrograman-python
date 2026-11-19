angka1 = int(input("inputkan angka pertama! "))
angka2 = int(input("inputkan angka kedua! "))
angka3 = int(input("inputkan angka ketiga! "))
if angka1 > angka2 and angka1 > angka3:
    print ("bilangan terbesar adalah", angka1)
elif angka2 > angka1 and angka2 > angka3:
    print ("bilangan terbesar adalah", angka2)
#elif angka3 > angka1 and angka3 > angka2:
   # print ("bilangan terbesar adalah", angka3)
else:
    print ("bilangan terbesar adalah", angka3)
