import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for different types of green spaces (in hectares)
parks = np.array([50, 55, 60, 70, 80, 95, 110, 130, 150, 175, 200])
community_gardens = np.array([10, 15, 20, 25, 30, 40, 50, 65, 85, 100, 120])
green_rooftops = np.array([5, 7, 10, 12, 15, 20, 30, 40, 55, 70, 90])

# Create an area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stackplot to visualize the growth of green spaces
ax.stackplot(years, parks, community_gardens, green_rooftops,
             labels=['Parks', 'Community Gardens', 'Green Rooftops'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.8)

# Title and labels
ax.set_title('Evolution of Urban Green Spaces\nin GreenVille (2010-2020)',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Green Space Area (Hectares)', fontsize=14)

# Grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Customize x-ticks for clarity
plt.xticks(years, rotation=45)

# Create legend
ax.legend(loc='upper left', title='Green Space Type', fontsize=12)

# Layout adjustment
plt.tight_layout()

# Display plot
plt.show()