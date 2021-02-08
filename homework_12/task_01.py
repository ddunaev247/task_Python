# На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут), длину перерыва(по-
# умолчанию 5 минут), количество циклов(по-умолчанию 4) и название задачи. Программа указывает оставшееся время
# фокусировки, после сигнализирует о наступлении перерыва, после сигнализирует о начале нового цикла фокусировки.
# Программа должна вести файл лога о всех запусках.

import argparse
from functions_for_task import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-tfh', '--time-focus-hours', default=0, required=False)
    parser.add_argument('-tfm', '--time-focus-min',default=25, required=False)
    parser.add_argument('-ps', '--time-pause', default=5, required=False)
    parser.add_argument('-rp', '--repeat', default=4, required=False)
    parser.add_argument('-ts', '--task', required=True)
    args = parser.parse_args()
    text_focus = 'focus'
    text_pause = 'pause'
    repeat = int(args.repeat)
    try:
        focus_time = datetime.timedelta(seconds=int(args.time_focus_hours)*3600 + int(args.time_focus_min)*60)
        pause_time = datetime.timedelta(seconds=int(args.time_pause*60))
        start = datetime.datetime.now()
        info = [args.last_name, args.first_name, start, focus_time, pause_time, repeat, args.task]
        write_log(info)
        while repeat > 0:
            timer_focus = generator(focus_time)
            remaining_time(timer_focus, text_focus)
            timer_pause = generator(pause_time)
            remaining_time(timer_pause, text_pause)
            repeat -= 1
        print('task timed out')
    except ValueError:
        print('check the entered times for time-focus-hours,time-focus-min, time-pause')

if __name__ == '__main__':
    main()
