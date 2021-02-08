# here functions for the task are described: time generator,
# counter in the console with sound notification, logging
import sys
from time import sleep
import datetime
from datetime import timedelta
import os
import csv

def generator(inp_time:datetime) -> datetime:
    """this time generating function"""

    while inp_time >= datetime.timedelta(seconds=1):
        sleep(1)
        inp_time = inp_time - timedelta(seconds=1)
        yield inp_time

def remaining_time(timer: generator, text: str) -> None:
    """this function displays the remaining time"""

    print(f'begin {text}!!!')
    for remaining in timer:
        sys.stdout.write('\r')
        sys.stdout.write("{} time left".format(remaining))
        sys.stdout.flush()
    sys.stdout.write(f'\r{text} end           \n')
    print('\a')

def write_log(list_log: list) -> None:
    """this is the function of writing information to logs"""

    headers = ['Last_name', 'First_name', 'Start_time', 'Focus_time', 'Pause_time', 'Repeat', 'Task']
    with open('logs.csv', 'a') as my_logs:
        writer = csv.writer(my_logs)
        file_is_empty = os.stat('logs.csv').st_size == 0
        if file_is_empty:
            writer.writerow(headers)
        writer.writerow(list_log)