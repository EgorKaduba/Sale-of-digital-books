class Book:
    """
    Класс Книги:

    book_id - id книги
    title - название
    author - автор
    year - год издания
    price - цена
    link - сслыка на книгу
    """
    def __init__(self, book_id, title, author, year, price, link):
        self.__id = book_id
        self._title = title
        self._author = author
        self._year = year
        self._price = price
        self._link = link

    # Найти книгу по названию
    @staticmethod
    def get_book(title: str, books):
        for book in books:
            if book['title'] == title:
                return book
        return None

    # Функция, сериализующая данные для записи в файл
    def to_json(self):
        return {
            'book_id': self.__id,
            'title': self._title,
            'author': self._author,
            'year': self._year,
            'price': self._price,
            'link': self._link
        }
