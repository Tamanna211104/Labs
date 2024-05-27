import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('youtube_data.csv')

# Extract the features and target variable
X_views = data['title'] # Use the video titles as the feature for predicting views
y_views = data['views']

X_likes = data['title'] + ' ' + data['author'] # Concatenate the title and author as the feature for predicting likes
y_likes = data['likes']

# Vectorize the text data
vectorizer = CountVectorizer()
X_views = vectorizer.fit_transform(X_views)
X_likes = vectorizer.fit_transform(X_likes)

# Split the data into training and testing sets
split_index = int(len(data) * 0.8)
X_train_views, X_test_views = X_views[:split_index], X_views[split_index:]
y_train_views, y_test_views = y_views[:split_index], y_views[split_index:]

X_train_likes, X_test_likes = X_likes[:split_index], X_likes[split_index:]
y_train_likes, y_test_likes = y_likes[:split_index], y_likes[split_index:]

# Train the model for predicting views
reg_views = LinearRegression()
reg_views.fit(X_train_views, y_train_views)

# Train the model for predicting likes
reg_likes = LinearRegression()
reg_likes.fit(X_train_likes, y_train_likes)

# Make predictions on the test set
y_pred_views = reg_views.predict(X_test_views)
y_pred_likes = reg_likes.predict(X_test_likes)

# Print the predicted values for the test set
print('Predicted views:', y_pred_views)
print('Predicted likes:', y_pred_likes)
