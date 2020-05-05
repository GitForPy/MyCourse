
# открываем файл для чтения (опция r)
# f = open('visit_log.csv', 'r')
# f = open(r'resources\visit_log.csv', encoding='utf-8')
f = open(r'../../../PycharmProjects/Нетология/resources/requirements.txt', encoding='utf-8')
file = f.readlines()
f.close()
print(len(file))

s = set(file)
print(len(s))

for line in s:
    print(line.strip())


f = open(r'../../../PycharmProjects/Нетология/resources/requirements_unique.txt', 'w', encoding='utf-8')  # открытие файла на запись
f.writelines(s)  # записывает все уникальные записи разом
f.close()

'''
def read(n, include_header=False):
    f = open(r'resources\purchase_log.txt', encoding='utf-8')

    if not include_header:
        next(f)

    for line in f.readlines()[:n]:
        print(line.strip())

    f.close()


# read(5)  # вывести n строк с учетом заголовка
read(5, include_header=True)  # вывести n строк с учетом заголовка

'''