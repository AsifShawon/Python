# while True:
#     try:
#         x = int(input("X? "))
#     except ValueError:
#         print("x is not an integer")
#     else:  # if the exception doesn't appear
#         break
#
# print(f"x is {x}")

# another way
# while True:
#     try:
#         x = int(input("X? "))
#         break  # if exception doesn't appear here the loop will break,
#         # if exception appear it will go 12 to 14th line to handle the error
#     except ValueError:
#         print("x is not an integer")

def main():
    # x = get_int()
    # x = get_int_pass()
    x = get_int_pass_par("What's x? ")
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("X? "))
        except ValueError:
            print("x is not an integer")


def get_int_pass():
    while True:
        try:
            return int(input("what is X? "))
        except ValueError:
            pass  # we can pass without printing error


def get_int_pass_par(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
