# Создать матрицу случайных чисел от a до b, размерность матрицы n*m;
from random import randint
n = int(input('введите n: '))
m = int(input('введите m: '))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(-10, 50))
    matrix.append(row)
print('\n'.join(map(str, matrix)))
# найти максимальный элемент матрицы;
print ("максимальный элемент матрицы:", max(map(max, matrix)))
# найти минимальный элемент матрицы;
print ("минимальный элемент матрицы: ", min(map(min, matrix)))
# найти сумму всех элементов матрицы;
print ("сумма всех элементов: ", sum(map(sum, matrix)))
# найти индекс ряда с максимальной суммой элементов;
max_sum = 0
col = 0
rad = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += matrix[i][j]
        if s > max_sum:
            max_sum = s
            r = max_sum
            rad = i
print("ряд с максимальной суммой эл-в: ", rad+1)
# найти индекс колонки с максимальной суммой элементов;
max_sum = 0
for i in range(m):
    s = 0
    for j in range(n):
        s += matrix[j][i]
        if s > max_sum:
            max_sum = s
            k = max_sum
            col = i
print("колонка с максимальной суммой эл-в: ", col+1)


# найти индекс ряда с минимальной суммой элементов;
for i in range(n):
    s = 0
    for j in range(m):
        s += matrix[i][j]
        if s < r:
            min_sum = s
            rad_m = i
print("ряд с минимальной суммой эл-в: ", rad_m + 1)
# найти индекс колонки с минимальной суммой элементов;
for i in range(m):
    s = 0
    for j in range(n):
        s += matrix[j][i]
        if s < k:
            min_sum = s
            col_m = i
print("колонка с минимальной суммой эл-в: ", col_m + 1, '\n')
# обнулить все элементы выше главной диагонали
for i in range(n):
    for j in range(m):
        if i < j:
           matrix[i][j] = 0
print('\n'.join(map(str, matrix)), '\n')
# обнулить все элементы ниже главной диагонали
for i in range(n):
    for j in range(m):
        if i > j:
           matrix[i][j] = 0
print('\n'.join(map(str, matrix)))
