import matplotlib.pyplot as plt
import numpy as np

# Average monthly temperatures for each continent (°C)
temperature_data = np.array([
    [-5, 0, 5, 10, 15, 20, 25, 25, 20, 10, 5, 0],  # North America
    [25, 26, 25, 24, 23, 22, 21, 21, 22, 23, 24, 25],  # South America
    [0, 2, 5, 10, 15, 20, 25, 24, 20, 15, 10, 5],  # Europe
    [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28],  # Africa
    [-10, -5, 5, 10, 15, 25, 30, 30, 25, 15, 5, -5],  # Asia
    [25, 25, 23, 20, 18, 15, 10, 10, 15, 20, 22, 25],  # Australia
    [-60, -58, -55, -50, -40, -30, -25, -20, -30, -40, -50, -58]  # Antarctica
])

# Names of continents
continents = [
    'North America', 'South America',
    'Europe', 'Africa', 'Asia', 'Australia', 'Antarctica'
]

# Names of months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Calculate average monthly temperatures across continents
average_monthly_temp = np.mean(temperature_data, axis=0)

# Create the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Heat map subplot
cax1 = axes[0].imshow(temperature_data, cmap='coolwarm', aspect='auto', interpolation='nearest')
axes[0].set_xticks(np.arange(len(months)))
axes[0].set_yticks(np.arange(len(continents)))
axes[0].set_xticklabels(months, rotation=45, ha='right', fontsize=10)
axes[0].set_yticklabels(continents, fontsize=10)
axes[0].set_title("Global Temperature Variations:\nA Year-long Overview Across Continents", fontsize=16, fontweight='bold', pad=10)
cbar1 = fig.colorbar(cax1, ax=axes[0], orientation='vertical', shrink=0.8, pad=0.05)
cbar1.set_label('Average Temperature (°C)', fontsize=12)

# Annotate each cell in the heat map
for (i, j), val in np.ndenumerate(temperature_data):
    axes[0].text(j, i, f'{val}°C', ha='center', va='center', fontsize=8, color='black' if abs(val) < 20 else 'white')

# Line plot subplot for average temperature trends
for idx, data in enumerate(temperature_data):
    axes[1].plot(months, data, label=continents[idx], marker='o')

# Highlight average global trend
axes[1].plot(months, average_monthly_temp, label='Global Average', linestyle='--', color='black', linewidth=2, marker='x')

# Enhance subplot layout and add details
axes[1].set_title("Average Monthly Temperature Trends by Continent", fontsize=14, fontweight='bold')
axes[1].set_ylabel("Temperature (°C)")
axes[1].set_xlabel("Months")
axes[1].legend(loc='upper right', fontsize=9, ncol=2, frameon=False)
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()