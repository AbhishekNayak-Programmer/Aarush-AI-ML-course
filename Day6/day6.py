import pandas as pd

df = pd.read_csv('netflix_full.csv')

# print(df.head())
# print(df.dtypes)

print(df.iloc[3])
print(df.iloc[10:20])
print(df.iloc[-5])

movies = df[df["year"] > 2020]
print(movies[movies["year"] < 2022])

print(df[df["rating"] == "TV-MA"])
print(df[(df["year"] > 2020) & (df["time"] == "110 min")])

print(df.sort_values('year'))
print(df.sort_values('year', ascending=False))

print(df.dropna())
print(df.fillna("Unknown"))