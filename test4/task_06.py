#Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium".
num = int(input("введите число:", ))
ost = num % 1000
if num % 1000 == False:
    print("millennium")
else:
    print("остаток от деления:", ost)
