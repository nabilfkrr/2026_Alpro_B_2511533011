schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a
busiest = ""
most = 0
for day, courses in schedule.items():
    if len(courses) > most:
        busiest = day
        most = len(courses)
print("Busiest day:", busiest, "(" + str(most), "courses)")

# 6b
course = input("Course name: ")
days = 0
for day, courses in schedule.items():
    if course in courses:
        days = days + 1
print(course + ":", days, "days")