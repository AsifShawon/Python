'''
# defining a function "hello()" with parameter "name"
def hello(name):
    print("hello,", name)

name = input("What's your name: ")
hello(name)  # calling the hello() function with "name" argument
'''


# here we defined a function hello() which have a parameter "to"
# the parameter is in default "world" [ to = "world" ]
# if user gives nothing in the argument the hello() function will take to="world"
# as default parameter
def hello(to="World"):
    print("Hello,", to)

name = input("Who are you? ")
hello(name)  # calling hello() function with name argument [that will change to=name]
hello()  # calling hello() function without argument
