'''Задача 1. Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 3
# 1'''

list_1 = [1, 2, 3, 4, 5, 3]
k = 3
count_k = 0
for i in list_1:
    if i == k: count_k += 1
print(count_k)