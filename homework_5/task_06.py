# Задан целочисленный список c n случайных элементов. Определить количество участков списка,
# на котором элементы монотонно возрастают (каждое следующее число больше предыдущего).
from random import sample
n = int(input('введите длину списка: '))
rez = 0
s = 1
list = sample(range(0, 100), n)
print(list)
while s < len(list) -1:
    if list[s] < list[s+1] and list[s] <= list[s-1]:
        rez += 1
    s += 1
if list[0] < list[1]:
    rez += 1
print(rez)
