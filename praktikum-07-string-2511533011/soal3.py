# Name: Nabil Fikri
# NIM: 2511533011
# Question 3

# soal 3 bagian a
text = "Informatika"
print(text[-1])
print(text.upper())
print(text[0:20])

# soal 3 bagian b
text = "Nabil Fikri"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("\nVowels:", count)
