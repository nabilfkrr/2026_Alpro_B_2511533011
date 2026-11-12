full_name = "Nabil Fikri"
nim = "2511533011"

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
name = full_name.strip()
space = name.find(" ")

if space == -1:
    first_name = name          
else:
    first_name = name[:space]  

username = first_name.lower() + nim[-3:]
print(username)