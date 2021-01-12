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
list1 = [2, 3, 5, 1]
n = 0
list2 = []
for elem in list1:
    list2.append(list1[n] * -2)
    n += 1
print(list2)

