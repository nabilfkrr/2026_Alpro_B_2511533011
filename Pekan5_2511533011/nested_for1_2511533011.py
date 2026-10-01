batas_3011 = int(input("Masukkan nilai batas: "))
for line_3011 in range(1, batas_3011 + 1):
    for j_3011 in range(1, (-1 * line_3011 + batas_3011) + 1):
        print(".", end = " ")
    print(line_3011)