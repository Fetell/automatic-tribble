"""
Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""

family_1 = [i for i in input().split(', ')]
family_2 = [i for i in input().split(', ')]

if len(family_1) != len(family_2):
    print(family_2) if len(family_1) < len(family_2) else print(family_1)
else:
    print('Equal')
