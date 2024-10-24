import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2000, 2020)

# Energy contributions in percentage over the years
solar_energy = np.array([2, 3, 5, 8, 12, 18, 24, 30, 35, 42, 48, 54, 60, 65, 68, 70, 72, 73, 74, 75])
wind_energy = np.array([5, 6, 8, 10, 13, 17, 20, 24, 27, 30, 32, 34, 36, 38, 39, 40, 41, 42, 42, 43])
hydro_energy = np.array([15, 16, 17, 18, 20, 21, 22, 23, 23, 24, 24, 25, 26, 26, 27, 28, 28, 29, 30, 31])

# Create an area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the areas
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, labels=['Solar', 'Wind', 'Hydroelectric'],
             colors=['#FFD700', '#87CEEB', '#3CB371'], alpha=0.8)

# Set title and labels
ax.set_title("Evolution of Renewable Energy Adoption in\nEnchanted Valleys (2000-2019)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Percentage of Total Energy Consumption", fontsize=12)
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 100)

# Adding a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adding a legend
ax.legend(title="Energy Type", loc="upper left", fontsize=11, frameon=False)

# Adding annotations for key milestones
ax.annotate('Major Solar Initiative', xy=(2005, 18), xytext=(2003, 30),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
ax.annotate('Wind Energy Peaks', xy=(2015, 90), xytext=(2012, 70),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Rotate x-axis labels if needed to avoid overlap
plt.xticks(rotation=45)

# Adjust layout to fit everything
plt.tight_layout()

# Show plot
plt.show()