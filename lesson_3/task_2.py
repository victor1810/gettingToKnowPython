'''Задача 2. Требуется найти в массиве list_1 самый близкий по величине элемент
к заданному числу k и вывести его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5'''

list_1 = [1, 4, 3, 7, 8, 9, 2, 14]
k = 12
num = None
num_diff = None
diff = None
for i in list_1:
    diff = abs(i - k)
    if num_diff is None or diff < num_diff:
        num = i
        num_diff = diff

print(num)