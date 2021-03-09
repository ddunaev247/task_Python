# Написать скрипт, который будет получать на входе: обязательный параметр: адрес изображения в интернете;
# необязательный параметр: флаг, указывающий на поведение в случае, если изображение уже есть в папке:
# 1. перезаписать файл; 2. оставить оба файла(в этом случае к имени нового файла добавить случайно
# сгенерированную строку); 3. не сохранять файл. По умолчанию: перезаписать файл.
# Скрипт должен скачать указанный файл и сохранить его в папку images.

import requests
import os
from datetime import datetime
import argparse
from requests.exceptions import MissingSchema
import csv
import doctest


def valid_status(code: requests) -> bool:
    """function checks for page existence
    >>> valid_status(200)
    True
    """

    if 400 <= code < 600:
        print(f'unsuccessful download request:{code}')
        return False
    return True

def valid_content(content: requests) -> bool:
    """the function checks that the downloaded file is an image
    >>> valid_content('image')
    True
    """

    if content != 'image':
        print(f'the content is not an image, type content: {content}')
        return False
    return True

def valid_flag(flag: str) -> bool:
    """the function tests the correctness of the received flag
    >>> valid_flag('1')
    True
    """

    if flag.isdigit() == False:
        raise ValueError
    return True

def dir_exists() -> None:
    "the function checks the existence of the directory, if it does not exist - creates it"

    if not os.path.isdir('images'):
        os.mkdir('images')

def exist_file(file_name: str) -> bool:
    "function checks for file existence"

    if os.path.exists(f'images\{file_name}'):
        return True
    return False

def create_file_name(req: requests, flag: str) -> str:
    "the function creates a name for the file"

    name = req.url.split('/')[-1]
    if exist_file(name) == False or int(flag) == 1:
        return name
    else:
        name = name.split('.')[0] + '_' + datetime.now().time().strftime('%H-%M-%S') + name[-5:]
        return name

def write_image(file_name: str,req: requests):
    "the function writes the image to a file"

    dir_exists()
    with open(f'images\{file_name}', 'wb') as file:
        for chunk in req.iter_content(chunk_size=100000):
            file.write(chunk)

def prepare(file_name: str,req: requests, flag: str) -> None:
    "The function checks which flag is selected and will write if the flag is 1 or 2"

    if 0 < int(flag) < 3:
        write_image(file_name,req)
    elif int(flag) > 3:
        print('incorect flag')

def read_file(path: str) -> list:
    "the function reads information from a file into a list"

    path = os.path.normpath(path)
    list_url = open(path, 'r')
    list_url = [line.strip() for line in list_url]
    return list_url

def write_log(list_log: list) -> None:
    "this is the function of writing information to logs"

    headers = ['URL', 'NAME_FILE', 'TIME_SAVE', 'STATUS_CODE', 'COMPLITE']
    with open('logs.csv', 'a') as my_logs:
        writer = csv.writer(my_logs)
        file_is_empty = os.stat('logs.csv').st_size == 0
        if file_is_empty:
            writer.writerow(headers)
        writer.writerow(list_log)

def parameter_check(args: argparse) -> list:
    "the function will check what parameters were specified and return the list of links"

    if (args.url and args.path) or (not args.url and not args.path):
        print('Not one of the parameters is specified or both are specified')
    elif args.url:
        list_urls = [args.url]
    elif args.path:
        list_urls = read_file(args.path)
    return list_urls

def process_image(url: str,args: argparse) -> None:
    "the function will launch all the necessary functions for working with images"

    req = requests.get(url, stream=True)
    valid_status(req.status_code)
    valid_content(req.headers['Content-Type'].split('/')[0])
    file_name = create_file_name(req, args.flag)
    time_save = datetime.now()
    list_log = [req.url, file_name, time_save, req.status_code,
                valid_status(req.status_code),valid_content(req.headers['Content-Type'].split('/')[0])]
    write_log(list_log)
    prepare(file_name, req, args.flag)


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', required=False)
        parser.add_argument('-fl', '--flag', default='1', required=False)
        parser.add_argument('-pt', '--path', required=False)
        args = parser.parse_args()
        list_urls = parameter_check(args)
        number_url = 0
        for url in list_urls:
            try:
                number_url += 1
                process_image(url, args)
            except MissingSchema or OSError:
                error_for_log = [url,'No',datetime.now(), 'No', 'not transferred URL']
                write_log(error_for_log)
                print(f'error in URL №{number_url}')
                continue
            except ValueError:
                print('incorect flag')

if __name__ == '__main__':
    #doctest.testmod()
    main()
