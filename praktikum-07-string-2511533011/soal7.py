# Name: Nabil Fikri
# NIM: 2511533011
# Question 7

lebar = "=" * 30
print(lebar)
space = " " * 10
print("STUDENT CARD".center(30))
print(lebar)

name = "siti aisyah"
nim = "2610511023"
name = name.strip()
space = name.find(" ")

if space == -1:
    first_name = name          
else:
    first_name = name[:space]  

username = first_name.lower() + nim[-3:]

print("Name".ljust(10) + ": " + name.title())
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": 20" + nim[:2])

print(lebar)