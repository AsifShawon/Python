def main():
    year = int(input())
    is_leap(year)


def is_leap(year):
    print(year%400==0 or (year%100!=0 and year%4==0))


main()