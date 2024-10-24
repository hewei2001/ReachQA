import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Number of deliveries for each method over the years (in thousands)
bicycle_couriers = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
drone_deliveries = np.array([1, 3, 5, 8, 12, 18, 24, 30, 35, 40, 45])
electric_vans = np.array([5, 7, 10, 13, 17, 22, 28, 33, 37, 42, 48])
traditional_trucks = np.array([65, 62, 58, 55, 51, 47, 43, 40, 36, 33, 30])

# Stack the data for an area plot
data = np.vstack([bicycle_couriers, drone_deliveries, electric_vans, traditional_trucks])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the stacked area plot
ax.stackplot(years, data, labels=['Bicycle Couriers', 'Drone Deliveries', 'Electric Vans', 'Traditional Trucks'],
             colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Add title and labels
ax.set_title('Shifting Modes of Urban Delivery in Techville\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Deliveries (in thousands)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 180)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Delivery Methods')

# Customize the grid
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Customize x-axis labels
plt.xticks(rotation=45)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()