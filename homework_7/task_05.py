# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер
# строки в списке. Использовать генератор списков.

def format_list() -> list:
    """This function formats a list of strings

    Input
    -------
    User enters words of their choice

    Result
    -------
    The result will be a list of the form: {number} - {string}
    """


    words = str(input('enter lines: '))
    list_lines = words.split()
    assert len(list_lines) != 0, 'the list must not be empty'
    list_lines = ['{' + str(i) + '}' + ' - ' + '{' + word + '}' for i, word in enumerate(list_lines, 1)]
    return list_lines

if __name__ == "__main__":
    print(format_list())



