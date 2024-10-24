import matplotlib.pyplot as plt
import numpy as np

# Define the original data
years = np.array([1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])
energy_production = np.array([0.1, 0.15, 0.3, 0.5, 1, 2, 4, 10, 20, 50, 100])

# Define related data for installed capacity
# Note: This data is constructed for demonstration purposes
installed_capacity = np.array([0.2, 0.3, 0.5, 1, 2, 3, 5, 12, 25, 55, 120])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the primary data (solar energy production)
ax1.plot(years, energy_production, marker='o', linestyle='-', color='gold', linewidth=2, markersize=8, label='Energy Production (GW)')

# Plot the secondary data (installed capacity) as a bar chart
ax2 = ax1.twinx()
ax2.bar(years, installed_capacity, width=2, color='lightblue', alpha=0.5, label='Installed Capacity (GW)')

# Highlight key milestones
milestones = {1980: 0.3, 2000: 4, 2015: 50}
for year, production in milestones.items():
    ax1.annotate(f"{year}: {production} GW", xy=(year, production), xytext=(year + 2, production + 10),
                 arrowprops=dict(facecolor='gray', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=9, color='darkslategray')

# Set titles and labels
ax1.set_title('Rise of Solar Energy Production and Installed Capacity\n1970-2020', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (Gigawatts)', fontsize=12)
ax2.set_ylabel('Installed Capacity (Gigawatts)', fontsize=12)

# Customize grid and style
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.minorticks_on()

# Add legends for both plots
ax1.legend(loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)

# Enhance the plot aesthetics
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()