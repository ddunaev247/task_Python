# Написать программу таймер. Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя оставшееся время. Программа должна хранить файл
# логирования с информацией о том кто запускал программу и когда.

import argparse
import csv
from time import sleep
import datetime
from datetime import timedelta

def generator(t:datetime) -> str:
    """this time generating function"""
    while t >= datetime.datetime(1,1,1,00,00,00,1):
        sleep(1)
        t = t - timedelta(seconds=1)
        yield t.strftime('%H:%M:%S')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-hr', '--hours', required=True)
    parser.add_argument('-mn', '--minutes', required=True)
    parser.add_argument('-sc', '--seconds', required=True)
    args = parser.parse_args()
    try:
        time_user = datetime.datetime(1,1,1,hour=int(args.hours),minute=int(args.minutes),second=int(args.seconds))
        start = datetime.datetime.now()
        with open ('logs.csv', 'a') as my_logs:
            writer = csv.writer(my_logs)
            writer.writerow([args.last_name, args.first_name, start])
        timer = generator(time_user)
        for i in timer:
            print(i)
        print('ALARM!')
    except ValueError:
        print('check the entered values: hours, minutes, seconds')

if __name__ == '__main__':
    main()






