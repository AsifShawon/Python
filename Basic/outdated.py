month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date = input("Date: ")
    y_m_d(date)


def y_m_d(date):
    while True:
        form = check_format(date)
        if form == "s_date":
            d = date.split()
            try:
                first = d[0]
                second = int(d[1][:-1])
                third = int(d[2])
            except (ValueError, IndexError):
                main()
            # print(first, second, third)
            m_ind = 0
            for i in range(len(month)):
                if month[i] == first:
                    m_ind = i + 1
                    break

            if 1 <= third <= 9999 and 1 <= m_ind <= 12 and 1 <= second <= 31:
                print(f"{third}-{m_ind:02}-{second:02}")
                break
            else:
                main()

        elif form == "i_date":
            d = date.split("/")
            try:
                first = int(d[0])
                second = int(d[1])
                third = int(d[2])
            except ValueError:
                main()
            try:
                if 1 <= third <= 9999 and 1 <= first <= 12 and 1 <= second <= 31:
                    print(f"{third:04}-{first:02}-{second:02}")
                    break
            except UnboundLocalError:
                main()
        else:
            main()


def check_format(date):
    if 'A' <= date[0] <= 'Z':
        return "s_date"
    elif '0' <= date[0] <= '9' or '0' <= date[1] <= '9':
        return "i_date"
    else:
        return "w_date"


if __name__ == "__main__":
    main()
