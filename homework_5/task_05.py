# В списке целых случайных чисел с количеством элементов n определить максимальное число и
# заменить им все четные по значению элементы.
from random import sample
n = int(input('введите длину списка: '))
list = sample(range(0, 100), n)
print(list)
for id, num in enumerate(list):
    if num % 2 == 0:
        list[id] = max(list)
print(list)
