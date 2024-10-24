import matplotlib.pyplot as plt
import numpy as np

# Cities considered for the study
cities = [
    'Green Valley', 'Solar City', 'Wind Town', 'Eco Ville', 'Hydro Borough',
    'Leaf Village', 'Solaris', 'Geothermal Bay', 'Bio District', 'Recycling Haven'
]

# Number of charging stations in each city
charging_stations = [150, 220, 130, 180, 210, 110, 90, 200, 170, 140]

# Average waiting time at charging stations in minutes
waiting_times = [15, 12, 20, 17, 14, 25, 30, 11, 16, 19]

# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot with customization
scatter = ax.scatter(
    charging_stations, waiting_times,
    c=waiting_times, cmap='coolwarm', s=100, edgecolor='black', alpha=0.7
)

# Adding city labels to each point
for i, city in enumerate(cities):
    ax.annotate(city, (charging_stations[i], waiting_times[i]),
                textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Customizing the plot
ax.set_title('EV Charging Stations vs. Waiting Time\nA Comparative City Analysis', fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Charging Stations', fontsize=12)
ax.set_ylabel('Average Waiting Time (minutes)', fontsize=12)

# Add color bar to show the meaning of color intensity
cbar = plt.colorbar(scatter)
cbar.set_label('Waiting Time Intensity', fontsize=12)

# Adding grid for better visualization
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust the layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()