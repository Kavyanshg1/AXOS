
import pandas as pd

# Sample data based on the provided information
data = {
    'storm_id': [1, 2, 3, 4, 5],
    'start_time': ['2024-05-02 15:00:00', '2024-05-10 15:00:00', '2024-05-12 21:00:00', '2024-05-16 06:00:00', '2024-05-17 18:00:00'],
    'kp_index': [6.67, 9.0, 6.33, 6.0, 6.0],
    'locations': [
        'Alaska, USA: 64.8° N, 147.7° W; Northwestern Canada: 60.0° N, 120.0° W; Northern Europe: 60.0° N, 10.0° E',
        'Northern Alaska, USA: 70.0° N, 150.0° W; Northern Canada: 65.0° N, 120.0° W; Northern Europe: 65.0° N, 10.0° E; Southern Australia: 40.0° S, 140.0° E; Southern New Zealand: 45.0° S, 170.0° E',
        'Arctic Circle: 70.0° N, 0.0° E; Northern Scandinavia: 65.0° N, 20.0° E; Northern Russia: 60.0° N, 100.0° E',
        'Western Alaska, USA: 60.0° N, 160.0° W; Northwestern Canada: 60.0° N, 120.0° W; Northern Europe: 60.0° N, 10.0° E',
        'Northern Alaska, USA: 70.0° N, 150.0° W; Northern Canada: 65.0° N, 120.0° W; Northern Europe: 65.0° N, 10.0° E'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data/geomagnetic_storm_data.csv', index=False)
