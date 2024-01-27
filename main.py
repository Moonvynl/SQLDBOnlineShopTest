
import sqlite3
import crud

db = sqlite3.connect("shop.db")

db.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);
''')

db.execute('''CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE );''')

db.execute('''CREATE TABLE IF NOT EXISTS orders ( 
        order_id INTEGER PRIMARY KEY, 
        customer_id INT NOT NULL, 
        product_id INTEGER NOT NULL, 
        quantity INTEGER NOT NULL, 
        order_date DATE NOT NULL, 
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
        FOREIGN KEY (product_id) REFERENCES products(product_id) );''')

while True:
        print('''
Що ви хочете зробити?

1 - Додавання продуктів:
2 - Додавання клієнтів:
3 - Замовлення товарів:
4 - Сумарний обсяг продажів:
5 - Кількість замовлень на кожного клієнта:
6 - Середній чек замовлення:
7 - Найбільш популярна категорія товарів:
8 - Загальна кількість товарів кожної категорії:
9 - Оновлення цін категорії на 10% більші:
10 - Показати усіх користувачів
11 - Показати усі продукти
12 - Показати усі замовлення(Joined)
0 - Вийти:

        ''')
        command = int(input("Оберіть ваші дії: "))
        if command == 1:
            name = input("CX")
            category = input("XB")
            price = int(input("F"))
            crud.add_product(db, name, category, price)

        if command == 2:
            first_name = input("f")
            last_name = input("a")
            email = input("p")
            crud.add_client(db, first_name, last_name, email)

        if command == 3:
            customer_id = int(input(""))
            product_id = int(input(""))
            quantity = int(input(""))
            crud.make_order(db, customer_id, product_id, quantity)

        if command == 4:
            print(crud.get_total_income(db))

        if command == 5:
            print(crud.count_orders_by_customer_id(db))

        if command == 6:
            print(crud.avg_check(db))

        if command == 7:
            print(crud.get_the_most_popular_category(db))

        if command == 8:
            print(crud.get_amount_of_products_in_category(db))

        if command == 9:
            crud.update_smartpohe_prices(db)
