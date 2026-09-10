is_lulus_3011 = True
is_Cumlaude_3011 = True

nilai_3011 =85
batas_lulus_3011 =75

status_kelulusan_3011 = nilai_3011 >= batas_lulus_3011

print("=== Cek Kelulusan ===")
print("Nilai : ", nilai_3011)
print("Apakah Lulus?", status_kelulusan_3011)
if is_lulus_3011 and is_Cumlaude_3011:
    print("Selamat Anda Lulus dengan predikat Cumlaude!")