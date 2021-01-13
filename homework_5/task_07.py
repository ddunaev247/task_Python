# Дана целочисленная квадратная матрица размерности n. Заполнить ее случайными целыми числами. Найти в
# каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.
from random import sample
n = int(input('введите размер матрицы: '))
matrix = []
m = 0
pos = 0
for i in range(n):
    line = sample(range(0, 100), n)
    matrix.append(line)
print('\n'.join(map(str, matrix)))
for i in matrix:
    for j in i:
        if j == max(i):
            pos = i.index(j)
            head = i[m]
            i[m] = i[pos]
            i[pos] = int(head)
    m += 1
print('\n'.join(map(str, matrix)))
