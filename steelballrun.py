import sqlite3

connect = sqlite3.connect("fruits.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS fruits(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER
    )             
""")

def add_fruit():
    name = input("Название фрукта: ")
    price = float(input("Цена за килограм: "))
    quantity = int(input("Количество на складе(в кг): "))

    cursor.execute(""" INSERT INTO fruits
                   (name, price, quantity)
                   VALUES (?, ?, ?)""", (name, price, quantity))
    
    connect.commit()

# def add_fruit(name, price, quantity):
#     cursor.execute(""" INSERT INTO fruits
#                    (name, price, quantity)
#                    VALUES (?, ?, ?)""", (name, price, quantity))
    
#     connect.commit()

# add_fruit('Яблоко', 80, 20)
# add_fruit('Рокакака', 600000, 1.2)
    
add_fruit()