def main():
    # print_column(3)
    # print_row(4)
    print_square(3)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(elements="?", width=3):
    print(elements * width)


def print_square(size):
    # 1st way
    # for i in range(size):  # for each row
    #     for j in range(size):  # for each brick
    #         print("#",end="")  # printing the brick
    #     print()  # printing a new line after every row is finished
    # 2nd way
    # for i in range(size):
    #     print("#" * size)  # printing every row and going in a new line
    # as we have print_row() function so the 3rd way
    for i in range(size):
        print_row("#", size)

main()
