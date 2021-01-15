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
