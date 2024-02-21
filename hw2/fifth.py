"""
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
"""

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
operator = input('Введите оператор [+, -, *, /, ^]: ')

match operator:
    case '+': result = num1 + num2
    case '-': result = num1 - num2
    case '*': result = num1 * num2
    case '/': result = num1 / num2
    case '^': result = num1 ** num2
    case _: print('Введен недопустимый оператор')


print(f'{num1} {operator} {num2} = {result}')
