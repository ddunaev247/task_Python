# Написать скрипт, который будет получать на входе: обязательный параметр: адрес изображения в интернете;
# необязательный параметр: флаг, указывающий на поведение в случае, если изображение уже есть в папке:
# 1. перезаписать файл; 2. оставить оба файла(в этом случае к имени нового файла добавить случайно
# сгенерированную строку); 3. не сохранять файл. По умолчанию: перезаписать файл.
# Скрипт должен скачать указанный файл и сохранить его в папку images.

import requests
import os
import datetime
import argparse
import sys
from excepion import StatusError, ContentError
from requests.exceptions import MissingSchema
import doctest

def valid_status(code: requests) -> bool:
    """function checks for page existence
    >>> valid_status(200)
    True
    """

    if code == 404:
        raise StatusError
    return True

def valid_content(content: requests) -> bool:
    """the function checks that the downloaded file is an image
    >>> valid_content('image')
    True
    """

    if not content == 'image':
        raise ContentError
    return True

def write_image(file_name: str,req: requests) -> None:
    """ the function writes the file to the folder images"""

    if not os.path.isdir('images'):
        os.mkdir('images')
    with open(f'images\{file_name}', 'wb') as file:
        for chunk in req.iter_content(chunk_size=100000):
            file.write(chunk)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url', required=True)
        parser.add_argument('-fl', '--flag', default=1, required=False)
        args = parser.parse_args()
        req = requests.get(args.url, stream=True)
        content = req.headers['Content-Type'].split('/')[0]
        valid_status(req.status_code)
        valid_content(content)
        file_name = req.url.split('/')[-1]
        file_name_2 = file_name.split('.')[0] + '_' + datetime.datetime.now().strftime('%Y-%m-%d') + file_name[-5:]

        if int(args.flag) == 1:
            write_image(file_name, req)
        elif int(args.flag) == 2:
            write_image(file_name_2, req)
        elif int(args.flag) == 3:
            sys.exit(0)
        else:
            print('incorrect flag')

    except MissingSchema:
        print(f'error in URL')
    except StatusError as error:
        print(f'check the request is correct: {error}',  end='\n\n')
    except ContentError as err:
        print(f'content is not an image: {err}', end='\n\n')



if __name__ == '__main__':
    #doctest.testmod()
    main()



