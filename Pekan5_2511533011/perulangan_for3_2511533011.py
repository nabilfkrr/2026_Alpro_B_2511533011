ulang_3011 = int(input("Masukkan jumlah perulangan: "))

jumlah_3011 = 0

for i_3011 in range(1, ulang_3011 + 1):
    print(i_3011, end = " ")
    jumlah_3011 += i_3011

    if i_3011 < ulang_3011:
        print("+", end = " ")
    else:
     print("=", jumlah_3011, end = " ")
print()
print ("Jumlah = ", jumlah_3011)
