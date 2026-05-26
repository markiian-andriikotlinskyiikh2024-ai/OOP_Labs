if __name__ == "__main__":
    # Завдання 1: Завантаження даних
    loader = DataLoader('Job opportunities.csv')
    data = loader.load_data()

    if data is not None:
        # Завдання 1 та 2: Первинний аналіз
        inspector = DataInspector(data)
        inspector.primary_analysis()
        inspector.structure_and_quality()

        # Завдання 3: Фільтрація
        job_filter = DataFilter(data)
        job_filter.run_all_filters()

        # Завдання 4: Сортування
        sorter = DataSorter(data)
        top_5 = sorter.sort_and_get_top(5)
        sorter.print_highest_paying_positions(top_5)

        # Завдання 6: Трансформація даних (робиться перед 5, бо потрібні числові колонки)
        transformer = DataTransformer(data)
        processed_data = transformer.categorize_salaries()

        # Завдання 5: Групування та агрегація
        aggregator = DataAggregator(processed_data)
        aggregator.analyze_by_industry()

        # Завдання 7: Часовий аналіз
        time_analyzer = DataTimeAnalyzer(data)
        time_analyzer.process_dates()
        time_analyzer.analyze_yearly_trends()
