""" 
Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

n = int(input('Введите трёхзначное число: '))
res1 = n//100
res2 = n//10%10
res3 = n%10 
print(res1+res2+res3)