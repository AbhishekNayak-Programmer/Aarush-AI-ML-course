import pandas as pd

df = pd.read_csv("data.csv")
# print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df["Age"])
print(df[["Passengerid", "Age", "Fare"]])

print(df.head(10))
print(df.tail(10))

print(df["Age"] > 25)
survived = df["2urvived"] == 1
print(survived.value_counts())

sorted_fares = df.sort_values(
    by="Fare",
    ascending=False
)["Fare"]

print(sorted_fares)

print(df.groupby("Sex")["2urvived"].mean())