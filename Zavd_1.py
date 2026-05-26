import sqlite3
import pandas as pd
import re
import os

class DatabaseManager:
    """Клас для роботи з базою даних SQLite."""
    def __init__(self, db_name="jobs_database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        print(f"Підключено до БД: {self.db_name}")

    def load_data(self, df, table_name="jobs"):
        """Завантаження DataFrame у таблицю SQLite."""
        df.to_sql(table_name, self.conn, if_exists='replace', index=False)
        print(f"Дані успішно завантажено в таблицю '{table_name}'.")

    def execute_query(self, query):
        """Виконання SQL-запиту та повернення результату у вигляді DataFrame."""
        return pd.read_sql_query(query, self.conn)

    def close(self):
        """Закриття з'єднання."""
        if self.conn:
            self.conn.close()
            print("\nЗ'єднання з базою даних закрито (Завдання 7).")

class DataProcessor:
    """Клас для очищення та підготовки даних."""
    @staticmethod
    def prepare_data(df):
        # Функція для перетворення діапазону "£40,000 - £60,000" у число (середнє)
        def clean_salary(salary_str):
            if pd.isna(salary_str): return None
            # Видаляємо коми та £, шукаємо всі числа
            nums = re.findall(r'\d+', str(salary_str).replace(',', ''))
            if len(nums) >= 2:
                return (float(nums[0]) + float(nums[1])) / 2
            elif len(nums) == 1:
                return float(nums[0])
            return None

        # Функція для отримання верхньої межі зарплати
        def get_max_salary(salary_str):
            if pd.isna(salary_str): return None
            nums = re.findall(r'\d+', str(salary_str).replace(',', ''))
            return float(nums[-1]) if nums else None

        df['avg_salary'] = df['Salary Range'].apply(clean_salary)
        df['max_salary_limit'] = df['Salary Range'].apply(get_max_salary)
        
        # Перетворюємо дату в рядок для зручності пошуку через LIKE
        df['Date Posted'] = df['Date Posted'].astype(str)
        return df
