tc = int(input())

for i in range(tc):
    inp = input().split()
    x = int(inp[0])
    y = int(inp[1])
    a = int(inp[2])

    if x <= a < y:
        print("YES")
    else:
        print("NO")
