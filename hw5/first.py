"""
Создайте любой класс с произвольным количеством подклассов, экземпляров,
атрибутов и методов - как минимум один атрибут должен быть с уровнем доступа private.
Соответственно, для получания значений этого атрибута нужно использовать методы get и set
"""


class Animal(object):

    definition = "Animal is a living thing"

    def __init__(self, name, legs):
        self.legs = legs
        self.name = name

    def hello(self):
        return f"Hello, {self.name}"

    @classmethod
    def change_def(cls, new_def):
        cls.definition = new_def

    @staticmethod
    def is_upright(legs):
        return legs == 2


class Cat(Animal):
    def __init__(self, name, legs, age, color, toy):
        super().__init__(name, legs)
        self.color = color
        self.age = age
        self.__toy = toy

    def get_toy(self):
        pass


class Human(Animal):
    def __init__(self, name, legs, age):
        super().__init__(name, legs)
        self.age = age


class QA(Human):
    def __init__(self, name, legs, age, job, salary):
        super().__init__(name, legs, age)
        self._job = job
        self.__salary = salary

    def get_job(self):
        return self._job

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

