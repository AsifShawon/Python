import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
else:
    file_name = sys.argv[1]

if not file_name.endswith(".csv"):
    sys.exit("Not a CSV file")

table = []
h = True

try:
    with open(file_name, 'r') as file:
        for line in file:
            if h:
                l = line.rstrip("\n")
                header = l.split(',')
                h = False
            else:
                table.append(line.split(","))
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, header, tablefmt="grid"))