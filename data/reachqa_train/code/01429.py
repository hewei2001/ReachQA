import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2010, 2021)

# Chocolate consumption per capita in kilograms for each region
europe = np.array([9.8, 10.0, 10.3, 10.5, 10.5, 10.4, 10.6, 10.8, 11.0, 11.2, 11.4])
north_america = np.array([5.5, 5.7, 5.8, 6.0, 6.2, 6.0, 6.3, 6.5, 6.7, 6.9, 7.1])
asia = np.array([1.2, 1.4, 1.6, 2.0, 2.3, 2.6, 3.0, 3.5, 4.0, 4.5, 5.0])
south_america = np.array([2.5, 2.7, 2.8, 3.0, 3.3, 3.5, 3.8, 4.0, 4.3, 4.5, 4.8])
africa = np.array([0.9, 1.0, 1.1, 1.3, 1.5, 1.7, 2.0, 2.3, 2.6, 3.0, 3.5])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each region's data with distinct styles
ax.plot(years, europe, marker='o', linestyle='-', color='brown', linewidth=2, label='Europe')
ax.plot(years, north_america, marker='s', linestyle='--', color='blue', linewidth=2, label='North America')
ax.plot(years, asia, marker='^', linestyle='-', color='red', linewidth=2, label='Asia')
ax.plot(years, south_america, marker='d', linestyle='-.', color='green', linewidth=2, label='South America')
ax.plot(years, africa, marker='x', linestyle=':', color='orange', linewidth=2, label='Africa')

# Adding titles and labels
ax.set_title("Global Chocolate Consumption Trends\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Consumption per Capita (kg)", fontsize=14)

# Position the legend and add grid
ax.legend(loc='upper left', fontsize=12, title='Regions')
ax.grid(True, linestyle='--', alpha=0.7)

# Improve x-axis labeling
plt.xticks(years, rotation=45, fontsize=10)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()