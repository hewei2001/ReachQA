import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([2020, 2030, 2040, 2050, 2060])

# Define energy source data (in arbitrary units)
solar_energy = np.array([10, 20, 30, 35, 40])
wind_energy = np.array([5, 15, 25, 30, 35])
nuclear_energy = np.array([10, 10, 15, 20, 25])
fossil_fuels = np.array([75, 55, 30, 15, 0])

# Stacked data for plotting
energy_data = np.vstack([solar_energy, wind_energy, nuclear_energy, fossil_fuels])

# Plotting the area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create a stackplot
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Nuclear', 'Fossil Fuels'],
             colors=['#FFD700', '#1E90FF', '#228B22', '#A9A9A9'], alpha=0.8)

# Title and axis labels
ax.set_title('Energy Consumption Trends in Ecopolis\n(2020-2060)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (Arbitrary Units)', fontsize=14)

# Enhance x-axis readability
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=12)

# Adding gridlines
ax.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legend
ax.legend(loc='upper right', fontsize=12, title='Energy Sources')

# Customizing y-axis for better visual representation
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))

# Adjust layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()