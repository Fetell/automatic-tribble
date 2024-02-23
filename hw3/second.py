"""
Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
s = 0
for i in list_1:
    if type(i) is int:
        s += i
    if type(i) is str and 'a' in i:
        print(i)
