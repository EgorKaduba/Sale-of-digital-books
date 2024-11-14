class Order:
    """
    Класс Заказ:

    order_id - айди заказа
    customer_id - айди покупателя
    positions - список книг в заказе
    """
    def __init__(self, order_id, customer_id: int, positions: list):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__positions = positions
        self.__purchase_amount = 0
        self.summ_order()

    # Функция, сериализующая данные для записи в файл
    def to_json(self):
        return {
            'order_id': self.__order_id,
            'customer': self.__customer_id,
            'positions': [book['book_id'] for book in self.__positions],
            'purchase_amount': self.__purchase_amount
        }

    # Подсчет суммы заказа
    def summ_order(self):
        for book in self.__positions:
            self.__purchase_amount += book['price']

    # Возвращает сумму заказа
    def get_purchase_amount(self):
        return self.__purchase_amount
