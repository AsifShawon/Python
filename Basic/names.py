# names = []

# for _ in range(3):
#     names.append(input("What's your name: "))
#
# for name in sorted(names):
#     print(f"Hello, {name}")


# name = input("What's your name? ")

# file

# file = open("names.txt", "w")  # opening a file # w -> means overwrite
# file = open("names.txt", "a")  # a -> append
# file.write(f"{name}\n")
# file.close()

#  another way of opening a file and closing it automatically
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# reading an existing file
# with open("names.txt", "r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(f"Hello,", line.rstrip())
#     # string_.rstrip() ->
#     # returns a new string with any trailing whitespace characters removed [like here "\n" is removed]
#     # from the right end of the original string. It does not modify the
#     # original string, but instead, it creates and returns a new string.

# another way of reading lines in file
# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"Hello,", line.rstrip())


