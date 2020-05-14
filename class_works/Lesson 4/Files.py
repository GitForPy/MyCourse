from pprint import pprint

path = r'C:\Users\Александр\Desktop\Python Нетология 20\1.Основы Python\[BOOMINFO.RU] 4. Работа с датами в Python\Дополнительные материалы к уроку 4\transactions.tsv'

total_running = 0
counter_dates = 0
d = {}
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        counter_dates += 1
        date, amount = line.strip().split()
        total_running += int(amount)
        d.setdefault(date, int(amount))
        d[date] += int(amount)
        print(f'{date}: {amount} and total is {total_running}')

avg = total_running/counter_dates
print(f'Total is {total_running}')
print('Avg is {:.0f} '.format(avg))
print('Max value is:', max(d.values()))
pprint(sorted(d.items(), key=lambda x: -x[1]))

