from datetime import datetime

'''
С помощью встроенной в Python библиотеки узнать системное время.
На основе этой информации выводить пользователю сообщение:
Добрый вечер/день/ночи в зависимости времени суток
'''

now = datetime.now()
print(now)

cur_hour = now.hour
print(cur_hour)

if 6 <= cur_hour <= 12:
    print('утро')
elif 12 < cur_hour <= 18:
    print('день')
elif 18 < cur_hour <= 24:
    print('вечер')
else:
    print('ночь')
