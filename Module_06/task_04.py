print('Задача 4. Поставьте оценку!')
print()

# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению от −100 до 100.
# Ему захотелось сравнить количество положительных и отрицательных отзывов,
# для этого он заранее отфильтровал все отзывы так,
# чтобы в конце были те, которые равны нулю.
 
# Напишите программу,
# которая находит количество положительных
# и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.
 
# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

number = int(input('Введите число: '))
minus = 0
plus = 0
if number < 0:
        minus += 1
if number > 0:
        plus += 1
while number != 0:
    number = int(input('Введите число: '))
    if number < 0:
        minus += 1
    if number > 0:
        plus += 1
print('Кол-во положительных чисел:', plus)
print('Кол-во отрицательных чисел:', minus)