from Database import Database


class OnlineStore:
    """
    Класс Магазина продажи цифровых книг:

    path - путь к базе данных
    """
    def __init__(self, path):
        self.database = Database(path)  # Подключение к базе данных
        self.db = self.database.db_read()  # Получение данных из БД
        self._name = self.db['name']
        self._link = self.db['link']
        self._revenue = self.db['revenue']
