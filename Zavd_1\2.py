import pandas as pd

class DataLoader:
    """Клас для завантаження даних з файлу."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Завантажує CSV-файл у DataFrame."""
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"Файл {self.file_path} успішно завантажено! \n")
            return self.df
        except FileNotFoundError:
            print(f"Помилка: Файл {self.file_path} не знайдено.")
            return None

class DataInspector:
    """Клас для первинного аналізу структури та якості даних."""
    def __init__(self, df):
        self.df = df

    def primary_analysis(self):
        """Виконує Завдання 1: Первинний аналіз даних."""
        print("="*40)
        print("ЗАВДАННЯ 1: ПЕРВИННИЙ АНАЛІЗ")
        print("="*40)
        print("\n--- Перші 5 рядків ---")
        print(self.df.head())
        print("\n--- Останні 5 рядків ---")
        print(self.df.tail())
        print(f"\nКількість рядків і стовпців: {self.df.shape}")
        memory_kb = self.df.memory_usage(deep=True).sum() / 1024
        print(f"Обсяг пам'яті датасету: {memory_kb:.2f} KB\n")

    def structure_and_quality(self):
        """Виконує Завдання 2: Аналіз структури та типів даних."""
        print("="*40)
        print("ЗАВДАННЯ 2: АНАЛІЗ СТРУКТУРИ ТА ТИПІВ")
        print("="*40)
        print("\n--- Типи даних усіх стовпців ---")
        print(self.df.dtypes)
        
        missing = self.df.isnull().sum()
        total_missing = missing.sum()
        print("\n--- Кількість пропущених значень ---")
        print(missing)
        print(f"\nЗагальна кількість пропусків: {total_missing}")
        
        print("\n--- Висновок щодо якості даних ---")
        if total_missing == 0:
            print("Дані відзначаються високою якістю: пропущені значення (NaN) відсутні.")
            print("Однак усі стовпці мають текстовий тип (object), що в майбутньому")
            print("потребуватиме конвертації (наприклад, зарплати в числа, а дати у формат часу).")
        else:
            print("У датасеті виявлено пропущені значення, які потребують очищення або заповнення.")
