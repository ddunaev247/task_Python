# Дан список целых чисел. Создать новый список, каждый элемент которого равен
# исходному элементу умноженному на -2
list = [2, 3, 4, 5]
dl_list = int(len(list))
#print(dl_list)
i = 0

while i <= dl_list - 1:
    list[i] = list[i] * -2
    i += 1
print(list)
