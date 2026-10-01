tinggi_3011 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3011 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3011 = tinggi_3011
    c_3011 = a_3011
    lebar_3011 = (2 * tinggi_3011) - 2

    for i_3011 in range(1, tinggi_3011 + 1):
        b_3011 = c_3011 + 1

        for j_3011 in range(1, lebar_3011 + 1):
            if i_3011 == 1 or i_3011 == tinggi_3011:
                if j_3011 == 1 or j_3011 == lebar_3011:
                    print("#", end = "")
                else:
                    print("=", end = "")

            else: 
                if j_3011 == 1 or j_3011 == lebar_3011:
                    print("|", end = "")
                else:
                    if j_3011 == c_3011:
                        print("<", end = "")
                    elif j_3011 == b_3011:
                        print(">", end = "")
                    elif j_3011 == (lebar_3011 - c_3011):
                        print("<", end = "")
                    elif j_3011 == (lebar_3011 - c_3011 + 1):
                        print(">", end = "")
                    elif j_3011 > b_3011 and j_3011 < (lebar_3011 - c_3011):
                        print(".", end = "")
                    else:
                        print(" ", end = "")
        print()

        # logika asli java
        a_3011 -= 2

        if a_3011 <= 0:
            c_3011 = (-a_3011) + 2
        else:
            c_3011 = a_3011

                    