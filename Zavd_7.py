class DataTimeAnalyzer:
    """Клас для обробки дат та аналізу часових трендів."""
    def __init__(self, df):
        self.df = df.copy()

    def process_dates(self):
        """Перетворює колонку дат та створює колонку Year."""
        print("-" * 40)
        print("ЗАВДАННЯ 7: ЧАСОВИЙ АНАЛІЗ РИНКУ ВАКАНСІЙ")
        print("-" * 40)
        
        self.df['Date Posted'] = pd.to_datetime(self.df['Date Posted'])
        self.df['Year'] = self.df['Date Posted'].dt.year
        
        print("\nКолонку 'Date Posted' перетворено у формат datetime.")
        print("Нову колонку 'Year' успішно створено!")
        print("\nПеревірка (3 випадкові записи):")
        print(self.df[['Date Posted', 'Year']].sample(3))

    def analyze_yearly_trends(self):
        """Групує дані за роком та знаходить найактивніший рік."""
        print("\n--- Динаміка кількості вакансій за роками ---")
        
        yearly_stats = self.df.groupby('Year').agg(
            Кількість_вакансій=('Job Title', 'count')
        )
        print(yearly_stats)
        
        top_year = yearly_stats.sort_values(by="Кількість_вакансій", ascending=False).index[0]
        max_vacancies = yearly_stats["Кількість_вакансій"].max()
        
        print(f"\nНайбільш активним був {top_year} рік. Відкрито вакансій: {max_vacancies}")
