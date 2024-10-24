import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Consumption data in GWh for each energy source
solar = np.array([5, 10, 20, 35, 50, 70, 90, 120, 150, 185, 210])
wind = np.array([8, 15, 25, 40, 60, 80, 110, 130, 160, 190, 220])
hydro = np.array([20, 22, 23, 25, 27, 30, 35, 40, 45, 50, 55])
biomass = np.array([10, 12, 15, 18, 22, 28, 35, 42, 50, 60, 70])

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Generate stacked area plot
ax.stackplot(years, solar, wind, hydro, biomass, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=['#FFD700', '#00BFFF', '#32CD32', '#8A2BE2'], alpha=0.85)

# Set title and labels
ax.set_title("Evolution of Renewable Energy Consumption\nin Rivertown (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Consumption (GWh)", fontsize=12)

# Configure grid, legend, and ticks
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title="Energy Source", fontsize=10, bbox_to_anchor=(1, 1))
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 401, 50))
ax.set_xlim(2010, 2020)
ax.set_ylim(0, 400)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()