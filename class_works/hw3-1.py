import sys

commands = {

}


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]


directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;


def people(doc_number):
    # doc_number = input('Введите номер документа ')  # запрашиваем у пользователя номер документа
    for row in documents:  # список состоит из словарей; итерируемся по словарям
        if row['number'] == doc_number:  # в каждой итерации проверяем по ключу Number значение, кот указал польз-ль.
            owner = row['name']          # записываем в переменную owner = инициала собственника док-та
            print(f'Владелец документа: {owner}')  # Выводим собственника док-та
            return owner
    print('В системе запись не найдена')

if sys.argv[1] in ['-p', '--people']:
    people(sys.argv[2])

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится


def shelf():
    doc_number = input('Введите номер документа ')  # запрашиваем номер док-та;
    for key, value in directories.items():  # итерируемся по ключам и значениям в директории
        for number in value:                # в значениях итерируемся по списку
            if number == doc_number:        # если в списке находим нужный док-т, то выводим номер полки
                print(f'\nДокумент находится на полке №{key}')
                return key
    print('Документ не найден')

# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"


def list_doc():
    result = ''
    for row in documents:
        doc_type = row['type']
        number = row['number']
        owner = row['name']
        result += f'{doc_type} "{number}" "{owner}"\n'
    print(result)
    return result


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень


def add_shelf():
    new_shelf = input('Введите номер новой полки ')
    if new_shelf in directories:
        print('Такая полка уже существует')
    else:
        directories[new_shelf] = []
        print(f'\nПолка №{new_shelf} добавлена.\n{directories}')

    # new_shelf = input('Введите номер новой полки ')
    # directories.setdefault(new_shelf, [])

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;


def delete():
    doc_number = input('Введите номер документа ')
    for key, values in directories.items():
        if doc_number in values:
            values.remove(doc_number)
            for doc in documents.copy():
                if doc['number'] == doc_number:
                    documents.remove(doc)
                    break

            print('Документ удален из каталога из документов')
            return 'Документ удален из каталога из документов'
    print(f'Документ с номером {doc_number} не найден')

# delete()
# pprint(documents)
# pprint(directories)

# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ
# или переместить документ на несуществующую полку;


directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': [] }

directories['1']
# print('yes' if '1' in directories.keys() else 'no')


def move():
    print(directories)  # для отладки
    doc_number = input('Введите номер документа ')
    goal_shelf = input('Укажите целевую полку ')

    if goal_shelf not in directories.keys():  # проверяем есть ли наша целевая полка среди существующих
        print(f'Полка №{goal_shelf} не существует')
        return f'Полка №{goal_shelf} не существует'
    flag = False  # по-умолчанию считаем, что документ не существует
    for docs in directories.values():  # если такая полка есть, то начинаем проверять наличие документа
        if doc_number in docs:
            docs.remove(doc_number)
            flag = True
    if flag is False:
        print(f'Документ №{doc_number} отсутствует в базе')
        return f'Документ №{doc_number} отсутствует в базе'

    directories[goal_shelf].append(doc_number)
    print(f'\nдок-т перемещен на полку №{goal_shelf}:\n{directories}')
    return f'док-т перемещен на указанную полку: {directories}'


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его
# номер, тип, имя владельца и номер полки, на котором он будет храниться.


def add():
    doc_num = input('Введите номер документа ')
    doc_type = input('Укажите тип документа ')
    owner = input('Укажите собственника документа ')
    shelf = input('Укажите номер полки ')

    for key in directories:  # прежде, чем добавить новые записи в базу, проверяем наличие полки.
        if shelf in key:
            directories[shelf].append(doc_num)
            documents.append({'type': doc_type, 'number': doc_num, 'name': owner})
            print('\nВаш документ добавлен в Архив!')
            print(f'\nСписок: {documents}\n{directories}')
            return '\nВаш документ добавлен в Архив!'

    print('\nВнимание! Такой полки не существует.')



# people()
# shelf()
# list_doc()
# add_shelf()
# delete()
# move()
# add()

