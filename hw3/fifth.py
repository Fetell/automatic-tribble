"""
Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
В значения можете передать информацию о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""

film = {
    'title': input('Введите название фильма: '),
    'director': input('Введите режиссера фильма: '),
    'year': input('Введите год выхода фильма: '),
    'budget': input('Введите бюджет фильма: '),
    'main_actor': input('Введите главного актера фильма: '),
    'slogan': input('Введите слоган фильма: ')
}

for k, v in film.items():
    print(k)

for k, v in film.items():
    print(v)

for k, v in film.items():
    print(f'{k} - {v}')
