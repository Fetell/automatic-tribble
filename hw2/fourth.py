"""
Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
Текст и количество повторений нужно ввести с помощью input()
"""

a, b = input('Введите текст и количество повторений: ').split()

for i in range(int(b)):
    print(a)