import sqlite3

def add_product(db, name: str, category: str, price: int):
    db.execute('''INSERT INTO products (name, category, price)
            VALUES(?, ?, ?);''', (name, category, price))
    db.commit()

def add_client(db, first_name: str, last_name: str, email: str):
    db.execute('''INSERT INTO customers (first_name, last_name, email)
            VALUES(?, ?, ?);''', (first_name, last_name, email))
    db.commit()

def make_order(db, customer_id: int, product_id: int, quantity: int):
    db.execute('''INSERT INTO orders (customer_id, product_id, quantity, order_date)
            VALUES(?, ?, ?, CURRENT_TIMESTAMP)''', (customer_id, product_id, quantity))
    db.commit()

def get_total_income(db):
    r = db.execute('''SELECT SUM(products.price*orders.quantity) AS total_price
            FROM orders
            INNER JOIN products ON orders.product_id = products.product_id
            ''')
    return r.fetchone()

def count_orders_by_customer_id(db):
    r = db.execute('''SELECT customers.first_name AS customer_name, COUNT(orders.order_id) AS amount_of_orders
            FROM orders
            INNER JOIN customers ON orders.customer_id = customers.customer_id
            GROUP BY customers.first_name
            ORDER BY customers.customer_id ASC
    ''')
    return r.fetchall()

def avg_check(db):
    r = db.execute('''SELECT AVG(products.price*orders.quantity) AS avg_price
            FROM orders
            INNER JOIN products ON orders.product_id = products.product_id
            ''')
    return r.fetchall()

def get_the_most_popular_category(db):
    r = db.execute('''SELECT products.category, COUNT(orders.order_id) AS order_count
        FROM products
        INNER JOIN orders ON products.product_id = orders.product_id
        GROUP BY products.category
        ORDER BY order_count DESC
        ''')
    return r.fetchall()

def get_amount_of_products_in_category(db):
    r = db.execute('''SELECT products.category, COUNT(products.product_id) as total
                FROM products
                GROUP BY products.category
				ORDER BY products.product_id ASC
                ''')
    return r.fetchone()

def update_smartpohe_prices(db):
    db.execute('''UPDATE products
        SET price = price * 1.1
        WHERE category = 'laptop''')
    db.commit()