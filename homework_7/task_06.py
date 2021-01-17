# Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов и
# выводит словарь с ключами удвоенной длины. {‘abc’:5} -> {‘abcabc’: 5}

print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(tet = 1, ltc = 2, rip = 3, eth = 4, btc = 5))
