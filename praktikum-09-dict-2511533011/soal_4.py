class_list = input("Class numbers: ").split()
submitted = set(input("Submitted numbers: ").split())

not_submitted = set(class_list) - submitted

print("Submitted:", len(submitted), "students")
print("Not submitted:", len(not_submitted), "students")

for number in class_list:
    if number not in submitted:
        print(number)