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
f1 = 1
f2 = 1
list1 = [f1, f2]
n = 15
for i in range(3, n + 1):
    temp = f1
    f1 = f2
    f2 = temp + f1
    list1.append(f2)
print(list1)


