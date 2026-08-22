# /////////////////////////////////////////////////////////
# Linear Regression Model for House Price Prediction
# /////////////////////////////////////////////////////////

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error


# df = pd.read_csv('train.csv')

# x = df[['GrLivArea', "BedroomAbvGr", 'FullBath']]
# y = df['SalePrice']


# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(x_train, y_train)

# predictions = model.predict(x_test)

# error = mean_absolute_error(y_test, predictions)

# print(f'Mean Absolute Error: {error}')

# new_house = [[2000, 3, 2]]
# price = model.predict(new_house)

# print("Predicted price for the new house: ", price[0])


# /////////////////////////////////////////////////////////
# Random Forest Regression Model for House Price Prediction
# /////////////////////////////////////////////////////////
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error

# df = pd.read_csv('train.csv')
# x = df[['GrLivArea', "BedroomAbvGr", 'FullBath']]
# y = df['SalePrice']

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(x_train, y_train)

# predictions = model.predict(x_test)

# error = mean_absolute_error(y_test, predictions)

# print(f'Mean Absolute Error: {error}')

# new_house = [[2000, 3, 2]]
# price = model.predict(new_house)

# print("Predicted price for the new house: ", price[0])



# /////////////////////////////////////////////////////////
# K Means Clustering for Mall Customer Segmentation
# /////////////////////////////////////////////////////////
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('Mall_Customers.csv')

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

model = KMeans(n_clusters=5, random_state=42, n_init=10)
model.fit(X)

df["Groups"] = model.labels_

print(df[['CustomerID', 'Annual Income (k$)', 'Spending Score (1-100)', 'Groups']].head(20))