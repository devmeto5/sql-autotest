import sqlite3
import unittest

class TestSQLDataExtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создание базы данных и таблицы на сервере
        cls.db_path = 'photofordv.db'  # Локальный путь к базе данных на сервере
        cls.connection = sqlite3.connect(cls.db_path)
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                city TEXT NOT NULL,
                country TEXT NOT NULL
            )
        ''')
        # Добавление тестовых данных
        cls.cursor.executemany('''
            INSERT INTO users (name, age, email, username, password, city, country) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', [
            ('Alice', 30, 'alice@example.com', 'alice123', 'password1', 'New York', 'USA'),
            ('Bob', 25, 'bob@example.com', 'bob123', 'password2', 'Los Angeles', 'USA'),
            ('Charlie', 35, 'charlie@example.com', 'charlie123', 'password3', 'Chicago', 'USA'),
            ('David', 28, 'david@example.com', 'david123', 'password4', 'Houston', 'USA'),
            ('Eve', 22, 'eve@example.com', 'eve123', 'password5', 'Phoenix', 'USA'),
            ('Frank', 31, 'frank@example.com', 'frank123', 'password6', 'Philadelphia', 'USA'),
            ('Grace', 29, 'grace@example.com', 'grace123', 'password7', 'San Antonio', 'USA'),
            ('Hank', 33, 'hank@example.com', 'hank123', 'password8', 'San Diego', 'USA'),
            ('Ivy', 27, 'ivy@example.com', 'ivy123', 'password9', 'Dallas', 'USA'),
            ('Jack', 26, 'jack@example.com', 'jack123', 'password10', 'San Jose', 'USA'),
            ('Karen', 32, 'karen@example.com', 'karen123', 'password11', 'Austin', 'USA'),
            ('Leo', 24, 'leo@example.com', 'leo123', 'password12', 'Jacksonville', 'USA'),
            ('Mia', 23, 'mia@example.com', 'mia123', 'password13', 'Fort Worth', 'USA'),
            ('Nick', 34, 'nick@example.com', 'nick123', 'password14', 'Columbus', 'USA'),
            ('Olivia', 30, 'olivia@example.com', 'olivia123', 'password15', 'Charlotte', 'USA'),
            ('Paul', 28, 'paul@example.com', 'paul123', 'password16', 'San Francisco', 'USA'),
            ('Quinn', 26, 'quinn@example.com', 'quinn123', 'password17', 'Indianapolis', 'USA'),
            ('Rachel', 31, 'rachel@example.com', 'rachel123', 'password18', 'Seattle', 'USA'),
            ('Sam', 25, 'sam@example.com', 'sam123', 'password19', 'Denver', 'USA'),
            ('Tina', 27, 'tina@example.com', 'tina123', 'password20', 'Washington', 'USA')
        ])
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        # Закрытие соединения с базой данных
        cls.connection.close()

    def test_extract_standard_data(self):
        # Выполнение SQL-запроса для извлечения данных
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()

        # Вывод всех данных из базы данных
        for row in rows:
            print(row)

        # Ожидаемые данные (первые три пользователя для проверки)
        expected_data = [
            (1, 'Alice', 30, 'alice@example.com', 'alice123', 'password1', 'New York', 'USA'),
            (2, 'Bob', 25, 'bob@example.com', 'bob123', 'password2', 'Los Angeles', 'USA'),
            (3, 'Charlie', 35, 'charlie@example.com', 'charlie123', 'password3', 'Chicago', 'USA')
        ]

        # Проверка соответствия извлеченных данных ожидаемым
        self.assertEqual(rows[:3], expected_data)

if __name__ == '__main__':
    unittest.main()