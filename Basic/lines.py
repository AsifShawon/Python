# Question link: https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
else:
    file_name = sys.argv[1]

if not file_name.endswith(".py"):
    sys.exit("Not a Python file")

try:
    count_line = 0
    with open(file_name, 'r') as file:
        for line in file:
            l = line.split()
            if len(l) < 1 or l[0] == '#':
                # print(line.split())
                pass
            else:
                # print(line)
                count_line += 1
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(count_line)
