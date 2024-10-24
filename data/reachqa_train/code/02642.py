import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2023)

# Create artificial data representing the percentage of total transportation trips for each mode
electric_buses = [5, 7, 9, 12, 15, 17, 20, 22, 25, 28]
cycling = [12, 14, 16, 18, 20, 22, 23, 24, 25, 26]
carpooling = [22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
electric_scooters = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Stack the data vertically
stacked_data = np.vstack([electric_buses, cycling, carpooling, electric_scooters])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, stacked_data, labels=['Electric Buses', 'Cycling', 'Carpooling', 'Electric Scooters'],
             colors=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728'], alpha=0.8)

# Add a title with line breaks for readability
ax.set_title('EcoVille Climate-Friendly Transportation Adoption\n (2013-2022)', fontsize=16, fontweight='bold', pad=15)

# Set x-axis and y-axis labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Trips (%)', fontsize=12)

# Customize the ticks on the axes for better readability
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

# Add a legend outside the main plot area
ax.legend(loc='upper left', fontsize=10, title='Transport Modes', bbox_to_anchor=(1.05, 1))

# Enhance grid visibility
ax.grid(visible=True, which='both', linestyle='--', linewidth=0.6, alpha=0.6)

# Set limits for y-axis
ax.set_ylim(0, 100)

# Adjust the layout to prevent overlap of visual elements
plt.tight_layout()

# Show the plot
plt.show()