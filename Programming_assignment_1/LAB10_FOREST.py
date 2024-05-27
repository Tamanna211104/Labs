import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('covertype.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Cover_Type', axis=1), 
                                                    data['Cover_Type'], 
                                                    test_size=0.2, 
                                                    random_state=42)

# Train a decision tree classifier on the training data
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Use the trained model to make predictions on the testing data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model on the testing data
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))


