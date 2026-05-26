class DataFilter:
    """Клас для відбору вакансій за різними критеріями."""
    def __init__(self, df):
        self.df = df

    def filter_industry(self, industry="Cloud Computing"):
        print(f"\n--- Вакансії у сфері {industry} ---")
        filtered = self.df[self.df['Industry'] == industry]
        print(f"Знайдено: {len(filtered)}")
        print(filtered[['Job Title', 'Company', 'Location']].head(3))

    def filter_senior_level(self):
        print("\n--- Вакансії з рівнем Senior ---")
        filtered = self.df[self.df['Experience Level'] == 'Senior']
        print(f"Знайдено: {len(filtered)}")
        print(filtered[['Job Title', 'Salary Range']].head(3))

    def filter_fulltime_city(self, city="London"):
        print(f"\n--- Вакансії Full-Time у місті {city} ---")
        filtered = self.df[(self.df['Job Type'] == 'Full-Time') & (self.df['Location'] == city)]
        print(f"Знайдено: {len(filtered)}")
        print(filtered[['Job Title', 'Company']].head(3))

    def run_all_filters(self):
        """Метод, який запускає всі фільтри по черзі."""
        print("-" * 40)
        print("ЗАВДАННЯ 3: ФІЛЬТРАЦІЯ")
        print("-" * 40)
        self.filter_industry()
        self.filter_senior_level()
        self.filter_fulltime_city()
