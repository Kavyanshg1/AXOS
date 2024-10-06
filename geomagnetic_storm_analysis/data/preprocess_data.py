
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('data/geomagnetic_storm_data.csv')

# Preprocess the data
# For simplicity, let's assume we only need the 'kp_index' for model training
X = df[['storm_id', 'start_time']]
y = df['kp_index']

# Convert 'start_time' to datetime and extract features
X['start_time'] = pd.to_datetime(X['start_time'])
X['year'] = X['start_time'].dt.year
X['month'] = X['start_time'].dt.month
X['day'] = X['start_time'].dt.day
X['hour'] = X['start_time'].dt.hour
X = X.drop(columns=['start_time'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the preprocessed data
X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)
