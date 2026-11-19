LAST_DIGIT = 1  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

# Input pengeluaran selama 7 hari
for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

# Inisialisasi variabel
total = 0
highest = expenses[0]
highest_day = 1
days_above_limit = 0

# Menghitung total, tertinggi, dan hari di atas batas
for i in range(len(expenses)):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        days_above_limit += 1

# Menghitung rata-rata
average = total / len(expenses)

# Menampilkan hasil
print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", round(average, 1))
print("Highest: day", highest_day, f"({highest})")
print("Days above limit:", days_above_limit)
