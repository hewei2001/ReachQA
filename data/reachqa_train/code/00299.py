import matplotlib.pyplot as plt
import numpy as np

# Define continents and milestone years
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
years = ['2000', '2005', '2010', '2015', '2020']

# Internet access data (% of population)
connectivity_data = np.array([
    [2, 5, 10, 25, 40],   # Africa
    [10, 20, 30, 50, 70],  # Asia
    [30, 50, 70, 80, 90],  # Europe
    [40, 60, 75, 85, 95],  # North America
    [10, 20, 35, 50, 65],  # South America
    [50, 60, 70, 85, 90]   # Australia
])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.imshow(connectivity_data, cmap='Blues', aspect='auto', interpolation='nearest')

# Add color bar
cbar = fig.colorbar(cax, ax=ax, pad=0.02)
cbar.set_label('Internet Access (% of population)', fontsize=12)

# Set axis labels and ticks
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, fontsize=11, rotation=45)
ax.set_yticks(np.arange(len(continents)))
ax.set_yticklabels(continents, fontsize=11)

# Set a multi-line title
plt.title('Mapping the Evolution of Internet Connectivity\nAcross Continents (2000-2020)', fontsize=16, fontweight='bold')

# Annotate each cell with the connectivity value
for i in range(len(continents)):
    for j in range(len(years)):
        ax.text(j, i, f'{connectivity_data[i, j]}%', ha='center', va='center', color='black', fontsize=10)

# Enable gridlines for better readability
ax.grid(which='major', color='gray', linestyle='--', linewidth=0.5)

# Adjust layout to prevent clipping of tick-labels and titles
plt.tight_layout()

# Display the plot
plt.show()