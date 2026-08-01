# https://www.kaggle.com/datasets/muhammadbinimran/housing-price-prediction-data

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.info())

# Bar chart
# survival_count = df["Survived"].value_counts()
# plt.figure(figsize=(6,4))
# plt.bar(["Not Survived", "Survived"], survival_count)
# plt.title("Titanic Survival Count")
# plt.xlabel("Survival")
# plt.ylabel("Number of Passengers")
# plt.show() 

# Histogram 1
# plt.figure(figsize=(8,5))
# plt.hist(df["Age"].dropna(), bins=30)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Number of Passengers")
# plt.show()


# Histogram 2
# plt.figure(figsize=(8,5))
# plt.hist(df["Fare"], bins=20)

# plt.title("Fare Distribution")
# plt.xlabel("Fare")
# plt.ylabel("Number of Passengers")

# plt.show()


# Bar Chart 2 
# survival_by_class = df.groupby("Pclass")["Survived"].mean()

# plt.figure(figsize=(6,4))
# plt.bar(survival_by_class.index.astype(str), survival_by_class)

# plt.title("Survival Rate by Passenger Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Survival Rate")

# plt.show()


# Scatter Plot
# plt.figure(figsize=(8,6))
# plt.scatter(df["Age"], df["Fare"], color="purple")

# plt.title("Age vs Fare")
# plt.xlabel("Age")
# plt.ylabel("Fare")

# plt.show()


# Dual Histogram
survived = df[df["Survived"] == 1]["Age"].dropna()
not_survived = df[df["Survived"] == 0]["Age"].dropna()


plt.figure(figsize=(8,5))
plt.hist(survived, bins=20, alpha=0.7, label="Survived")
plt.hist(not_survived, bins=20, alpha=0.7, label="Not Survived")

plt.legend()

plt.title("Age Comparision")
plt.xlabel("Age")
plt.ylabel("Passengers")

plt.show()