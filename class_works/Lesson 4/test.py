#
# # arr = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(max(arr))
#

# s = ['Иванов', 'Сидоров', 'Петров']
# right_offset = len(max(s, key=len))
# for i, item in enumerate(s, start=10):
#     print(f'{i}. {item.rjust(right_offset )}')
#
#
#
# # Дан список фруктов
# # напишите программу, выдающу шахматистов в виде нумерованного списка, выровненого по правой стороне
#
# data = ['Каспаров', 'Карпов', 'Крамник', 'Иванчук', 'Топалов', 'Иванчук', 'Ботвиник', 'Капабланка']
# #
# right_offset = len(max(data, key=len))
# for index, item in enumerate(data, start=1):
#     # print(index, item)
#     print('{}. {}'.format(index, item.rjust(right_offset)))


# # Задача 2
# # Даны два произвольных списка.
# # Удалите из первого списка элементы, присутствующие во втором списке.
#
# list_a = [1, 2, 3, 4, 5, 6]
# list_b = [3, 4, 5, 6, 7]
#
#
# def diff_list(set1, set2):
#     for digit in set1.copy():
#         if digit in set2:
#             set1.remove(digit)
#     print(set1)

# while b in list_b:
#     list_a.remove(b)
#
#
# # diff_list(list_b, list_a)
#
# list_a = [1, 2, 3, 4, 5, 6]
# for a in list_a:
#     print(a)

#


#
# # Способ 2
# list_a = [1, 2, 3, 4, 5, 6]
# for a in list_a[:]:  # через срез итеррируемся по коллекции. Фактически таже самая копия. проходимся по другой
#     print(a)         # области памяти, по другой переменной и все хорошо работет.
#     list_a.remove(a)
# print(f'Финальный список {list_a}')
#
#
#
# # такая есть особенность, о ней нужно знать. Вроде по всем элементам прошлись, а что-то еще осталось.
# # как с этим бороться?


# Датчик принимает сигнал, состоящий из 0 и 1.
# Известно, что сигнал имеет периодичность, не превышающей натурального числа n.
# Напишите код, который вычисляет периодичность сигнала.
# Считайте, что 3 < n < 1000, а общая длина сигнала значительно превышает n.
# Пример сигнала с периодичностью 4 (повторяющийся элемент 1011): 1011101110111011101110111011101110111011

# s[:3] == s[3:6]

s = '1011101110111011101110111011101110111011'


# pattern = 'no pattern '
# step = 3
# for i in range(0, len(s)//2, step):
#     print(i, s[:step])

    
# Шаг 1
step = 3
n = 3
while True:
    for i in range(0, len(s), step):
        print(s[:step])
        print(s[n * i + step:2*(n * i + step)])
        break
    break

# Шаг 2
# step = 3
# n = 3
# while True:
#     for i in range(0, len(s), step):
#         # print(s[:step])
#         # print(s[n * i + step:2*(n * i + step)])
#         if s[:step] != s[n * i + step:2 * (n * i + step)]:
#             break
#     break

# # Шаг 3
# n = 3
# step = 3
# pattern = ''
# while True:
#     for i in range(0, len(s), step):
#         # print(s[:step])
#         # print(s[n * i + step:2*(n * i + step)])
#         pattern = s[:step]
#         if pattern != s[n * i + step:2 * (n * i + step)]:
#             break
#     break
# print(pattern)
#
# # Шаг 4 обнулять патерн
# n = 3
# step = 3
# pattern = ''
# while True:
#     for i in range(0, len(s), step):
#         # print(s[:step])
#         # print(s[n * i + step:2*(n * i + step)])
#         pattern = s[:step]
#         if pattern != s[n * i + step:2 * (n * i + step)]:
#             pattern = 'no pattern'
#             step += 1
#             break
#     break
# print(pattern)
#




# s = '10111011101110111011'
# s = '101101'
# s = '101101101'
# s = '101101101101'
# s = '11111111111111111111'
# s = '01000011'
# print('01000011' != s)
#
pattern_sequence = ''
step = 3
#while len(pattern_sequence) < len(s) // 2 or pattern_sequence != s:
while pattern_sequence != s:
    for i in range(0, len(s) // 2, step):
        pattern_sequence = s[:step + i]
        print(step, pattern_sequence)
        if pattern_sequence != s[step:2 * step + i]:
            pattern_sequence = ''
            step += 1
            break

pattern = s[:step]
print('Answer:', pattern)


# первые три элемента сравниваем со следующими тремя; потом еще три с еще тремя;
# Зачем нам так гонять цикл до конца строки, если уже на первом шаге понятно, что 3 это не переодичность.
# Нужно step увеличить на единицу и запустить этот цикл заново, чтобы он начал с начала строки и взял последовательность
# из 4 элементов (за шаблон)

# Как распознать патерн  0000000?

# Мы не знаем сколько итераций нам нужно, чтобы вычислить и поэтому можно в начале задать цикл While True
# таким образом мы избавимся от нашей переменной флаг
# Мы сможем в нужный момент сразу сделать брейк или континиу и у нас цикл прервется. Если мы нашли патерн
# строку до конца и убедились в том, что этот патер действительно повторяется
# То есть внешняя оболочка у нас получается While True а дальше мы задаем цикл for как раз таки для нахождения патерна
# Цикл While нужен для того, чтобы повторять обход этой строки до тех пор пока мы не найдем патерн либо
# не Пройдем всю строку и закончим.




#         print(f'периодичность сигнала равна{n+i}')
#     else:
#         Flag = False
# print(flag)
#


# print(signal[:3])
# print(signal[3:6])
# print(signal[:3] == signal[3:6])
#
# n = 3
# for i in signal:
#     if signal[:n] == signal[n:2*n]:
#         print('Сигнал имеет периодчность')
#     else:
#


# a = [0, 1, 2, 4] * 4
# Flag = 1
# for m in range(len(a) - 8):
#     for i in range(len(a) - (m + 3)):
#         if a[i] == a[i + 3 + m]:
#             Flag = 1
#             print(f'Успешная последовательность: {a[:(3 + m)]}')
#             break  # если находит 1 неправильный останавливается#
#         else:
#             continue
#
#
#
# print('Последовательность не подходит')
