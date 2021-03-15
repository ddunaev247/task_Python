# Создать сайт, содержащий 3 страницы: главную, страницу со списком пользователей, детальную страницу пользователя.
# 2. При переходе на главную страницу должна отобразится страница с приветственной надписью для пользователя.
# 3. При переходе на страницу со списком пользователей - должна отобразится страница, где перечислены
# пользователи в виде ссылок. При клике на любую из них должен осуществиться переход на детальную страницу пользователя.
# 4. При переходе на детальную страницу пользователя должна открыться страница с приветствием пользователя по его имени
# и текущее время с указанием утро это, день, вечер или ночь(6 - 12 утро,
# 12 - 16 день, 16 - 0 вечер, 0 - 6 ночь), например: Привет, Жора! Сейчас 23:00:32. Приятного вечера!

from flask import Flask,render_template
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

@app.route('/users/')
def list_users():
    return render_template('list_users.html')

@app.route('/users/<name>/')
def user(name):
    users = {'dima': 'Дима', 'masha': 'Маша', 'vanya': 'Ваня'}
    name = users.get(name)
    info_time = time_of_day()
    return render_template('user.html',name=name,info_time=info_time)

if __name__ == '__main__':
    app.run()
