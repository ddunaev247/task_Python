# Дано число. Найти сумму и произведение его цифр.
ch = int(input("введите число: "))
sum = 0
pr = 1
while ch > 0:
    sum += ch % 10
    pr *= ch % 10
    ch = ch // 10
print("сумма:", sum)
print("произведение:", pr)
