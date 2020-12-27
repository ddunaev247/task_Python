# Составить список чисел Фибоначчи содержащий 15 элементов.
n_el = int(input("введите кол-во элементов ряда Фибоначи:", ))
el1 = 1
el2 = 1
i = 0
list = [el1, el2 ]
while i < n_el - 2:
    sum = el1 + el2
    el1 = el2
    el2 = sum
    list.append(sum)
    i += 1
print(list)


