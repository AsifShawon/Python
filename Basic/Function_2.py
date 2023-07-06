'''
def main():  # defining this main() function as my main function
    name = input("Who are you? ")
    hello(name)

def hello(to="World"):
    print("Hello,", to)

main()
'''


def main():
    x = int(input("Enter x: "))
    print("X square = ", square(x))


def square(x):
    return x * x  # we can do this with "x ** 2" or "pow(x,2)"


main()