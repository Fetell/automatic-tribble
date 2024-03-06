"""
Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
"""

from third import my_list
from functools import reduce

prod = reduce(lambda a, b: a * b, my_list)
