import pandas as pd



df = pd.read_csv('sample_data\california_housing_train.csv')

df2 = df[df['population'] == df['population'].min()]

print(df2['households'].max())