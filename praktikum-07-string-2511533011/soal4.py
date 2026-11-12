# Name: Nabil Fikri
# NIM: 2511533011
# Question 4

phone = "082511533011"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)