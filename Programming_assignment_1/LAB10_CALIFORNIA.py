import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('housing_data.csv')

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    data.drop('median_house_value', axis=1),  # Features
    data['median_house_value'],  # Labels
    test_size=0.2,  # 20% for testing
    random_state=42  # For reproducibility
)

# Train the random forest regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(train_data, train_labels)

# Evaluate the model on the testing set
predictions = model.predict(test_data)
mse = mean_squared_error(test_labels, predictions)
print(f"Mean squared error: {mse:.2f}")
