class DataTransformer:
    """Клас для створення нових стовпців та категоризації даних."""
    def __init__(self, df):
        self.df = df.copy()

    def _extract_salaries(self):
        """Приватний метод для витягування Min, Max та Avg зарплат."""
        self.df['Min_Salary'] = self.df['Salary Range'].str.replace('£', '').str.replace(',', '').str.split('-').str[0].astype(int)
        self.df['Max_Salary'] = self.df['Salary Range'].str.replace('£', '').str.replace(',', '').str.split('-').str[1].astype(int)
        self.df['Avg_Salary'] = (self.df['Min_Salary'] + self.df['Max_Salary']) / 2

    def categorize_salaries(self):
        """Виконує Завдання 6: Категоризація за допомогою apply()."""
        print("=" * 40)
        print("ЗАВДАННЯ 6: СТВОРЕННЯ НОВИХ ОЗНАК (apply)")
        print("=" * 40)
        
        # Спочатку готуємо числові стовпці з зарплатою
        self._extract_salaries()
        
        # Локальна функція для категоризації
        def get_category(salary):
            if salary <= 40000:
                return "Low"
            elif 40001 <= salary <= 70000:
                return "Medium"
            else:
                return "High"
        
        # Застосовуємо apply до максимальної зарплати
        self.df['Salary Category'] = self.df['Max_Salary'].apply(get_category)
        print("\nКатегоризацію успішно виконано!")
        print("Перевірка правильності (5 випадкових записів):")
        print(self.df[['Salary Range', 'Max_Salary', 'Salary Category']].sample(5))
        
        return self.df # Повертаємо оновлений датафрейм
