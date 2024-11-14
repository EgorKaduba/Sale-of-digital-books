class Customer:
    """
    Класс Пользователя:

    customer_id - id пользователя
    first_name - фамилия
    last_name - имя
    age - возраст
    phone_number - номер телефона
    """
    def __init__(self, customer_id, first_name: str, last_name: str, age: int, phone_number: str):
        self.__id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._phone_number = phone_number

    # Найти пользователя по номеру телефона
    @staticmethod
    def get_customer(phone_number: str, customers: list):
        for customer in customers:
            if customer['phone_number'] == phone_number:
                return customer
        return None

    # Функция, сериализующая данные для записи в файл
    def to_json(self):
        return {
            'customer_id': self.__id,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'age': self._age,
            'phone_number': self._phone_number
        }
