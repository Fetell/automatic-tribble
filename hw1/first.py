"""
2) Напишите и запустите программу. которая выводит строку  "Hello world!"
3) Напишите программу, которая на входе получает имя пользователя, сохраняет его в переменную user_name
    и выводит строку  "Hello {user_name}!"
4) Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую операцию
    (на ваше усмотрение), и выводит “Результат = {результат}”
"""

def first_hw():
    print('1.1.2)')
    print('Hello world!')


def second_hw():
    print('1.1.3)')
    user_name = str(input('What is your name? '))
    print('Hello ' + user_name + '!')


def third_hw():
    print('1.1.4)')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print('Результат = ' + str(a + b))


first_hw()
second_hw()
third_hw()
