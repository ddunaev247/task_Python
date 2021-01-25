# Создать CSV файл с данными следующей структуры: Имя, Фамилия, Возраст. Создать отчетный файл в
# формате CSV с информацией по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv

def age_report_csv():
    """ this function will create a report with the number of people belonging to a particular age group.

    Result
    ------
    As a result of the function, 2 files will be created. The first file will contain a table with
    the following fields: Name, Surname, Age.
    The second file will contain information on the number of people in a particular age group.
    """

    file_name = 'users.csv'
    new_file_name = 'new_users.csv'
    users = [{'last_name': 'Alex', 'first_name':'Bin', 'age': 23}, {'last_name':'Fill', 'first_name':'Rox', 'age': 12},
            {'last_name':'Joni', 'first_name':'Smith', 'age': 18}, {'last_name':'Nat', 'first_name':'Timo', 'age': 6},
            {'last_name':'Koni', 'first_name':'Ivanova', 'age': 43}, {'last_name':'Tim', 'first_name':'Flex', 'age': 41},
            {'last_name':'Rom', 'first_name':'Shut', 'age': 11}, {'last_name':'Sam', 'first_name':'kolt', 'age': 10}]
    group = {'1-12':0, '13-18':0, '19-25':0, '26-40':0, '40+':0}

    with open(file_name, 'w', newline="") as file:       # create the first file and write information to it
        columns = ['last_name', 'first_name', 'age']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(users)

    with open(file_name, 'r', newline="") as file:       # we read the file, make a selection by age group
        reader = csv.DictReader(file)
        for row in reader:
            if 1 <= int(row['age']) <= 12:
                group['1-12'] = group['1-12'] + 1
            elif 13 <= int(row['age']) <= 18:
                group['13-18'] = group['13-18'] + 1
            elif 19 <= int(row['age']) <= 25:
                group['19-25'] = group['19-25'] + 1
            elif 26 <= int(row['age']) <= 40:
                 group['26-40'] = group['26-40'] + 1
            elif int(row['age']) > 40:
                 group['40+'] = group['40+'] + 1

    with open(new_file_name, 'w', newline="") as file1: # create a report from a file with information from a selection
        columns = ['1-12', '13-18', '19-25', '26-40', '40+']
        writer = csv.DictWriter(file1, fieldnames=columns)
        writer.writeheader()
        writer.writerow(group)


if __name__ == '__main__':
    age_report_csv()
    print('work completed')
