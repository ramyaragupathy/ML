import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# load the dataset
data = pd.read_csv('melb_data.csv')
# print(data.isnull().any())
data = data.fillna(0)

# summary statistics of all columns
# 8 fields: count, mean, std, min, 25%, 50%, 75%, max
# print(data.describe())
# print(data.head)
# print all columns in the dataset
# print(data.columns)
# # size of dataset
# print(data.shape)

# store the series of years as a separate variable
data_price = data.Price

# returns the top few lines of data
# print(data_price.head())

# selecting multiple columns
select_columns = ['Price', 'BuildingArea']
two_columns_data = data[select_columns]
# print(two_columns_data)

y = data_price
data_predictors = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = data[data_predictors]

# split data into training and validation data, for both predictors and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
data_model = DecisionTreeRegressor()
data_model.fit(train_X, train_y)
# print("Making predictions for the following 5 houses:")
# print(X.head())
# print("The predictions are")
# print(data_model.predict(X.head()))

predicted_home_prices = data_model.predict(X)
print('IN_SAMPLE SCORE ', mean_absolute_error(y, predicted_home_prices))

# get predicted prices on validation data
val_predictions = data_model.predict(val_X)
print('VALIDATION DATA ', mean_absolute_error(val_y, val_predictions))
