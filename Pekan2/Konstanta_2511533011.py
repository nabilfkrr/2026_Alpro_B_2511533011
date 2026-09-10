from typing import Final
PI : Final = 3.14
print("pi : %f" % (PI))
jari_3011 = float(input("Masukkan jari-jari: "))
luas_3011 = PI * jari_3011 * jari_3011
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3011, luas_3011))