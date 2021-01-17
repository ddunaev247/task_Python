# Написать модуль, содержащий 12 функций по переводу:

def konver_sm(per):
    return f'Дюймы в сантиметры: {per * 2.54}'


def konver_dm(per):
    return f'Сантиметры в дюймы: {per / 2.54}'


def konver_km(per):
    return f'Мили в километры: {per * 1.609}'


def konver_ml(per):
    return f'Километры в мили: {per / 1.609}'


def konver_kg(per):
    return f'Фунты в килограммы: {per / 2.205}'


def konver_fn(per):
    return f'Килограммы в фунты: {per * 2.205}'


def konver_gr(per):
    return f'Унции в граммы: {per * 28.35}'


def konver_un(per):
    return f'Граммы в унции: {per / 28.35}'


def konver_lt(per):
    return f'Галлон в литры: {per * 3.785}'


def konver_gl(per):
    return f'Литры в галлоны: {per / 3.785}'


def konver_litr(per):
    return f'Пинты в литры: {per / 2.113}'


def konver_pint(per):
    return f'Литры в пинты: {per / 2.113} '
    
    
text = '''
0.Выход из программы
1.Дюймы в сантиметры
2.Сантиметры в дюймы
3.Мили в километры
4.Километры в мили
5.Фунты в килограммы
6.Килограммы в фунты
7.Унции в граммы
8.Граммы в унции
9.Галлон в литры
10.Литры в галлоны 

введите номер функции: '''
def result():
"""This function presents an interface for the user to work with the conversion

   Input
   -------
   The user enters the number of the required conversion function, as well as the number
   to which the conversion is applied """
    dir = {1: konver_sm, 2: konver_dm, 3: konver_km, 4: konver_ml,5: konver_kg, 6: konver_fn, 7: konver_gr,
           8: konver_un, 9: konver_lt, 10: konver_gl, 11: konver_litr, 12: konver_pint}
    while True:
        fun_sel = int(input(text))
        if fun_sel == 0: break
        if fun_sel < 11:
            chislo = int(input('введите число: '))
            print(dir.get(fun_sel)(chislo))
        else:
            print('Вы ввели номер несуществующей функции')



if __name__ == "__main__":
   result()
