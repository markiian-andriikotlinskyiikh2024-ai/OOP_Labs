# Основна частина програми
if __name__ == "__main__":
    file_name = 'Job opportunities.csv'
    
    if os.path.exists(file_name):
        # 1. Підготовка
        raw_df = pd.read_csv(file_name)
        processed_df = DataProcessor.prepare_data(raw_df)
        
        db = DatabaseManager()
        db.load_data(processed_df)
        
        # 2-6. Аналіз
        analyzer = JobAnalyzer(db)
        analyzer.task_2_basic_queries()
        analyzer.task_3_analytical_queries()
        analyzer.task_4_aggregate_functions()
        analyzer.task_5_complex_queries()
        analyzer.task_6_additional_queries()
        
        # 7. Закриття
        db.close()
    else:
        print(f"Файл {file_name} не знайдено.")
