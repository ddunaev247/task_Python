# Дан текстовый файл, содержащий различные даты. Каждая дата - это число, месяц и год. Найти самую раннюю дату.

import datetime

def op_file() -> datetime.date:
    """ this function finds the earliest date in a text file

    the function opens the file for reading and finds the earliest in the environment,
    the result is displayed in the format %d-%m-%Y
    """

    file = open('data.txt','r')
    line = file.readlines()
    line = [line.rstrip() for line in line]
    date_buf = datetime.datetime(9999,12,31)
    for date in line:
        date = datetime.datetime.strptime(date, '%Y.%m.%d')
        if date < date_buf:
            date_buf = date
    return date_buf.date()


def main():
    print(op_file())

if __name__ == "__main__":
    main()
