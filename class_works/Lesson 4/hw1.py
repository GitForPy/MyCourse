ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}

# print(' '.join(map(str, set([v for row in ids.values() for v in row]))))

print(' '.join(list(map(str, set([v for lst in ids.values() for v in lst])))))

# print([v for lst in ids.values() for v in lst])





# lst = [213, 213, 213, 15, 213]
#
# list1 = list(map(str, lst))
#
# print(' '.join(list1))



# print(' '.join(lst))






# print(' '.join(map(str, set([v for row in ids.values() for v in row]))))







# print('Решение:', ' '.join(map(str, set([v for row in ids.values() for v in row]))))





