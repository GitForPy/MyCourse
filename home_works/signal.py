# Датчик принимает сигнал, состоящий из 0 и 1.
# Известно, что сигнал имеет периодичность, не превышающей натурального числа n.
# Напишите код, который вычисляет периодичность сигнала.
# Считайте, что 3 < n < 1000, а общая длина сигнала значительно превышает n.
# Пример сигнала с периодичностью 4 (повторяющийся элемент 1011): 1011101110111011101110111011101110111011

# s[:3] == s[3:6]



# pattern = 'no pattern '
# step = 3
# for i in range(0, len(s)//2, step):
#     print(i, s[:step])


# # Шаг 1
# step = 3
# n = 3
# while True:
#     for i in range(0, len(s), step):
#         print(s[:step])
#         print(s[n * i + step:2*(n * i + step)])
#         break
#     break

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


# pattern_sequence = ''
# step = 3
# #while len(pattern_sequence) < len(s) // 2 or pattern_sequence != s:
# while pattern_sequence != s:
#     for i in range(0, len(s) // 2, step):
#         pattern_sequence = s[:step + i]
#         print(step, pattern_sequence)
#         if pattern_sequence != s[step:2 * step + i]:
#             pattern_sequence = ''
#             step += 1
#             break
#
#
# pattern = s[:step]
# print('Answer:', pattern)

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


s = '1011101110111011101110111011101110111011'

def sequence_finder(s):
    step = 3
    while step <= len(s) // 2:
        for i in range(0, len(s) // 2 + 1, step):
            pattern_sequence = s[:step + i]
            # print(step, pattern_sequence)
            if pattern_sequence != s[step:2 * step + i]:
                step += 1
            else:
                pattern = s[:step]
                print('Answer:', pattern)
                return pattern
    else:
        print('no pattern')


sequence_finder('1011101110111011101110111011101110111011')
sequence_finder('10111011101110111011')
sequence_finder('101101')
sequence_finder('101101101')
sequence_finder('101101101101')
sequence_finder('11111111111111111111')
sequence_finder('0000')
sequence_finder('01000011')
sequence_finder('')
sequence_finder('0')
sequence_finder('01')
sequence_finder('01'*1000)
sequence_finder('101110111111101110111111')  # 101110111111




