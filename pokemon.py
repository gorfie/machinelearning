import pandas as pd

df = pd.read_csv('pokemon_data.csv')
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df['Total'] = df.iloc[:,4:10].sum(axis=1)

df.sort_values(['Name', 'HP'], ascending=[1,0])

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

df.to_csv('poke_data.csv', index=False)

df = pd.read_csv('poke_data.csv')
df = df.loc[df['Name'].str.contains('Mega')]
new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
df.reset_index(drop=True, inplace=True)