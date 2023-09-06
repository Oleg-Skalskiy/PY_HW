import random

list_len = int(input('Введите длину списка: '))

list_1 = [random.randint(1, 1000) for _ in range(list_len)]
print(list_1)

k = int(input('Введите число k: '))
start_num = abs(list_1[0] - k)
end_num = list[0]

count=0
for i in list_1:
# Функция abs () — это встроенная функция, возвращающая абсолютное значение числа. Она принимает целые, с плавающей точкой и комплексные числа на вход. 
# Если передать в abs () целое число или число с плавающей точкой, то функция вернет не-отрицательное значение n и сохранит тип. 
# Для целого числа — целое число. 
# Для числа с плавающей точкой — число с плавающей точкой.>>> abs (20) 20>>> abs (20.0) 20.0>>> abs (-20.0) 20.0.
    neg_to_pos = abs(i - k)
    if i==k:
        count+=1
    if neg_to_pos < start_num:
        start_num = neg_to_pos
        end_num = i

if count == 0:
    print(f'Числа нет, ближайшее число {end_num}')
else:
    print(f'Число {count} встречается раз')
