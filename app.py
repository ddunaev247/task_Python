# 1. Интегрировать в существующий сайт из домашней работы 16.1 верстку, сделанную в домашней работе 15.
# 2. Разбить верстку на отдельные составляющие части шаблона - заголовочная часть(header), подвальная
# часть(footer), правая контентовая колонка, левая контентовая колонка и центральная контентовая часть.
# 3. Должно присутствовать минимум 2 css файла - сброс стилей по умолчанию и основной стилевой файл для сайта.
# 4. Меню вынести в отдельный шаблон. Оно должно позволять попасть на любую страницу сайта, кроме детальной страницы пользователя.
# 5. На главной странице не должно быть левой и правой колонки, только центральная с приветствием из домашнего задание 16.1
# 6. На странице со списком пользователей - список пользователей должен отобразится в левой колонке, в центральной
# колонке должен быть любой текст, описывающий данную страничку, в правой колонке - любое изображение. 
# Предусмотреть, что список пользователей может быть пустым - в этом случае должно быть соответствующее сообщение вместо
# списка.
# 7. На детальной странице пользователя - в левой колонке должен по прежнему быть список всех пользователей, в 
# центральной колонке - приветствие текущего пользователя в соответствии с домашним заданием 16.1, 
# в правой колонке - картинка, соответствующая данному пользователю. Предусмотреть, что у пользователя может
# не быть картинки - в этом случае должно подставиться изображение по умолчанию.
# 8. Если осуществляется попытка открыть страницу несуществующего пользователя - должна открываться страница 
# с ошибкой 404. Шаблон аналогичен главной странице, но в контентовой части должен быть размещен текст об ошибке.

from flask import Flask,render_template, redirect
from datetime import datetime

app = Flask(__name__)

def time_of_day() -> str:
    "this function will return a string with the current time and wish"

    time_of_day_list = ['Хорошей ночи!','Приятного утра!','Приятного дня!', 'Приятного вечера!']
    time = datetime.now().time()
    time_seconds = (time.hour * 60 * 60 + time.minute * 60 + time.second)

    if 0 <= time_seconds < 21600:
        result = time_of_day_list[0]
    elif 21600 <= time_seconds < 43200:
        result = time_of_day_list[1]
    elif 43200 <= time_seconds < 57600:
        result = time_of_day_list[2]
    else:
        result = time_of_day_list[3]
    return f'{time.strftime("%H:%M:%S")}.{result}'

@app.route('/')
def homepage():
    return render_template('homepage.html')

dima = {'name': 'Дима', 'age': 18, 'img':'https://cdn.pixabay.com/photo/2021/02/08/16/03/dinosaur-5995333_1280.png'}
masha = {'name': 'Маша', 'age': 21, 'img':'https://cdn.pixabay.com/photo/2021/02/11/08/43/couple-6004642_1280.jpg' }
vanya = {'name': 'Ваня', 'age': 19}
users = {'dima': dima, 'masha': masha, 'vanya': vanya}

@app.route('/users/')
def list_users():
    return render_template('list_users.html', users=users)

@app.route('/users/<name>/')
def user(name):

    user = users.get(name)
    if user == None:
        return redirect(404)
    info_time = time_of_day()
    return render_template('user.html',**user,info_time=info_time, users=users)

if __name__ == '__main__':
    app.run()
