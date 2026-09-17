print("=======================================")
print("1. OPERATOR KEANGGOTAAN")
print("=======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3011 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3011 = [int(angka_3011.strip()) for angka_3011 in input_data_3011.split(",")]

nilai_dicari_3011 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3011 = nilai_dicari_3011 in data_3011
print("\nOperator keanggotaan IN")
print(nilai_dicari_3011, "in", data_3011, "=", hasil_3011)

# Operator not in
hasil_3011 = nilai_dicari_3011 not in data_3011
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3011, "not in", data_3011, "=", hasil_3011)

print("\n=======================================")
print("2. OPERATOR IDENTITAS")
print("=======================================")

# objek1 menggunakan list dari input pengguna
objek1_3011 = data_3011

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3011 = objek1_3011

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3011 = data_3011.copy()

print("objek1 =", objek1_3011)
print("objek2 =", objek2_3011)
print("objek3 =", objek3_3011)

# Operator is
hasil_3011 = objek1_3011 is objek2_3011
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_3011)

# Operator is not
hasil_3011 = objek1_3011 is not objek3_3011
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3011)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_3011 is objek3_3011)
print("objek1 == objek3 =", objek1_3011 == objek3_3011)