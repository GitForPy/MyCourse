import json
from pprint import pprint


# Переведите содержимое файла purchase_log.txt в словарь purchases вида:
# {'1840e0b9d4': 'Продукты', ...}
'''
 'fffb1b6b85': ['Электроника', 'Досуг'],
 'fffcbf94dc': ['Бытовая техника'],

'''
# with open('resources/purchase_log.txt', encoding='utf-8') as p:
#     next(p)
#     data = p.readlines()
file = open('resources/purchase_log.txt', encoding='utf-8')
next(file)
data = file.readlines()
file.close()

ids = []
purchases = dict()
for i, item in enumerate(data):
    user_id, value = list(json.loads(item).values())
    if user_id in purchases.keys():
        ids.append(user_id)
        purchases[user_id].append(value)
    else:
        purchases[user_id] = [value]
    # if len(purchases[user_id]) > 2:
    #     print(user_id, purchases[user_id])


pprint(len(purchases))  # 99517
pprint(len(ids))  # 482
pprint(99999 - 99517)  # 99517
#print(ids)
#pprint(purchases)

output = open('resources/funnel.csv', 'w', encoding='utf-8')
with open('resources/visit_log.csv', encoding='utf-8') as file_visits:
    header = file_visits.readline()
    output.write(header.strip() + ',categories\n')
    line = file_visits.readline()
    while line:
        user_id, source = line.strip().split(',')
        if user_id in purchases.keys():
            new_line = user_id + ',' + source + ',' + ','.join(purchases[user_id]) + '\n'
            output.write(new_line)
        line = file_visits.readline()
output.close()






