import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2019
years = np.arange(2010, 2020)

# Artificial data for hectares of gardening space in urban areas
community_gardens = np.array([20, 25, 30, 35, 40, 45, 50, 60, 65, 70])
balcony_gardens = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
rooftop_gardens = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
indoor_planting = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Colors for the different gardening types
colors = ['#88B04B', '#F7CAC9', '#92A8D1', '#034F84']

# Plot the area chart
plt.figure(figsize=(12, 7))
plt.stackplot(years, community_gardens, balcony_gardens, rooftop_gardens, indoor_planting,
              labels=['Community Gardens', 'Balcony Gardens', 'Rooftop Gardens', 'Indoor Planting'],
              colors=colors, alpha=0.8)

# Add title and labels
plt.title('Expansion of Urban Gardening Practices (2010-2019)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Area in Hectares', fontsize=14)
plt.legend(loc='upper left', title="Gardening Types", fontsize=10)

# Customize grid and layout
plt.grid(alpha=0.3)
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()