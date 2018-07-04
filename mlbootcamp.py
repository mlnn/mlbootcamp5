import pandas as pd

#из CSV-файла в объект pandas DataFram
df = pd.read_csv('../../data/mlbootcamp5_train.csv',
                 sep=';', index_col='id')

# df.head() #для просмотра первых 5 записей

# средний рост по различным значениям пола
df.groupby('gender')['height'].mean()
# gender
# 1    161.355612 - женщины
# 2    169.947895 - мужчины

# указание алкоголя реже у женщин
df.groupby('gender')['alco'].mean()
# gender
# 1    0.025500
# 2    0.106375

# курящих мужчин в 12 раз больше женщин
df[df['gender'] == 2]['smoke'].mean() / df[df['gender'] == 1]['smoke'].mean()

# возраст указан в днях. получить медианный возраст курящих в годах
df.groupby('smoke')['age'].median() / 365.25

# новый признак
df['age_years'] = (df['age'] / 365.25).round().astype('int')
# df['age_years'].max() - максимальный возраст 65

# отбор курящих мужчин
smoking_old_men = df[(df['gender'] == 2) & (df['age_years'] >= 60)
                    & (df['age_years'] < 65) & (df['smoke'] == 1)]

# выводы
smoking_old_men[(smoking_old_men['cholesterol'] == 1) &
               (smoking_old_men['ap_hi'] < 120)]['cardio'].mean()
smoking_old_men[(smoking_old_men['cholesterol'] == 3) &
               (smoking_old_men['ap_hi'] >= 160) &
               (smoking_old_men['ap_hi'] < 180)]['cardio'].mean()

# индекс массы тела
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df.groupby('gender')['BMI'].mean()
# gender
# 1    27.987583
# 2    26.754442

# чистка данных по перцентилям
filtered_df = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
print(filtered_df.shape[0] / df.shape[0])