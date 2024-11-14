import os
import json


class Database:
    """
    Класс БД:

    path - путь к файлу БД
    """
    def __init__(self, path: str):
        if os.path.isfile(path):  # Проверка файла на существование
            self.__path = path
            self.__extension = self.__path.split('.')[-1]  # Расширение файла

    # Чтение данных из файла
    def db_read(self):
        if self.__extension == 'json':
            with open(self.__path, 'r') as file:
                return json.load(file)

    # Запись данных в файл
    def db_write(self, data: dict):
        if self.__extension == 'json':
            with open(self.__path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=3)