"""
Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы  (a+b)2
    и сумму квадратов a2+b2 этих чисел.
Пример:

Input:
3
2

Output:
Квадрат суммы 3 и 2 равен 25
Сумма квадратов 3 и 2 равна 13
"""

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', a**2+b**2)
