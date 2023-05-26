print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 

one = int(input(''))
two = int(input(''))
three = int(input(''))
if one > two:
    if one > three:
        print(one)
if two > three:
    if two > one:
        print(two)
if three > one:
    if three > two:
        print(three)