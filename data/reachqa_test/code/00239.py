import matplotlib.pyplot as plt
import numpy as np

# Apply a style for better aesthetics
plt.style.use('ggplot')

# Fictional cities
cities = [
    'Eco City', 'Green Valley', 'Clean Town', 'Renewable Hills', 
    'Solar Bay', 'Wind Ridge', 'Hydroville', 'Biofuels Town', 'Fusionville', 'Quantum Harbor'
]

# Electric vehicles registered (in thousands)
electric_vehicles = np.array([15, 8, 25, 10, 30, 5, 12, 17, 9, 20])

# Charging stations (hundreds)
charging_stations = np.array([6, 5, 10, 4, 12, 2, 7, 8, 3, 9])

# Average distance to the nearest charging station (in km) - fictional data
average_distance = np.array([1.2, 1.5, 1.1, 2.0, 0.8, 2.5, 1.3, 1.4, 2.2, 1.0])

# Color and size settings for the scatter points
colors = electric_vehicles * 10
sizes = electric_vehicles * 20

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 1]})

# First subplot: Scatter plot
scatter = ax[0].scatter(electric_vehicles, charging_stations, c=colors, s=sizes, cmap='plasma', alpha=0.8, edgecolors='k', linewidth=1.5)
cbar = plt.colorbar(scatter, ax=ax[0])
cbar.set_label('Electric Vehicles Count (in thousands)', rotation=270, labelpad=20)
ax[0].set_title('EV Adoption vs. Charging Infrastructure\nAcross Various Fictional Cities', fontsize=16, fontweight='bold', pad=20)
ax[0].set_xlabel('Electric Vehicles Registered (Thousands)', fontsize=14)
ax[0].set_ylabel('Charging Stations (Hundreds)', fontsize=14)

# Annotate each point with city names
for i, city in enumerate(cities):
    ax[0].annotate(city, (electric_vehicles[i], charging_stations[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='navy')

# Configure grid and layout
ax[0].grid(True, linestyle='--', alpha=0.7)
ax[0].set_xticks(range(0, 35, 5))
ax[0].set_yticks(range(0, 15, 3))

# Second subplot: Bar plot for average distance
ax[1].barh(cities, average_distance, color='skyblue', edgecolor='black')
ax[1].set_title('Average Distance to Charging Stations', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Distance (km)', fontsize=12)
ax[1].invert_yaxis()  # Invert y-axis for better alignment

# Tight layout adjustment for avoiding overlap
plt.tight_layout()

# Show plot
plt.show()