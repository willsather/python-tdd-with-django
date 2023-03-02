import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from accuracy import accuracy
from save_figure import save_figure

# This example read from a local CSV file for simplicity,
# but your data source can come from anywhere.  As you scale,
# there exist tools to help manage large datasets
df = pd.read_csv("../penguins.csv")
df = df.dropna()

# X = Feature Data
X = df.drop(['species', 'year'], axis=1)

# Y = Target Data
y = df['species']

"""
Decision Trees (at least in Scikit Learn), do not support 
categorical data in a decision tree, so for our Penguin example,
the "sex" field must be One Hot Encoded to properly be trained.

One hot encoding replaces categorical data with binary, numerical data
like shown below:

| bill_length_mm | sex |
------------------------
|     125        | male|

turns into

| bill_length_mm | is_Male |
----------------------------
|     125        |    1    |

pandas has a built in One Hot Encoder called "get_dummies"
"""
X_encoded = pd.get_dummies(X, drop_first=True)

# Split up training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2)

# Create Decision Tree classifier object
model = DecisionTreeClassifier()

# Train Decision Tree Classifier
model = model.fit(X_train, y_train)

# Test accuracy when training model
accuracy(model, X_test, y_test)

# Save PNG visualization of decision tree
save_figure(model=model, feature_names=X_encoded.columns)

# Save model
joblib.dump(model, '../Predict_PenguinSpecies_DecisionTree_Model.sav')




