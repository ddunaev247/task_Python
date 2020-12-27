# Дан список целых чисел. Подсчитать сколько четных чисел в списке
list = [1, -1, 2, 4, 56, 7, 11, 100, 112, 120]
i = 0
y = 0
dl_list = len(list)

while i <= dl_list - 1:
    s = list[i] % 2
    i += 1
    if s == False:
        y += 1

print(y)
