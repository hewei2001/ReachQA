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
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

# Create the heat map
fig, ax = plt.subplots(figsize=(14, 8))
cax = ax.imshow(temperature_data, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Set axis labels
ax.set_xticks(np.arange(len(months)))
ax.set_yticks(np.arange(len(continents)))
ax.set_xticklabels(months, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(continents, fontsize=10)

# Add a color bar
cbar = fig.colorbar(cax, orientation='vertical', shrink=0.8, pad=0.05)
cbar.set_label('Average Temperature (°C)', fontsize=12)

# Add title
plt.title("Global Temperature Variations:\nA Year-long Overview Across Continents", fontsize=16, fontweight='bold', pad=20)

# Annotate each cell with the numerical value
for (i, j), val in np.ndenumerate(temperature_data):
    ax.text(j, i, f'{val}°C', ha='center', va='center', fontsize=8, color='black' if abs(val) < 20 else 'white')

# Enhance layout
plt.tight_layout()

# Display the heat map
plt.show()