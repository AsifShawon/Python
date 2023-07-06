''''''
# python dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}


# print(students["Hermione"])
for student in students:
    print(student)
    # it will print the keys of the student dictionaries [1st value]

# for student in students:
#     print(student, students[student], sep=", ")  # here in default sep=" "[sep = seperator]


# if we have more info, and we want to organize them
# list[] of dictionaries{}
# students = [
#     {"name": "Hermione", "house": "Gryffindor","patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]
#
# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")
#     # here student is a dictionary of students list