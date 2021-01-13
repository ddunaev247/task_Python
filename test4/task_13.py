#Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345 -> 23451
list = input("введите список:", )
stp = 1
list = list[stp:] + list[:stp]
print(list)
list1 = [1, 2, 3, 4]
list2 = []
len_list = len(list1)
i = 0
for id, elem in enumerate(list1):

    if id + 1  == len_list:
        list2.append(list1[0])
    else:
        list2.append(list1[i + 1])
    i += 1    
print(list2)

