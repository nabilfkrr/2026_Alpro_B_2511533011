tinggi_3011 = int(input("Masukkan tinggi segitiga: "))

for i_3011 in range(1, tinggi_3011 + 1):
    for j_3011 in range(tinggi_3011 - i_3011):
        print(" ", end="")
    for k_3011 in range(i_3011):
        print("*", end=" ")
    print()