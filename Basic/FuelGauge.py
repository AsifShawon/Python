# question link: https://cs50.harvard.edu/python/2022/psets/3/fuel/

while True:
    fraction = input("Fraction: ")
    f = fraction.split(sep="/")
    try:
        x = int(f[0])
        y = int(f[1])
        result = int(round((x / y), 2) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if result <= 1:
            print("E")
        elif 99 <= result <= 100:
            print("F")
        elif 1 < result < 99:
            print(result, "%", sep="")
        else:
            continue
        break

