import pandas as pd

# 1. Kaggle dataset - ben10_aliens.csv
ben10_df = pd.read_csv('data/ben10_aliens.csv')

print("Первые 5 строк ben10_aliens.csv:")
print(ben10_df.head())

print("\nИнформация о DataFrame:")
print(ben10_df.info())

print("\nСтатистическое описание:")
print(ben10_df.describe(include='all'))

# 2. Анализ средней зарплаты по городам
dz_df = pd.read_csv('data/dz.csv')

print("\nСтолбцы dz.csv:")
print(dz_df.columns)

# На случай, если названия колонок могут быть другие
# print(dz_df.head())

# Если Salary - числовой, а City - строковый (как обычно)
avg_salary_by_city = dz_df.groupby('City')['Salary'].mean()

print("\nСредняя зарплата по городам:")
print(avg_salary_by_city)
