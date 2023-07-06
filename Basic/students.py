# csv -> comma separated values - file

# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# to get sorted values
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}   # declaring a dictionary
        # student["name"] = name
        # student["house"] = house
        student = {"name": name, "house": house}
        students.append(student)


# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# same work with lamda function

for student in sorted(students, key=lambda student: student["name"]):  # here we used lambda to use temporary function
    print(f"{student['name']} is in {student['house']}")