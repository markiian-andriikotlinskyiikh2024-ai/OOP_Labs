class JobAnalyzer:
    """Клас для виконання аналітичних завдань."""
    def __init__(self, db_manager):
        self.db = db_manager

    def task_2_basic_queries(self):
        print("\n=== Завдання 2. Основні запити ===")
        print("\n1. Перші 10 вакансій:")
        print(self.db.execute_query("SELECT * FROM jobs LIMIT 10"))
        
        print("\n2. Вакансії з вимогою SQL:")
        print(self.db.execute_query("SELECT * FROM jobs WHERE `Required Skills` LIKE '%SQL%'"))
        
        print("\n3. Унікальні Location та Company (перші 10):")
        print(self.db.execute_query("SELECT DISTINCT Location, Company FROM jobs LIMIT 10"))

    def task_3_analytical_queries(self):
        print("\n=== Завдання 3. Аналітичні запити ===")
        print("\n1. Середня зарплата для кожного рівня досвіду:")
        print(self.db.execute_query("""
            SELECT `Experience Level`, AVG(avg_salary) as AvgSalary 
            FROM jobs 
            GROUP BY `Experience Level`
        """))

        print("\n2. Кількість вакансій для кожного рівня досвіду:")
        print(self.db.execute_query("""
            SELECT `Experience Level`, COUNT(*) as Count 
            FROM jobs 
            GROUP BY `Experience Level`
        """))

        print("\n3. Мінімальна та максимальна зарплата серед усіх вакансій:")
        print(self.db.execute_query("""
            SELECT MIN(avg_salary) as MinSal, MAX(avg_salary) as MaxSal 
            FROM jobs
        """))

    def task_4_aggregate_functions(self):
        print("\n=== Завдання 4. Агрегатні функції ===")
        print("\n1. Кількість вакансій в індустріях (зарплата > £50,000):")
        print(self.db.execute_query("""
            SELECT Industry, COUNT(*) as Count 
            FROM jobs 
            WHERE avg_salary > 50000 
            GROUP BY Industry
        """))

        print("\n2. Середня зарплата для кожної індустрії (перші 10):")
        print(self.db.execute_query("""
            SELECT Industry, AVG(avg_salary) as AvgSal 
            FROM jobs 
            GROUP BY Industry 
            LIMIT 10
        """))

    def task_5_complex_queries(self):
        print("\n=== Завдання 5. Складніші запити ===")
        print("\n1. Кількість вакансій за Location та Experience Level (перші 10):")
        print(self.db.execute_query("""
            SELECT Location, `Experience Level`, COUNT(*) as Count 
            FROM jobs 
            GROUP BY Location, `Experience Level` 
            LIMIT 10
        """))

        print("\n2. Кількість вакансій за Industry та Job Type:")
        print(self.db.execute_query("""
            SELECT Industry, `Job Type`, COUNT(*) as Count 
            FROM jobs 
            GROUP BY Industry, `Job Type` 
            LIMIT 10
        """))

        print("\n3. Середня зарплата за Location та Experience Level:")
        print(self.db.execute_query("""
            SELECT Location, `Experience Level`, AVG(avg_salary) as AvgSal 
            FROM jobs 
            GROUP BY Location, `Experience Level` 
            LIMIT 10
        """))

    def task_6_additional_queries(self):
        print("\n=== Завдання 6. Додаткові запити ===")
        print("\n1. 5 вакансій з найвищою верхньою межею зарплати:")
        print(self.db.execute_query("""
            SELECT `Job Title`, Company, max_salary_limit 
            FROM jobs 
            ORDER BY max_salary_limit DESC 
            LIMIT 5
        """))

        print("\n2. Підрахунок кількості вакансій для кожної навички (Top 10):")
        # Тут використовуємо Pandas, бо в SQL складно розбивати рядки через кому
        df_skills = self.db.execute_query("SELECT `Required Skills` FROM jobs")
        skills_series = df_skills['Required Skills'].str.split(',').explode().str.strip()
        print(skills_series.value_counts().head(10))

        print("\n3. Компанії з найбільшою кількістю вакансій у 2023 році:")
        print(self.db.execute_query("""
            SELECT Company, COUNT(*) as VacancyCount 
            FROM jobs 
            WHERE `Date Posted` LIKE '%2023%' 
            GROUP BY Company 
            ORDER BY VacancyCount DESC 
            LIMIT 5
        """))
