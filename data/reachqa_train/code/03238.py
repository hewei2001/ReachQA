import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2000, 2051, 5)

# Contributions of different energy sources (in arbitrary units for simplicity)
solar = [1, 2, 4, 8, 15, 25, 35, 45, 60, 75, 90]
wind = [2, 4, 7, 12, 20, 30, 40, 50, 65, 80, 95]
hydropower = [30, 32, 33, 34, 35, 35, 36, 36, 37, 37, 38]
biomass = [5, 6, 7, 9, 12, 15, 20, 25, 30, 35, 40]

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the data
ax.stackplot(years, solar, wind, hydropower, biomass, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'],
             colors=['#ffa600', '#bc5090', '#003f5c', '#58508d'], alpha=0.8)

# Add titles and labels
ax.set_title("The Rise of Renewables:\nEnergy Landscape Transformation (2000-2050)", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (Arbitrary Units)", fontsize=12)

# Customize ticks and grid
ax.set_xticks(years)
ax.xaxis.set_tick_params(rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', title="Renewable Sources", fontsize=10, bbox_to_anchor=(1, 1))

# Annotate significant points
ax.annotate('Significant Solar Surge', xy=(2040, 190), xytext=(2025, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Adjust layout for a better fit
plt.tight_layout()

# Display the plot
plt.show()