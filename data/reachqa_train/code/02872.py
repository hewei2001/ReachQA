import matplotlib.pyplot as plt
import numpy as np

# Define the years for the study
years = np.arange(2010, 2021)

# Define percentage contribution of each energy source over the years
solar_energy = np.array([5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50])
wind_energy = np.array([10, 15, 20, 25, 27, 30, 32, 33, 34, 35, 36])
hydro_energy = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

# Stack data for the area plot
energy_sources = np.row_stack((solar_energy, wind_energy, hydro_energy))

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#32CD32']

# Plot the stacked area chart
ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro'], colors=colors, alpha=0.8)

# Add a title and labels
ax.set_title('Renewable Energy Adoption Over a Decade\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Renewable Energy (%)', fontsize=12)

# Customize ticks and grid
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend outside the plot
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Highlight certain years with annotations
highlight_years = {2015: "Paris Agreement", 2020: "Global Renewables Push"}
for year, event in highlight_years.items():
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=0.8)
    ax.text(year, 5, event, rotation=90, verticalalignment='bottom', horizontalalignment='right', color='grey', fontsize=9)

# Rotate x-axis labels slightly for better visibility
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()