"""
Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
"""

from time import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        stop = time()
        print(stop)
        print(start)
        print(f"{func.__name__} took {stop-start} seconds")
    return wrapper
