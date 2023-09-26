'''Напишите функцию print_operation_table(operation, num_rows, num_columns),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст - ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
как, например, у операции умножения. Пример:
На входе:
print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:
1 2 3
2 4 6
3 6 9'''

'''def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            for j in range(2, num_columns + 1):
                answer = operation(i, j)
                print(answer, end=' ')
            print()'''

def print_operation_table(operation, num_rows , num_columns ):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            print(i, end = ' ')
            for j in range(2, num_columns + 1):
                print(operation(i, j), end = ' ')
            print()

print_operation_table(lambda x, y: x / y, 4, 4)