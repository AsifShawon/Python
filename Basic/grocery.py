# question link: https://cs50.harvard.edu/python/2022/psets/3/grocery/

grocery = {}
g_list = []


def main():
    print_grocery()


def count_item(item):
    count = 0
    for i in g_list:
        if item == i:
            count += 1

    return count


def print_grocery():
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        try:
            g_list.append(item)
        except TypeError:
            pass
        grocery[item] = 1

    for i in sorted(grocery):
        print(count_item(i), i)
    # print(g_list)


if __name__ == "__main__":
    main()
