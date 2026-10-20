import pandas as pd

df = pd.read_csv('data/treningsdata.csv', sep=',')
df.columns = ['lengde', 'puls', 'makspuls', 'kalorier']
print(df.describe())
