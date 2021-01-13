# Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m;
from random import randint
n = int(input('введите n: '))
m = int(input('введите m: '))
matrix_a = []
matrix_b = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(-10, 50))
    matrix_a.append(row)
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(-10, 50))
    matrix_b.append(row)
print('\n'.join(map(str, matrix_a, )),'\n')
print('\n'.join(map(str, matrix_b)),'\n' )
# создать матрицу равную сумме matrix_a и matrix_b;
matrix_c = [[a+b for a, b in zip(one, two)] for (one, two) in zip(matrix_a, matrix_b)]
print(f'Сумма: ', '\n','\n'.join(map(str, matrix_c)),'\n' )
# создать матрицу равную разности matrix_a и matrix_b;
matrix_c = [[a-b for a, b in zip(one, two)] for (one, two) in zip(matrix_a, matrix_b)]
print(f'Разность: ', '\n', '\n'.join(map(str, matrix_c)),'\n' )
# создать новую матрицу равную matrix_a умноженной на число g. g вводится с клавиатуры.
g = int(input('\n''на какое число умножить матрицу№1?:' , ))
matrix_d = []
for i in range(n):
    row = []
    for j in range(m):
        el = matrix_a[i][j]
        r = el * g
        row.append(r)
    matrix_d.append(row)
print(f'Умножение на число: ', '\n', '\n'.join(map(str, matrix_d)),'\n' )
