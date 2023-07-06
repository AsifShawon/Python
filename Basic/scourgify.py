import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line argument")
else:
    read_file = sys.argv[1]
    write_file = sys.argv[2]

if not read_file.endswith(".csv") and not write_file.endswith(".csv"):
    sys.exit("Not a CSV file")


