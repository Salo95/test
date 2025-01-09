import sqlite3

connect = sqlite3.connect('employeess.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        position TEXT,
        salary REAL,
        hire_date DATE  
    )
''')

def add():
    name = input('Введите имя сотрудника: ')
    age = int(input('Введите возраст сотрудника: '))
    department = input('Назовите отдел, в котором работает сотрудник: ')
    position = input('Назовите должность сотрудника: ')
    salary = int(input('Введите зарплату сотрудника: '))
    hire_date = input('Введите дату приема на работу: ')

    cursor.execute(''' INSERT INTO employees
                   (name, age, department, position, salary, hire_date)
                   VALUES (?, ?, ?, ?, ?, ?)''', (name, age, department, position, salary, hire_date))
    
    connect.commit()

# add()

def show_with_department(department):
    cursor.execute('SELECT * FROM employees WHERE department = ?', (department,))
    employeess = cursor.fetchall()
    print(employeess)

# show_with_department('self')

def show_with_salary(salary):
    cursor.execute('SELECT * FROM employees WHERE salary > ?', (salary,))
    employeess = cursor.fetchall()
    print(employeess)

# show_with_salary(50000)

def count():
    cursor.execute('SELECT name FROM employees')
    names = cursor.fetchall()
    quant = len(names)
    print(quant)

# count()

def update_data(name, new_position, new_salary):
    cursor.execute("SELECT * FROM employees WHERE name = ?", (name,))
    employee = cursor.fetchone()
    cursor.execute("UPDATE employees SET position = ? WHERE name = ?", (new_position, name))
    cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (new_salary, name))
    connect.commit()
    print(f'Данные сотрудника {name} были успешно обновлена')

# update_data('Joseph', 'guide', 30000)

def fire_by_date():
    cursor.execute("SELECT * FROM employees ORDER BY hire_date ASC LIMIT 1")
    oldest = cursor.fetchone()
    if oldest:
        cursor.execute("DELETE FROM employees WHERE name = ?", (oldest[1],))
        connect.commit()
        print(f"Сотрудник {oldest[1]} был(а) успешно уволен(а)")
    else:
        pass

# fire_by_date()

connect.close()