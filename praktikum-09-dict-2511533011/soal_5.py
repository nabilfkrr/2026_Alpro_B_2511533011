n = int(input("Number of deposits: "))
totals = {}

for i in range(n):
    line = input().split()
    name = line[0]
    amount = int(line[1])
    if name in totals:
        totals[name] = totals[name] + amount
    else:
        totals[name] = amount

total_cash = 0
top_name = ""
top_total = 0

for name, total in totals.items():
    print(name + ": " + str(total))
    total_cash = total_cash + total
    if total > top_total:
        top_name = name
        top_total = total

print("Total cash:", total_cash)
print("Top contributor:", top_name, "(" + str(top_total) + ")")