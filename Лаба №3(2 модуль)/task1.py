class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self._name = name
        if not isinstance(author, str):
            raise TypeError('Автор книги должен быть типа str')
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError('Количество страниц в книге должно быть типа int')
        if value < 0:
            raise ValueError('Количество страниц не должно быть отрицательным')
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError('Продолжительность книги должна быть типа float')
        if value < 0:
            raise ValueError('Продолжительность книги должна быть отрицательной')
        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

