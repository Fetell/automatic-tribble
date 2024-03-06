"""
Напишите фукнцию, которая принимает произвольное количество именнованных аргументов
и выводит их построчно в формате аргумент: значение. Например:
name: John
last_name: Smith
age: 35
position: web developer
"""


def printer(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")


printer(name='John', last_name='Smith', age=35, position='web developer')
