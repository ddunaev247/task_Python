# Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время
# отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20
# минут. (Примечание: использовать возможности библиотеки datetime).

import datetime

city_o = ['Minsk', 'Gomel', 'Orsha', 'Bobr']
t1 = datetime.datetime(2021, 1, 1, 9, 10)
t2 = datetime.datetime(2021, 1, 1, 9, 15)
t3 = datetime.datetime(2021, 1, 1, 10, 40)
t4 = datetime.datetime(2021, 1, 15, 5, 11)
time1 = [t1.strftime("%Y-%m-%d-%H.%M"), t2.strftime("%Y-%m-%d-%H.%M"),
          t3.strftime("%Y-%m-%d-%H.%M"), t4.strftime("%Y-%m-%d-%H.%M")]
time_o = [t1,t2,t3,t4]

city_p = ['Mogilev', 'Krupki', 'Tolochin', 'Brest']
t11 = datetime.datetime(2021, 1, 1, 17, 10)
t22 = datetime.datetime(2021, 1, 1, 9, 15)
t33 = datetime.datetime(2021, 1, 1, 17, 10)
t44 = datetime.datetime(2021, 1, 15, 7, 11)
time2 = [t11.strftime("%Y-%m-%d-%H.%M"), t22.strftime("%Y-%m-%d-%H.%M"),
          t33.strftime("%Y-%m-%d-%H.%M"), t44.strftime("%Y-%m-%d-%H.%M")]
time_p = [t11,t22,t33,t44]

train = [1, 2, 3, 4]
dict1 = {city: v for city, v in zip(city_o,time1)}
dict2 = {city2:v2 for city2, v2 in zip(city_p,time2)}
info = []
dan1 = list(dict1.items())
dan2 = list(dict2.items())

for i in range(4):
    info.append(f'{dan1[i]} -> {dan2[i]}')
train_dict = {key: value for key, value in zip(train, info)}

for i in range(4):
    delta = time_p[i] - time_o[i]
    if delta.seconds > 26400:
        print(train[i], train_dict[train[i]])



