import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
file_path = '/Users/olegelizarov/PycharmProjects/AZ02/student-scores.csv'
df = pd.read_csv(file_path)

# Вывод первых нескольких строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# Вывод списка всех столбцов в DataFrame
print("\nСписок всех столбцов в DataFrame:")
print(df.columns)

# Обновленный список столбцов с оценками
score_columns = ['math_score', 'history_score', 'geography_score', 'english_score', 'biology_score']
scores_df = df[score_columns]

# Вычисление средней оценки по каждому предмету
mean_scores = scores_df.mean()
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = scores_df.median()
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = scores_df['math_score'].quantile(0.25)
Q3_math = scores_df['math_score'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nQ1, Q3 и IQR для оценок по математике:")
print(f"Q1 (25-й перцентиль): {Q1_math}")
print(f"Q3 (75-й перцентиль): {Q3_math}")
print(f"IQR: {IQR_math}")

# Вычисление стандартного отклонения
std_deviation = scores_df.std()
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)

# Сохранение результатов основного анализа в новый CSV файл
results = pd.DataFrame({
    'Средняя оценка': mean_scores,
    'Медианная оценка': median_scores,
    'Стандартное отклонение': std_deviation
})
results['Q1 (Математика)'] = Q1_math
results['Q3 (Математика)'] = Q3_math
results['IQR (Математика)'] = IQR_math

output_path_main = '/Users/olegelizarov/PycharmProjects/AZ02/analysis_results.csv'
results.to_csv(output_path_main, index=True)
print(f"\nРезультаты основного анализа сохранены в файл '{output_path_main}'.")

# Дополнительные методы анализа

