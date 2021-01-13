# Написать программу, в которой вводятся два операнда
# Х и Y и знак операции sign (+, –, /, *). Вычислить
# результат Z в зависимости от знака.
print("чтобы завершить программу введите 0 в знаке операции")
while True:
    znak = input("знак операции (+,-,*,/): ")
    if znak == '0': break
    if znak in ('+','-','*','/'):
            x = float(input("введите число x: "))
            y = float(input("введите число y: "))
            if znak == '+':
                    print(x+y)
            elif znak == '-':
                    print(x-y)
            elif znak == '*':
                    print(x*y)
            elif znak == '/':
                    if y != 0:
                            print(x/y)
                    else:
                            print("деление на ноль невозможно")
    else:
       print("неверный знак операции!")
