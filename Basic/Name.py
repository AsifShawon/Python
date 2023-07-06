import sys  # sys = system

# try:
#     print("Hello, my name is", sys.argv[1])  # to use this argv we need to run this cope through terminal
# except IndexError:
#     print("Too few arguments")


# checking errors and printing name
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

# another way
# checking error
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    # through sys.exit(message) we can exit from here and do not compile further in this program

    # printing name
print("Hello, my name is", sys.argv[1])