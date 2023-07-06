# x = float(input("Enter a number: "))
# y = float(input("Enter a number: "))
#
# # z = round(x/y,3)  # to print 3 number after decimal
# # print(z)
# z = x/y
# print(f"{z:.2f}")  # to print 2 number after decimal

n = int(input())

for i in range(n):
    inp = input().split()
    x = int(inp[0])
    y = int(inp[1])

    if (x+y) > 6:
        print("YES")
    else:
        print("NO")