'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.'''

s = int(input('Введите сумму чисел -> '))
p = int(input('Введите произведение чисел -> '))
x = 0
for i in range(s + p):
    if x:
        break
    for j in range(s + p):
        if i + j == s and i * j == p:
            x = 1
            print(i, j)
            break
