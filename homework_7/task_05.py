# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер
# строки в списке. Использовать генератор списков.

def format_list():
    """This function formats a list of strings

    Input
    -------
    User enters words of their choice

    Result
    -------
    The result will be a list of the form: {number} - {string} """


    words = str(input('введите строки: '))
    list = words.split()
    list = ['{' + str(i) + '}' + ' - ' + '{' + word + '}' for i, word in enumerate(list, 1)]
    print(list)

if __name__ == "__main__":
    format_list()




