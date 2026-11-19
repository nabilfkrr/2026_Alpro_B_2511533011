menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(number_of_days):
    row = []

    for menu in menus:
        jumlah = int(input(f"Day {day + 1}, {menu}:"))
        row.append(jumlah)

    sales.append(row)

# Menghitung total penjualan setiap hari
print("\nTotal per day:")

for i in range(number_of_days):
    total = 0

    for j in range(len(menus)):
        total += sales[i][j]

    print(f"Day {i + 1}: {total}")

# Menghitung total penjualan setiap menu
menu_totals = []

for j in range(len(menus)):
    total = 0

    for i in range(number_of_days):
        total += sales[i][j]

    menu_totals.append((menus[j], total))

print("\nTotal per menu:", menu_totals)

# Mencari menu terlaris
best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print("Best seller:", best_name, f"({best_total})")    

     
