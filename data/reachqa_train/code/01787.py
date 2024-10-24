import matplotlib.pyplot as plt
import numpy as np

# Define the time period from 2010 to 2020
years = np.arange(2010, 2021)

# Hypothetical data for logistics operations volume (in millions of shipments)
# Reflecting an initial decrease due to new legislation and a subsequent recovery
shipments_volume = np.array([200, 190, 185, 188, 192, 195, 198, 205, 210, 215, 220])

# Create a figure and axis for the plot
plt.figure(figsize=(12, 7))

# Plotting the line chart
plt.plot(years, shipments_volume, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8, label='Shipments Volume')

# Annotations to highlight significant events
plt.annotate('Green Freight Act Implemented', xy=(2010, 200), xytext=(2012, 210),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Recovery Begins', xy=(2015, 195), xytext=(2017, 205),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Title and axis labels
plt.title("Impact of Green Legislation on\nLogistics Operations (2010-2020)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Volume of Shipments (Millions)", fontsize=12)

# Adding a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adding legend
plt.legend(loc='upper left')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()