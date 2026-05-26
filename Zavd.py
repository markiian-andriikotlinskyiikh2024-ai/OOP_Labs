import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# 1. Підготовка середовища та завантаження даних
class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_and_prepare(self):
        self.df = pd.read_csv(self.filepath)
        # Створення числової колонки Average Salary
        self.df['Average Salary'] = self.df['Salary Range'].apply(self._parse_salary)
        # Підготовка колонки року з Date Posted
        self.df['Date Posted'] = pd.to_datetime(self.df['Date Posted'], errors='coerce')
        self.df['Year'] = self.df['Date Posted'].dt.year
        return self.df

    def _parse_salary(self, salary_str):
        if pd.isna(salary_str):
            return np.nan
        numbers = re.findall(r'\d+,\d+|\d+', str(salary_str))
        numbers = [int(n.replace(',', '')) for n in numbers]
        if len(numbers) == 2:
            return sum(numbers) / 2
        elif len(numbers) == 1:
            return numbers[0]
        return np.nan

# Візуалізація даних згідно зі стилем методички
class Visualizer:
    def __init__(self, df):
        self.df = df

    # 2. Створення стовпчастої діаграми (Barplot)
    def plot_barplot(self):
        plt.figure(figsize=(10, 6))
        order = ['Internship', 'Entry-Level', 'Junior', 'Mid-Level', 'Senior', 'Executive']
        order = [o for o in order if o in self.df['Experience Level'].unique()]
        
        sns.barplot(data=self.df, x='Experience Level', y='Average Salary', order=order, palette='viridis')
        plt.title('Середня зарплата залежно від рівня досвіду')
        plt.xlabel('Рівень досвіду')
        plt.ylabel('Середня зарплата')
        plt.show()

    # 3. Створення діаграми розмаху (Boxplot)
    def plot_boxplot(self):
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.df, x='Industry', y='Average Salary', palette='Set2')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.title('Розподіл зарплат за галузями')
        plt.xlabel('Галузь')
        plt.ylabel('Середня зарплата')
        plt.show()

    # 4. Створення теплової карти (Heatmap)
    def plot_heatmap(self):
        plt.figure(figsize=(12, 6))
        pivot_table = pd.crosstab(self.df['Experience Level'], self.df['Industry'])
        sns.heatmap(pivot_table, annot=True, cmap='viridis', linewidths=0.5)
        plt.title('Кількість вакансій за рівнем досвіду та галуззю')
        plt.tight_layout()
        plt.show()

    # 5. Створення точкової діаграми (Scatterplot)
    def plot_scatterplot(self):
        plt.figure(figsize=(10, 6))
        # Використано palette='deep' та alpha=0.7
        sns.scatterplot(data=self.df, x='Year', y='Average Salary', hue='Experience Level', 
                        palette='deep', alpha=0.7, s=70)
        plt.title('Залежність середньої зарплати від року публікації')
        plt.xlabel('Рік')
        plt.ylabel('Середня зарплата')
        # Винесення легенди за межі графіка
        plt.legend(title='Рівень досвіду', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

    # 6. Парні графіки (Pairplot)
    def plot_pairplot(self):
        # Використано diag_kind='kde' та palette='bright'
        sns.pairplot(self.df[['Average Salary', 'Year', 'Experience Level']], 
                     hue='Experience Level', diag_kind='kde', palette='bright')
        plt.suptitle('Парні графіки: Зарплата, Рік та Досвід', y=1.02)
        plt.show()

# -- Головний блок виконання коду
if __name__ == "__main__":
    processor = DataProcessor("Job opportunities.csv")
    df_cleaned = processor.load_and_prepare()
    
    vis = Visualizer(df_cleaned)
    vis.plot_barplot()
    vis.plot_boxplot()
    vis.plot_heatmap()
    vis.plot_scatterplot()
    vis.plot_pairplot()
