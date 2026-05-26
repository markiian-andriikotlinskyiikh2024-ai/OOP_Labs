class DataAggregator:
    """Клас для групування даних та розрахунку агрегатних метрик."""
    def __init__(self, df):
        self.df = df

    def analyze_by_industry(self):
        """Виконує Завдання 5: Аналіз по галузях."""
        print("\n" + "=" * 40)
        print("ЗАВДАННЯ 5: ГРУПУВАННЯ ТА АГРЕГАТНІ ФУНКЦІЇ")
        print("=" * 40)
        
        # Групуємо за галуззю та рахуємо метрики
        industry_stats = self.df.groupby('Industry').agg(
            Кількість_вакансій=('Job Title', 'count'),
            Середня_мін_зарплата=('Min_Salary', 'mean'),
            Середня_зарплата=('Avg_Salary', 'mean')
        )
        
        print("\n--- Загальна статистика по галузях (перші 5) ---")
        print(industry_stats.round(2).head())
        
        # Знаходимо галузь з найвищою середньою зарплатою
        top_industry = industry_stats.sort_values(by="Середня_зарплата", ascending=False).head(1)
        print("\n--- Галузь з найвищою середньою зарплатою ---")
        industry_name = top_industry.index[0]
        avg_sal = top_industry["Середня_зарплата"].values[0]
        print(f"Галузь: {industry_name} | Середня зарплата: £{avg_sal:,.2f}")
