# age = 20
# price = 19.95
# first_name = "Shawon"
# is_online = False # false can't be 'f'alse
# print("age")

# f_name = "John"
# l_name = "Smith"
# age = 20
# print(f"Name: {f_name} {l_name} and age: {age}")

# Input in python
# name = input("What is your name: ")
# print(f"Hello, {name}! How are you?")

# type conversion
# b_year = int (input("Enter your birth year: ")) # typecasting input value in an int
# age = 2023-b_year
# print(f"your age = {age}")
# # also we have float() str() bool() to typecast any variable

# string and co
# line = "What are you doing"
# print("am" in line)  # returns whether the string "am" is available in line string or not
# print("are" in line)

# arithmatic operation
# print("10 / 3 = ", 10 / 3)
# print("10 // 3 = ", 10 // 3)  # returns int number
# print("10 * 3 = ", 10 * 3)
# print("10 ** 3 = ", 10 ** 3)  # 10 ** 3 = 10 to the power 3
# print("10 % 3 = ", 10 % 3)

# if statements
# temp = 40
# if 25 < temp <= 35:  # temp > 25 and temp <= 35
#     print("Hot day")
#     print("Take an umbrella")
# elif temp > 35:
#     print("So hot")
#     print("Don't go out")
# else:
#     print("Nice day")
#     print("Go out")
# print("Ok!")  # it will appear every time the code runs


# while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # here "i++" won't work

# i = 1
# while i <= 5:
#     print(i * '*')  # it will multiply the string * every time by i
#     i += 1

# list
# names = ["Asif","Shawon","Iffat","Shajid"]
# print("List: ",names)
# print("1st element of the list: ", names[0])
# print("Last element of the list: ", names[-1])
#
# names[1] = "Shaon"
# print(names)
# print("Names from 1st to 3rd: ", names[0:3])  # list_name[included_index:excluded_index]
# # names.append("Shaf")
# names.insert(2,"Shaf")
# names.remove("Shajid")
# print(names)
# # names.clear()  # to clear the list
# print("Shaon" in names)
# print("Number of elements in the plist: ", len(names))


# for loop
# numbers = [1,2,3,4,5,6,7,8]
#
# for item in numbers:
#     print(item)

# range
# number = range(5,10)
# print(number)
# for item in number:
#     print(item)

# for i in range(1,10,2):  # range(start,end,steps)
#     print(i)

# tuples
numbers = (1,2,3)
