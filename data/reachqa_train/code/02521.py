import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for different types of green spaces (in hectares)
parks = np.array([50, 55, 60, 70, 80, 95, 110, 130, 150, 175, 200])
community_gardens = np.array([10, 15, 20, 25, 30, 40, 50, 65, 85, 100, 120])
green_rooftops = np.array([5, 7, 10, 12, 15, 20, 30, 40, 55, 70, 90])

# Calculate total green space for each year
total_green_space = parks + community_gardens + green_rooftops

# Calculate proportions
parks_prop = parks / total_green_space * 100
community_gardens_prop = community_gardens / total_green_space * 100
green_rooftops_prop = green_rooftops / total_green_space * 100

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Stackplot for the total areas of green spaces
axs[0].stackplot(years, parks, community_gardens, green_rooftops,
                 labels=['Parks', 'Community Gardens', 'Green Rooftops'],
                 colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.8)
axs[0].set_title('Evolution of Urban Green Spaces\nin GreenVille (2010-2020)',
                 fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Green Space Area (Hectares)', fontsize=12)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', title='Green Space Type', fontsize=10)

# Line plot for proportions of green spaces
axs[1].plot(years, parks_prop, marker='o', label='Parks', color='#66c2a5', linestyle='-')
axs[1].plot(years, community_gardens_prop, marker='s', label='Community Gardens', color='#fc8d62', linestyle='--')
axs[1].plot(years, green_rooftops_prop, marker='^', label='Green Rooftops', color='#8da0cb', linestyle='-.')
axs[1].set_title('Proportion of Green Space Types\n(Percentage of Total)', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Proportion (%)', fontsize=12)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper left', title='Green Space Type', fontsize=10)

# Rotate x-ticks for readability
for ax in axs:
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45)

# Adjust layout for clarity
plt.tight_layout()

# Display plot
plt.show()