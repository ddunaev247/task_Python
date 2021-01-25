# Дан текстовый файл, содержащий различные даты. Каждая дата - это число, месяц и год. Найти самую раннюю дату.

import time
import typing

def op_file() ->time.struct_time:
    """ this function finds the earliest date in a text file

    the function opens the file for reading and finds the earliest in the environment,
    the result is displayed in the format %d-%m-%Y
    """

    file = open('data.txt','r')
    line = file.readlines()
    line = [line.rstrip() for line in line]
    date_buf = time.strptime('31129999','%d%m%Y')
    for date_line in line:
        date_line = time.strptime(date_line,'%d%m%Y')
        if date_line <= date_buf:
            date_buf = date_line
    file.close()
    return time.strftime('%d-%m-%Y', date_buf)


def main():
    print(op_file())

if __name__ == "__main__":
    main()


