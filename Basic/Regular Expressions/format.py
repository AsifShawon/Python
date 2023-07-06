import re

name = input("What's your name: ").strip()  # here we used '.strip()' to ignore leading whitespaces

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"hello, {name}")


if matches := re.search(r"^(.+), *(.+)$", name):  #  ":=" -> assigning a value left to right and getting the boolean value
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")