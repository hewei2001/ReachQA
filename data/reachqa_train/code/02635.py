import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

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
fig, ax = plt.subplots(figsize=(14, 9))

# Create the stacked area plot with gradient-like colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
ax.stackplot(years, data, labels=['Bicycle Couriers', 'Drone Deliveries', 'Electric Vans', 'Traditional Trucks'],
             colors=colors, alpha=0.8)

# Annotations to highlight trends
ax.annotate('Rapid rise in drone deliveries', xy=(2015, 18), xytext=(2012, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

# Add title and labels
ax.set_title('Shifting Modes of Urban Delivery in Techville\nGrowth and Trends from 2010 to 2020',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Deliveries (in thousands)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 180)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Delivery Methods')

# Refined gridlines and axis
ax.grid(linestyle='--', alpha=0.5)

# Customizing the x-axis label rotation for clarity
plt.xticks(rotation=45, ha='right')

# Define formatter for percentage share
def percentage_formatter(x, pos):
    total = np.sum(data, axis=0)[pos]
    return f'{(x / total) * 100:.1f}%'

# Create a secondary y-axis for percentage share
ax2 = ax.twinx()
ax2.set_ylim(0, 100)
ax2.yaxis.set_major_formatter(FuncFormatter(percentage_formatter))
ax2.set_ylabel('Percentage Share', fontsize=12, color='gray')
ax2.tick_params(axis='y', colors='gray')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()