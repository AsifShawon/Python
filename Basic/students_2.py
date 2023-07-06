import csv  # to handle .csv file

students = []

# with open("students_2.csv") as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "home": row[1]})
#     for name, home in reader:
#         students.append({"name": name, "home": home})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# with open("students_2.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

name = input("What's your name? ")
home = input("What's your home? ")

with open("students_2.csv", "a", newline='') as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
