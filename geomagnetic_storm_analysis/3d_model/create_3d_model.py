
import plotly.graph_objects as go
import pandas as pd

# Load the geomagnetic storm data
df = pd.read_csv('data/geomagnetic_storm_data.csv')

# Function to convert coordinates to float
def convert_coords(coord):
    coord = coord.replace('°', '').strip()
    if 'N' in coord or 'E' in coord:
        return float(coord.replace('N', '').replace('E', '').strip())
    elif 'S' in coord or 'W' in coord:
        return -float(coord.replace('S', '').replace('W', '').strip())
    return float(coord)

# Create a 3D Earth model
fig = go.Figure()

# Add Earth surface
fig.add_trace(go.Scattergeo(
    locationmode='ISO-3',
    lon=[-180, 180],
    lat=[-90, 90],
    mode='lines',
    line=dict(width=1, color='blue'),
))

# Add geomagnetic storm data points
for i, row in df.iterrows():
    locations = row['locations'].split('; ')
    for loc in locations:
        name, coords = loc.split(': ')
        lat, lon = coords.split(', ')
        lat = convert_coords(lat)
        lon = convert_coords(lon)
        fig.add_trace(go.Scattergeo(
            locationmode='ISO-3',
            lon=[lon],
            lat=[lat],
            mode='markers',
            marker=dict(size=10, color='red'),
            name=f'Storm {row["storm_id"]} - {name}'
        ))

# Update layout
fig.update_layout(
    title='Geomagnetic Storms',
    geo=dict(
        showland=True,
        landcolor='rgb(243, 243, 243)',
        subunitcolor='rgb(217, 217, 217)',
        countrycolor='rgb(217, 217, 217)',
        showlakes=True,
        lakecolor='rgb(255, 255, 255)',
        projection=dict(
            type='orthographic',
            rotation=dict(
                lon=0,
                lat=0
            )
        ),
        lonaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            range=[-180.0, 180.0],
            dtick=30
        ),
        lataxis=dict(
            showgrid=True,
            gridwidth=0.5,
            range=[-90.0, 90.0],
            dtick=30
        )
    )
)

# Save the figure
fig.write_html('3d_model/geomagnetic_storms.html')
