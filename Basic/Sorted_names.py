# names = []  # creating a blank list of names
#
# with open("names.txt", "r") as file:  # opening the file
#     for line in file:  # iterating every line of the file
#         names.append(line.rstrip())  # appending the lines in the names list [as in every line there is a name
#
#
# for name in sorted(names):  # iterating the sorted names and printing them
#     print(f"Hello, {name}")

# another way
with open("names.txt", "r") as file:
    for line in sorted(file):
        print(f"Hello,", line.rstrip())
