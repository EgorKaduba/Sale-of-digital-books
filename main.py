import config
from Manager import Manager


# Функция, выступающая в роли консоли приложения
def console(mng: Manager):
    while True:
        print('-----------------------------------------------')
        print("Выберите действие:\n1 - Добавить книгу\t2 - Сделать заказ"
              "\n3 - Вывести список заказов\t4 - Вывести список покупателей"
              "\n5 - Вывести список книг\t6 - Найти заказ по id"
              "\n7 - Найти книгу по id\t8 - Обновить цену на книгу по id"
              "\n9 - Удалить книгу по id\t10 - Обновить номер телефона пользователя по id"
              "\n11 - Вывести выручку магазина\t12 - Выход")
        choice = int(input("Введите Ваш выбор: "))
        if choice == 1:
            mng.add_book()
        elif choice == 2:
            mng.add_order()
        elif choice == 3:
            orders = mng.list_orders()
            print(orders)
        elif choice == 4:
            customers = mng.list_customers()
            print(customers)
        elif choice == 5:
            books = mng.list_books()
            print(books)
        elif choice == 6:
            order_id = int(input("Введите id заказа: "))
            order = mng.get_order(order_id)
            print(order)
        elif choice == 7:
            book_id = int(input("Введите id книги: "))
            book = mng.get_book(book_id)
            print(book)
        elif choice == 8:
            book_id = int(input("Введите id книги: "))
            new_price = int(input("Введите новую цену: "))
            mng.update_book(book_id, new_price)
        elif choice == 9:
            book_id = int(input("Введите id книги: "))
            mng.delete_book(book_id)
        elif choice == 10:
            customer_id = int(input("Введите id пользователя: "))
            new_number = input("Введите новый номер телефона: ")
            mng.update_customers(customer_id, new_number)
        elif choice == 11:
            revenue = mng.get_revenue()
            print(revenue)
        elif choice == 12:
            break
        print('-----------------------------------------------')


if __name__ == '__main__':
    manager = Manager(config.PATH)  # Менеджер магазина
    console(manager)