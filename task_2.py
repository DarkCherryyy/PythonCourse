BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):

        if not isinstance(id_, int):
            raise TypeError('Идентификатор книги должен быть типа int')
        if id_ < 0:
            raise ValueError('Идентификатор книги не должен быть не отрицательным')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должен быть типа int')
        if pages < 0:
            raise ValueError('Количество страниц не должно быть отрицательным')
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        if not isinstance(books, list):
            raise TypeError("Список книг должен иметь тип list")
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, get_index: int):
        if not isinstance(get_index, int):
            raise TypeError("Запрашиваемый id должен быть типа int")
        if get_index < 0:
            raise ValueError('Запрашиваемый id не должен быть отрицательным')
        for index, book in enumerate(self.books):
            if book.id_ == get_index:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
