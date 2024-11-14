from Online_store import OnlineStore
from Customer import Customer
from Order import Order
from Book import Book


class Manager:
    """
    Класс Менеджер:

    path - путь к файлу БД
    """
    def __init__(self, path: str):
        self.online_store = OnlineStore(path)  # Магазин, которым будем управлять

    # Добавление нового заказа, создание нового пользователя, если такого нет в БД
    def add_order(self):
        phone_number = self.__get_number()
        if Customer.get_customer(phone_number, self.online_store.db['customers']) is None:
            first_name = input("Введите фамилию покупателя: ")
            last_name = input("Введите имя покупателя: ")
            age = self.__get_age()
            if len(self.online_store.db['customers']) > 0:
                customer_id = self.online_store.db['customers'][-1]['customer_id'] + 1
            else:
                customer_id = 1
            customer = Customer(customer_id, first_name, last_name, age, phone_number)
            self.online_store.db['customers'].append(customer.to_json())
        else:
            customer = Customer.get_customer(phone_number, self.online_store.db['customers'])
        positions = []
        print("Введите список книг для покупки через '; ': ")
        books = input().split('; ')
        for book in books:
            for i in self.online_store.db['books']:
                if book == i['title']:
                    positions.append(i)
                    print(f"{i['title']}: {i['link']}")
                else:
                    print(f"К сожалению, книги '{book}' нет")
        if len(self.online_store.db['orders']) > 0:
            order_id = self.online_store.db['orders'][-1]['order_id'] + 1
        else:
            order_id = 1
        order = Order(order_id, customer['customer_id'], positions)
        self.online_store.db['orders'].append(order.to_json())
        self.online_store.db['revenue'] += order.get_purchase_amount()
        self.online_store.database.db_write(self.online_store.db)

    # Добавление новой книги
    def add_book(self):
        title = input("Введите название книги: ")
        if Book.get_book(title, self.online_store.db['books']) is None:
            author = input("Введите автора книги: ")
            year = self.__get_year()
            price = self.__get_price()
            link = input("Введите ссылку на книгу")
            if len(self.online_store.db['books']) > 0:
                book_id = self.online_store.db['books'][-1]['book_id']
            else:
                book_id = 1
            book = Book(book_id, title, author, year, price, link)
            self.online_store.db['books'].append(book.to_json())
            self.online_store.database.db_write(self.online_store.db)
        else:
            print("Такая книга уже есть")

    # Функция для ввода номера телефона с проверкой на корректность ввода
    def __get_number(self):
        try:
            phone_number = input("Введите номер телефона: ")
            if len(phone_number) > 0:
                if not ((phone_number[0] == '8' and len(phone_number) == 11) or (
                        phone_number[0] == '+' and phone_number[1] == '7') and len(phone_number) == 12):
                    raise LicenseError
                else:
                    if phone_number[0] == '+' and phone_number[1] == '7':
                        phone_number = '8' + phone_number[2:]
                    return phone_number
        except LicenseError:
            print("Неверный формат данных, попробуйте ещё раз!")
            return self.__get_number()

    # Функция для возраста
    def __get_age(self):
        try:
            age = int(input("Введите возраст покупателя: "))
            if (age <= 0) or (age > 120):
                raise LicenseError
            else:
                return age
        except LicenseError:
            print("Неверный формат данных, попробуйте ещё раз!")
            return self.__get_age()

    # Функция для ввода года
    def __get_year(self):
        try:
            year = int(input("Введите год издания книги: "))
            if (year <= 0) or (year > 2024):
                raise LicenseError
            else:
                return year
        except LicenseError:
            print("Неверный формат данных, попробуйте ещё раз!")
            return self.__get_year()

    # Функция для ввода цены
    def __get_price(self):
        try:
            price = int(input("Введите цену книги: "))
            if price <= 0:
                raise LicenseError
            else:
                return price
        except LicenseError:
            print("Неверный формат данных, попробуйте ещё раз!")
            return self.__get_price()

    # Получения списка заказов
    def list_orders(self):
        return self.online_store.db['orders']

    # Получения списка пользователей
    def list_customers(self):
        return self.online_store.db['customers']

    # Получения списка книг
    def list_books(self):
        return self.online_store.db['books']

    # Найти заказ по id
    def get_order(self, order_id: int):
        for i in range(len(self.online_store.db['orders'])):
            if self.online_store.db['orders'][i]['order_id'] == order_id:
                return Order(self.online_store.db['orders'][i]['order_id'],
                             self.online_store.db['orders'][i]['customer_id'],
                             self.online_store.db['orders'][i]['positions'])

    # Найти книгу по id
    def get_book(self, book_id: int):
        for i in range(len(self.online_store.db['books'])):
            if self.online_store.db['books'][i]['book_id'] == book_id:
                return Book(self.online_store.db['books'][i]['book_id'],
                            self.online_store.db['books'][i]['title'], self.online_store.db['books'][i]['author'],
                            self.online_store.db['books'][i]['year'], self.online_store.db['books'][i]['price'],
                            self.online_store.db['books'][i]['link'])

    # Изменить цену книги по id
    def update_book(self, book_id: int, price: int):
        for i in range(len(self.online_store.db['books'])):
            if self.online_store.db['books'][i]['book_id'] == book_id:
                self.online_store.db['books'][i]['price'] = price
                self.online_store.database.db_write(self.online_store.db)
                return

    # Удалить книгу
    def delete_book(self, book_id: int):
        for book in self.online_store.db['books']:
            if book['book_id'] == book_id:
                self.online_store.db['books'].remove(book)
                self.online_store.database.db_write(self.online_store.db)
                return

    # Изменить номер телефона пользователя по id
    def update_customers(self, customer_id: int, number: str):
        for i in range(len(self.online_store.db['customers'])):
            if self.online_store.db['customers'][i]['customer_id'] == customer_id:
                self.online_store.db['customers'][i]['number'] = number
                self.online_store.database.db_write(self.online_store.db)
                return

    # Получить выручку магазина
    def get_revenue(self):
        return self.online_store.db['revenue']

# Класс для обработки ошибок
class LicenseError(Exception):
    pass
