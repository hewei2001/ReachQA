import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.array([1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])
energy_production = np.array([0.1, 0.15, 0.3, 0.5, 1, 2, 4, 10, 20, 50, 100])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(years, energy_production, marker='o', linestyle='-', color='gold', linewidth=2, markersize=8)

# Highlight key milestones
milestones = {1980: 0.3, 2000: 4, 2015: 50}
for year, production in milestones.items():
    ax.annotate(f"{year}: {production} GW", xy=(year, production), xytext=(year + 2, production + 10),
                arrowprops=dict(facecolor='gray', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=9, color='darkslategray')

# Set titles and labels
ax.set_title('Rise of Solar Energy Production\n1970-2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (Gigawatts)', fontsize=12)

# Customize grid and style
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.minorticks_on()

# Add a legend
ax.legend(['Global Solar Energy Production'], loc='upper left', frameon=False)

# Enhance the plot aesthetics
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()