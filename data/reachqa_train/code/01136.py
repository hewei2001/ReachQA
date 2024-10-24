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

# Calculate the total number of properties sold each year
total_properties = apartments + single_family_homes + condos + townhouses + luxury_villas

# Calculate the percentage change of properties sold each year
percentage_change = np.diff(total_properties) / total_properties[:-1] * 100

# Create the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6), constrained_layout=True)

# Plot the stacked area chart on the first subplot
axs[0].stackplot(years, apartments, single_family_homes, condos, townhouses, luxury_villas,
                 labels=['Apartments', 'Single-Family Homes', 'Condos', 'Townhouses', 'Luxury Villas'],
                 colors=['#7FB3D5', '#76D7C4', '#F7DC6F', '#F1948A', '#C39BD3'], alpha=0.8)
axs[0].set_title('Real Estate Trends in Skyline City (2013-2023)\nSales of Different Property Types', fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Number of Properties Sold', fontsize=12)
axs[0].legend(loc='upper left', title='Property Types', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].set_xticks(years)
axs[0].tick_params(axis='x', rotation=45)

# Plot the percentage change as a bar chart on the second subplot
axs[1].bar(years[1:], percentage_change, color='#FFA07A', alpha=0.7)
axs[1].set_title('Annual Percentage Change\nin Total Properties Sold', fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Percentage Change (%)', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].set_xticks(years[1:])
axs[1].tick_params(axis='x', rotation=45)

# Show the plots
plt.show()