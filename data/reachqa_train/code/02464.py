import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2025 to 2050
years = np.arange(2025, 2051)

# Data representing millions of packages delivered by drones per year per continent
asia = np.array([0.5, 1.2, 2.5, 4.0, 6.5, 9.3, 13.5, 17.5, 22.0, 27.0, 33.0, 40.0, 48.5, 58.0, 68.5, 80.0, 92.5, 105.0, 120.0, 135.0, 150.0, 170.0, 190.0, 210.0, 235.0, 260.0])
europe = np.array([0.3, 0.8, 1.5, 2.5, 4.0, 6.0, 8.5, 11.0, 14.0, 17.5, 21.5, 26.0, 31.0, 36.5, 42.5, 49.0, 56.0, 64.0, 72.5, 81.5, 91.0, 102.0, 114.0, 127.0, 140.5, 155.5])
north_america = np.array([0.4, 1.0, 1.8, 3.0, 4.8, 7.0, 9.7, 12.5, 15.8, 19.5, 23.5, 28.0, 33.0, 38.5, 44.5, 51.0, 58.0, 66.0, 74.5, 83.5, 93.0, 104.0, 116.0, 129.0, 143.5, 158.5])
africa = np.array([0.1, 0.3, 0.5, 0.8, 1.2, 1.8, 2.5, 3.3, 4.2, 5.3, 6.5, 8.0, 9.5, 11.0, 13.0, 15.0, 17.5, 20.0, 23.0, 26.5, 30.0, 34.0, 38.5, 43.0, 48.5, 54.5])
south_america = np.array([0.2, 0.5, 0.8, 1.3, 2.0, 3.0, 4.2, 5.6, 7.3, 9.3, 11.5, 14.0, 17.0, 20.5, 24.5, 29.0, 34.0, 39.5, 45.5, 52.0, 59.0, 67.0, 76.0, 86.0, 97.5, 110.0])

# Create stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stacking the areas to show cumulative values over time
ax.stackplot(years, asia, europe, north_america, africa, south_america,
             labels=['Asia', 'Europe', 'North America', 'Africa', 'South America'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.85)

# Add labels, title, and legend
ax.set_title("Global Drone Delivery Usage:\nTrends Across Continents (2025-2050)", fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Millions of Packages Delivered', fontsize=14)
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1.02, 1))
ax.grid(True, linestyle='--', alpha=0.5)

# Enhancing x-axis with year labels
ax.set_xticks(np.arange(2025, 2051, 5))
ax.tick_params(axis='x', rotation=45)

# Emphasize significant milestones with annotations
ax.annotate('Regulatory Breakthroughs in Asia', xy=(2032, 22), xytext=(2035, 60),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax.annotate('North America Expansion', xy=(2040, 33), xytext=(2042, 80),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()