"""
Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
содержащий только положительные числа
"""

my_list = [20, -3, 15, 2, -1, -21]

new_list = filter(lambda x: x > 0, my_list)
