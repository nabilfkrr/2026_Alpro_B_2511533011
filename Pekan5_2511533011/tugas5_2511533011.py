print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3011 = int(input("Masukkan ukuran skala jam pasir (N): "))

# ---------- Bingkai atas ----------
print("#", end="")
for kolom_3011 in range(4 * n_3011 + 5):
    print("=", end="")
print("#", end="")
print()

# ---------- Fase 1: jam pasir atas (baris N turun s.d. 1) ----------
for baris_3011 in range(n_3011, 0, -1):
    print("|", end="")
    print(" ", end="")
    for spasi_3011 in range(2 * (n_3011 - baris_3011)):
        print(" ", end="")
    for angka_3011 in range(baris_3011, 0, -1):
        print(angka_3011, end=" ")
    print("<*>", end="")
    for angka_3011 in range(1, baris_3011 + 1):
        print(" ", end="")
        print(angka_3011, end="")
    for spasi_3011 in range(2 * (n_3011 - baris_3011)):
        print(" ", end="")
    print(" ", end="")
    print("|", end="")
    print()

# ---------- Fase 2: poros titik pusat ----------
print("|", end="")
for spasi_3011 in range(2 * n_3011 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3011 in range(2 * n_3011 + 1):
    print(" ", end="")
print("|", end="")
print()

# ---------- Fase 3: jam pasir bawah (baris 1 naik s.d. N) ----------
for baris_3011 in range(1, n_3011 + 1):
    print("|", end="")
    print(" ", end="")
    for spasi_3011 in range(2 * (n_3011 - baris_3011)):
        print(" ", end="")
    for angka_3011 in range(baris_3011, 0, -1):
        print(angka_3011, end=" ")
    print("<*>", end="")
    for angka_3011 in range(1, baris_3011 + 1):
        print(" ", end="")
        print(angka_3011, end="")
    for spasi_3011 in range(2 * (n_3011 - baris_3011)):
        print(" ", end="")
    print(" ", end="")
    print("|", end="")
    print()

# ---------- Bingkai bawah ----------
print("#", end="")
for kolom_3011 in range(4 * n_3011 + 5):
    print("=", end="")
print("#", end="")
print()
