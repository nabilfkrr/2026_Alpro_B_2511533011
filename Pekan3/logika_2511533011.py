a1_3011 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3011 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3011)
print("A2 =", a2_3011)

# Konjungsi: bernilai True jika keduanya True
hasil_3011 = a1_3011 and a2_3011
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3011)

# Disjungsi: bernilai True jika salah satunya True
hasil_3011 = a1_3011 or a2_3011
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3011)

# Negasi A1: membalik nilai A1
hasil_3011 = not a1_3011
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3011)

# Negasi A2: membalik nilai A2
hasil_3011 = not a2_3011
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3011)

# XOR: bernilai True jika kedua nilai berbeda
hasil_3011 = a1_3011 != a2_3011
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3011)