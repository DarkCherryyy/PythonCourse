import doctest
from typing import Union


class Person:
    def __init__(self, weight: Union[int, float], height: Union[int, float], age: int):
        """
        Создание и подготовка к работе объекта "Person"

        :param weight: Вес человека
        :param height: Рост человека
        :param age: Возраст человека

        Примеры:
        >>> person = Person(62, 156, 19)
        """
        if not isinstance(weight, (int, float)):
            raise TypeError('Вес человека должен быть типа int или float')
        if weight <= 0:
            raise ValueError('Вес человека должен быть положительным')
        self.weight = weight

        if not isinstance(height, (int, float)):
            raise TypeError('Рост человека должен быть типа int или float')
        if height <= 0:
            raise ValueError('Рост человека должен быть положительным')
        self.height = height

        if not isinstance(age, int):
            raise TypeError('Возраст человека должен быть типа int')
        if age < 0:
            raise ValueError('Возраст человека не должен быть отрицательным')
        self.age = age

    def add_ages(self, count_ages: int) -> None:
        """
        Добавление числа лет человеку.
        :param count_ages: число добавляевых лет

        Примеры:
        >>> person = Person(62, 156, 19)
        >>> person.add_ages(2)
        """
        if not isinstance(count_ages, int):
            raise TypeError("Добавляемый возраст должны быть типа int")
        if count_ages < 0:
            raise ValueError("Добавляемый возраст должны быть не отрицательными")
        ...

    def change_weight(self, count_weight: Union[int, float]):
        """
        Изменение веса человека.
        :param count_weight: Число, на которое изменится вес.
        :raise ValueError: Если после при попытке изменения веса получается
        отрицательное число, то возвращается ошибка.

        Примеры:
        >>> person = Person(62, 156, 19)
        >>> person.change_weight(-5)
        """
        if not isinstance(count_weight, (int, float)):
            raise TypeError("Число, на которое изменится вес, должно быть типа int или float")
        ...


class Christmas_tree:
    def __init__(self, height: Union[int, float], toys: int, alive: bool):
        """
        Создание и подготовка к работе объекта "Christmas_tree"

        :param height: Высота ёлки
        :param toys: Количество игрушек на ёлке
        :param alive: Тип елки (живая ёлка (True) или искуственная (False))

        Примеры:
        >>> christmas_tree = Christmas_tree(210, 30, False)
        """
        if not isinstance(height, (int, float)):
            raise TypeError('Высота ёлки должна быть типа int или float')
        if height <= 0:
            raise ValueError('Высота ёлки должна быть положительной')
        self.height = height

        if not isinstance(toys, int):
            raise TypeError('Количество игрушек должно быть типа int')
        if toys < 0:
            raise ValueError('Количество игрушек не должно быть отрицательным')
        self.toys = toys

        if not isinstance(alive, bool):
            raise TypeError('Тип ёлки должен быть типа bool')
        self.alive = alive

    def remove_toys_from_tree(self, estimate_toys: int) -> None:
        """
        Снятие игрушек с ёлки.

        :param estimate_toys: Количество снимаемых с дерева игрушек
        :raise ValueError: Если количество снимаемых с дерева игрушек превышает количество
        игрушек на елке, то возвращается ошибка.

        :return: Количество реально убранных игрушек.

        Примеры:
        >>> christmas_tree = Christmas_tree(210, 30, False)
        >>> christmas_tree.remove_toys_from_tree(10)
        """
        if not isinstance(estimate_toys, int):
            raise TypeError('Количество снимаемых игрушек должно быть типа int')
        if estimate_toys < 0:
            raise ValueError('Количество снимаемых игрушек не должно быть отрицательным')
        ...

    def change_material_of_tree(self) -> None:
        """
        Меняет тип ёлки на противоположный (на живую или искусственную).

        Примеры:
        >>> christmas_tree = Christmas_tree(210, 30, False)
        >>> christmas_tree.change_material_of_tree()
        """
        ...


class Lamp:
    def __init__(self, material: str, is_on: bool):
        """
        Создание и подготовка к работе объекта "Lamp"

        :param material: Материал лампы
        :param is_on: Работает ли лампа в данный момента (True = Да, False = Нет)

        Примеры:
        >>> lamp = Lamp('Пластик', True)
        """
        if not isinstance(material, str):
            raise TypeError('Материал лампы должен быть типа str')
        self.material = material

        if not isinstance(is_on, bool):
            raise TypeError('Параметр, работает ли лампа, должен быть типа bool')
        self.is_on = is_on

    def change_material_of_lamp(self, new_material: str) -> None:
        """
        Меняет материал лампы на новый.

        Примеры:
        >>> lamp = Lamp('Пластик', True)
        >>> lamp.change_material_of_lamp('Металл')
        """
        if not isinstance(new_material, str):
            raise TypeError('Новый материал лампы должен быть типа str')

    def changing_lamp_mode(self):
        """
        Меняет режим работы лампы на противоположный (включено/выключено).

        Примеры:
        >>> lamp = Lamp('Пластик', True)
        >>> lamp.changing_lamp_mode()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
