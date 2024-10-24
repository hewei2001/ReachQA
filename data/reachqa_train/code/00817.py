import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Area data in acres for each type of urban farming over the years
rooftop_gardens = [10, 15, 20, 25, 35, 45, 55, 65, 80, 95, 110]
vertical_farms = [5, 8, 12, 18, 25, 35, 45, 60, 75, 90, 105]
community_plots = [15, 20, 28, 40, 52, 67, 83, 100, 120, 140, 160]
hydroponics = [2, 5, 8, 14, 22, 30, 45, 60, 80, 100, 120]

# Colors for each farming type
colors = ['#76c7c0', '#f7cac9', '#92a8d1', '#ff6f61']

# Create the area plot
plt.figure(figsize=(14, 8))
plt.stackplot(years, rooftop_gardens, vertical_farms, community_plots, hydroponics,
              labels=['Rooftop Gardens', 'Vertical Farms', 'Community Plots', 'Hydroponics'],
              colors=colors, alpha=0.8)

# Add title and labels
plt.title('Urban Agriculture:\nDecadal Growth of Urban Farming Spaces in Metropolis', 
          fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Area Covered (Acres)', fontsize=12)

# Customize x-axis
plt.xticks(years, rotation=45)

# Add legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Highlight significant trends with annotations
plt.annotate('Emergence of Vertical Farms', xy=(2017, 60), xytext=(2015, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.annotate('Rapid Growth in Hydroponics', xy=(2021, 220), xytext=(2018, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()