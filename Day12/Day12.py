# KNN Algorithm

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("titanic.csv")
# print(df.head())

# x = df[["Pclass", "Age", "Fare"]]
# y = df["Survived"]

# x["Age"] = x["Age"].fillna(x["Age"].mean())

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model = KNeighborsClassifier(n_neighbors=5)

# model.fit(x_train, y_train)

# predictions = model.predict(x_test)
# print(f"Predictions: {predictions}")

# accuracy = accuracy_score(y_test, predictions)
# print('Accuracy', accuracy)


# Random Forest Algorithm
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("titanic.csv")
# print(df.head())

# x = df[["Pclass", "Age", "Fare"]]
# y = df["Survived"]

# x["Age"] = x["Age"].fillna(x["Age"].mean())

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model = RandomForestClassifier(n_estimators=100, random_state=42)

# model.fit(x_train, y_train)

# predictions = model.predict(x_test)
# print(f"Predictions: {predictions}")

# accuracy = accuracy_score(y_test, predictions)
# print('Accuracy', accuracy)


# Support Vector Machine
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC 
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("titanic.csv")

# x = df[["Pclass", "Age", "Fare"]]
# y = df["Survived"]

# x["Age"] = x["Age"].fillna(x["Age"].mean())

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# scalar = StandardScaler()
# x_train = scalar.fit_transform(x_train)
# x_test = scalar.fit_transform(x_test)

# model = SVC()
# model.fit(x_train, y_train)

# predictions = model.predict(x_test)
# print(f"Predictions: {predictions}")

# accuracy = accuracy_score(y_test, predictions)
# print('Accuracy', accuracy)


# Navive Bayes Algorithm
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("titanic.csv")
# print(df.head())

# x = df[["Pclass", "Age", "Fare"]]
# y = df["Survived"]

# x["Age"] = x["Age"].fillna(x["Age"].mean())

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model = GaussianNB()

# model.fit(x_train, y_train)

# predictions = model.predict(x_test)
# print(f"Predictions: {predictions}")

# accuracy = accuracy_score(y_test, predictions)
# print('Accuracy', accuracy)


# Gradient Boosting Algorithm
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("titanic.csv")
print(df.head())

x = df[["Pclass", "Age", "Fare"]]
y = df["Survived"]

x["Age"] = x["Age"].fillna(x["Age"].mean())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = GradientBoostingClassifier(random_state=42)

model.fit(x_train, y_train)

predictions = model.predict(x_test)
print(f"Predictions: {predictions}")

accuracy = accuracy_score(y_test, predictions)
print('Accuracy', accuracy)


# Homework
# 1. 