# Задача 32: Определить индексы элементов списка, значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
glist1 = [random.randint(1, 100) for _ in range(100)]
print(f'Случайный список: {glist1}')
glist2 = []
minimum = 9
maximum = 99
print()
for i in range(len(glist1)):
    if glist1[i] >= minimum and glist1[i] <= maximum:
        glist2.append(i)
print(f'Остортированный список: {glist2}')
