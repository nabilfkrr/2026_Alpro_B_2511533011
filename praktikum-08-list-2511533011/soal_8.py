number_of_rows = 4
seats_per_row = 5
# Write your code below

# Membuat denah kursi
seats = [["."] * seats_per_row for _ in range(number_of_rows)]

seats_taken = 0

while True:

    # Menampilkan denah kursi
    print("\nDenah Kursi:")

    for i in range(number_of_rows):
        print(f"Baris {i + 1}:", seats[i])

    # Meminta nomor baris
    row = int(input("Masukkan nomor baris (0 untuk keluar): "))

    # Mengakhiri program
    if row == 0:
        break

    # Meminta nomor kursi
    seat = int(input("Masukkan nomor kursi: "))

    # Memeriksa apakah baris atau kursi di luar rentang
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat")

    # Memeriksa apakah kursi sudah dipesan
    elif seats[row - 1][seat - 1] == "X":
        print("Seat already taken")

    # Memesan kursi
    else:
        seats[row - 1][seat - 1] = "X"
        seats_taken += 1
        print("Seat booked")

# Menampilkan jumlah kursi yang dipesan
print("\nSeats taken:", seats_taken)