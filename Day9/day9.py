# Predict whether a Netflix title is a movie or a series using year and ratings column

# Importing Steps
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('netflix_full.csv')
# print(df.head())

# Formating steps
data = df[["year", 'rating', 'type']].dropna()

# Change & Divide the Data into differnt formats 
rating_encoder = LabelEncoder()
type_encoder = LabelEncoder()

data["rating"] = rating_encoder.fit_transform(data["rating"])
data["type"] = type_encoder.fit_transform(data["type"])

X = data[["year", 'rating']]
y = data["type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creation of Model 
model = DecisionTreeClassifier(random_state=42)

# Training the Model
model.fit(X_train, y_train)

# Prediction Stage 
predictions = model.predict(X_test)

# Accuracy testing 
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy ", accuracy)