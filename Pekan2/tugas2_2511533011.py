from typing import final
batas_lulus_3011 : final[float] = 75.0
print("=== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 ===")
nama_3011 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3011 = input("Masukkan Jenis Kelamin (L/P) : ")
alamat_3011 = """ 
Jl. Aur Duri, Kec. Padang Timur, 
Kota Padang, Sumatera Barat 
"""
umur_3011 = int(input("Masukkan Umur : "))
skor_3011 = float(input("Masukkan Skor Tes Awal : "))
token_3011 = 100 + 3j
lulus_3011 = skor_3011 >= batas_lulus_3011

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_3011} | Tipe: {type(nama_3011)}")
print(f"Jenis Kelamin : {jenis_kelamin_3011} | Tipe: {type(jenis_kelamin_3011)}")
print(f"Alamat Domisili:\n{alamat_3011} | Tipe: {type(alamat_3011)}")
print(f"Umur : {umur_3011} tahun | Tipe: {type(umur_3011)}")
print(f"Skor Tes Awal : {skor_3011} | Tipe: {type(skor_3011)}")
print(f"ID Token Sinyal: {token_3011} | Tipe: {type(token_3011)}")
 
print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {batas_lulus_3011}")
print(f"Apakah Dinyatakan Lulus?: {lulus_3011} | Tipe: {type(lulus_3011)}")