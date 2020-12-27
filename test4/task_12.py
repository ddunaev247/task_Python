#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
#получить список ключей - использовать метод .keys() (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
val = {'test': 'test_value', 'europe': 'eur', 'dollar':'usd', 'ruble': 'rub'}

i = 0
s = len(val)
l = list(val.keys())
while i <= s - 1:
    dl_key = len(l[i])
    y = l[i] + str(dl_key)
    val[y] = val.pop(l[i])
    i += 1
print(val)



