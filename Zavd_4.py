class DataSorter:
    """Клас для перетворення зарплати та сортування вакансій."""
    def __init__(self, df):
        self.df = df.copy() # Робимо копію таблиці, щоб не пошкодити оригінал
        self._prepare_salaries() # Автоматично готуємо зарплати при створенні об'єкта

    def _prepare_salaries(self):
        """Приватний метод для витягування максимальної зарплати з тексту."""
        self.df['Max_Salary'] = self.df['Salary Range'].str.replace('£', '').str.replace(',', '').str.split('-').str[1].astype(int)

    def sort_and_get_top(self, top_n=5):
        """Сортує вакансії та повертає топ."""
        print("=" * 40)
        print("ЗАВДАННЯ 4: СОРТУВАННЯ ЗА ЗАРПЛАТОЮ")
        print("=" * 40)
        sorted_df = self.df.sort_values(by='Max_Salary', ascending=False)
        top_jobs = sorted_df.head(top_n)
        print(f"\nТоп-{top_n} вакансій з найвищою зарплатою")
        print(top_jobs[['Job Title', 'Company', 'Salary Range']])
        return top_jobs

    def print_highest_paying_positions(self, top_jobs_df):
        """Виводить унікальні назви найбільш високооплачуваних посад."""
        print("\nНайбільш високооплачувані посади:")
        unique_titles = top_jobs_df['Job Title'].unique()
        for title in unique_titles:
            print(f"- {title}")
