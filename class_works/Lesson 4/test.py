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
s = '10111011101110111011'
s = '101101'
s = '101101101'
s = '101101101101'
s = '11111111111111111111'
s = '01000011'
print('01000011' != s)
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
