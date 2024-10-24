import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Data: number of properties sold each year for different property types
apartments = np.array([150, 165, 180, 190, 210, 230, 250, 270, 280, 300, 310])
single_family_homes = np.array([80, 78, 75, 73, 70, 68, 66, 65, 64, 63, 60])
condos = np.array([50, 52, 55, 60, 68, 75, 80, 85, 90, 95, 100])
townhouses = np.array([30, 32, 35, 38, 42, 48, 52, 55, 58, 60, 62])
luxury_villas = np.array([10, 11, 13, 15, 18, 20, 22, 24, 26, 28, 30])

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the stacked area chart
ax.stackplot(years, apartments, single_family_homes, condos, townhouses, luxury_villas,
             labels=['Apartments', 'Single-Family Homes', 'Condos', 'Townhouses', 'Luxury Villas'],
             colors=['#7FB3D5', '#76D7C4', '#F7DC6F', '#F1948A', '#C39BD3'], alpha=0.8)

# Set the title and labels, with line breaks in the title for clarity
ax.set_title('Real Estate Trends in Skyline City (2013-2023)\nSales of Different Property Types', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Properties Sold', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', title='Property Types', fontsize=10)

# Enable grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Ensure x-axis labels are not overlapping
plt.xticks(years, rotation=45)

# Adjust layout to prevent clipping of titles and labels
plt.tight_layout()

# Display the plot
plt.show()