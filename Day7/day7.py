import pandas as pd

df = pd.read_csv('netflix_full.csv')

# print(df.head())
# print(df.dtypes)

# print(df.iloc[3])
# print(df.iloc[10:20])
# print(df.iloc[-5])

# movies = df[df["year"] > 2020]
# print(movies[movies["year"] < 2022])

# print(df[df["rating"] == "TV-MA"])
# print(df[(df["year"] > 2020) & (df["time"] == "110 min")])

# print(df.sort_values('year'))
# print(df.sort_values('year', ascending=False))

# print(df.dropna())
# print(df.fillna("Unknown"))


print(df.rename(columns={'describle': 'description'}))
x = df['Age'] = 2026 - df['year']
print(x)

df.loc[df["rating"] == 'TV-MA', 'rating'] = 'Mature'
print(df.iloc[0:10]["rating"])

print(df["rating"].unique())
print(df['rating'].nunique())
print(df['rating'].value_counts())

print(df['year'].max())
print(df['year'].min())
print(df['year'].mean())
print(df['year'].median())

print(df.groupby('rating').size())
print(df.groupby('type')['year'].mean())
print(df.groupby('type')['year'].min())

print(df[df['name'].str.contains("Love", case=False)])
print(df['name'].str.upper())
print(df['name'].str.lower())
print(df['name'].str.len())

def decade(x):
    return (x // 10) * 10 

df["Decade"] = df['year'].apply(decade)
print(df)

# df.to_excel("netflix_excel_file.xlsx", index=False)

print(df.groupby(['type', 'rating']).size())

print(df[df['type'] == 'Movie'].sort_values('year', ascending=False).head(10))

# Homework
# 1. Find Top 10 countries producing content 
# 2. Find Highest Rated categories 