import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2031)

# Create artificial data representing the percentage of total transportation trips for each mode
electric_buses = np.linspace(3, 30, len(years))  # Non-linear growth
cycling = 20 + 2 * np.sin(np.linspace(0, 10, len(years)))  # Sinusoidal variation
carpooling = np.clip(30 - np.linspace(0, 25, len(years)), 0, None)  # Decreasing trend
electric_scooters = np.clip(0.5 * (years - 2010)**1.5, 0, 18)  # Exponential-like growth
walking = np.clip(15 + np.cos(np.linspace(0, 8, len(years))) * 5, 0, None)  # Cyclic variation
ride_sharing = np.clip(20 - electric_scooters, 0, None)  # Inverse relationship with scooters

# Ensure the sum is 100% for each year
total_sum = electric_buses + cycling + carpooling + electric_scooters + walking + ride_sharing
remaining_space = 100 - total_sum
ride_sharing += remaining_space

# Stack the data vertically
stacked_data = np.vstack([electric_buses, cycling, carpooling, electric_scooters, walking, ride_sharing])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, stacked_data, labels=['Electric Buses', 'Cycling', 'Carpooling', 
                                          'Electric Scooters', 'Walking', 'Ride-sharing'],
             colors=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728', '#9467bd', '#8c564b'], alpha=0.85)

# Add a title with line breaks for readability
ax.set_title('EcoVille Sustainable Transportation Mode Share\n(2010-2030)', 
             fontsize=18, fontweight='bold', pad=15)

# Set x-axis and y-axis labels
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage of Total Trips (%)', fontsize=14)

# Customize the ticks on the axes for better readability
ax.set_xticks(np.arange(2010, 2031, 2))
ax.set_yticks(np.arange(0, 101, 10))

# Add a legend outside the main plot area
ax.legend(loc='upper left', fontsize=12, title='Transport Modes', bbox_to_anchor=(1.05, 1))

# Enhance grid visibility
ax.grid(visible=True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Set limits for y-axis
ax.set_ylim(0, 100)

# Adjust the layout to prevent overlap of visual elements
plt.tight_layout()

# Show the plot
plt.show()