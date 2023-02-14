import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

from accuracy import accuracy
from save_figure import save_figure

df = pd.read_csv("./penguins.csv")
df = df.dropna()

# X = Feature Data
X = df.drop(['species', 'year'], axis=1)

# Y = Target Data
y = df['species']

# Decision Trees (at least in Scikit Learn), do not support 
# categorical data in a decision tree, so for our Penguin example,
# the "sex" field must be One Hot Encoded to properly be trained

# Give example of datasets before and after one hot encoding
X_encoded = pd.get_dummies(X, drop_first=True)

# Split up training and testing data
# For testing and fine tuning the model, use TDD approach to train model
# X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2)

# Create Decision Tree classifier object
model = DecisionTreeClassifier()

# Train Decision Tree Classifier
# model = model.fit(X_train, y_train)
model = model.fit(X_encoded, y)


# Test accuracy when training model
# accuracy(model, X_test, y_test)

# Save PNG visualization of decision tree
save_figure(model=model, feature_names=X_encoded.columns)

# Save model
joblib.dump(model, 'finalizedDecisionTree.sav')




