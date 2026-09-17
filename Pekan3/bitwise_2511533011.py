print("\n=======================================")
print("3. OPERATOR BITWISE")
print("=======================================")

angka1_3011 = int(input("Masukkan angka bitwise-1: "))
angka2_3011 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_3011, "| biner =", bin(angka1_3011))
print("angka2 =", angka2_3011, "| biner =", bin(angka2_3011))

# Bitwise AND
hasil_3011 = angka1_3011 & angka2_3011
print("\nBitwise AND (&)")
print(angka1_3011, "&", angka2_3011, "=", hasil_3011)
print("Biner hasil =", bin(hasil_3011))
print("Biner hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise OR
hasil_3011 = angka1_3011 | angka2_3011
print("\nBitwise OR (|)")
print(angka1_3011, "|", angka2_3011, "=", hasil_3011)
print("Biner hasil =", bin(hasil_3011))
print("Biner hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise XOR
hasil_3011 = angka1_3011 ^ angka2_3011
print("\nBitwise XOR (^)")
print(angka1_3011, "^", angka2_3011, "=", hasil_3011)
print("Biner hasil =", bin(hasil_3011))
print("Biner hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise NOT
hasil_3011 = ~angka1_3011
print("\nBitwise NOT (~)")
print("~", angka1_3011, "=", hasil_3011)
print("Biner hasil =", bin(hasil_3011))
print("Biner hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise geser kiri
jumlah_geser_3011 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3011 = angka1_3011 << jumlah_geser_3011
print("\nBitwise geser kiri (<<)")
print(angka1_3011, "<<", jumlah_geser_3011, "=", hasil_3011)
print("Biner hasil =", bin(hasil_3011))
print("Biner hasil (8 bit) =", format(hasil_3011, "08b"))

# Bitwise geser kanan
hasil_3011 = angka1_3011 >> jumlah_geser_3011
print("\nBitwise geser kanan (>>)")
print(angka1_3011, ">>", jumlah_geser_3011, "=", hasil_3011)
print("Biner hasil =", bin(hasil_3011))
print("Biner hasil (8 bit) =", format(hasil_3011, "08b"))