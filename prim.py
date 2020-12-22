# решения примера с 2-мя действительными числами.
x = float(input("введите число x:", ))
y = float(input("введите число y:", ))
rezult = (abs(x) - abs(y)) / (1 - abs(x * y))
print(rezult)
