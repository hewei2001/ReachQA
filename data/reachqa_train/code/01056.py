import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Popularity data for different gardening techniques (in arbitrary units)
balcony_gardening = np.array([10, 20, 30, 35, 40, 45, 47, 48, 50, 55, 60])
vertical_gardening = np.array([5, 10, 15, 18, 22, 27, 32, 38, 45, 50, 60])
community_gardens = np.array([20, 30, 35, 40, 45, 50, 52, 55, 58, 60, 62])
hydroponic_gardening = np.array([1, 2, 5, 8, 12, 18, 25, 30, 40, 50, 60])

# Combine data for stacking
gardening_trends = np.vstack([balcony_gardening, vertical_gardening, community_gardens, hydroponic_gardening])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
ax.stackplot(years, gardening_trends, labels=[
    "Balcony Gardening", "Vertical Gardening", "Community Gardens", "Hydroponic Gardening"],
    colors=colors, alpha=0.8)

# Set the title and labels
ax.set_title("Urban Gardening Trends: A Decade of Growth\nCity Green Initiatives (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Popularity Index", fontsize=12)

# Add grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Annotate key trends
ax.annotate('Hydroponics Rise', xy=(2020, 60), xytext=(2017, 80),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='black')

# Rotate x-axis labels for clarity
plt.xticks(years, rotation=45)

# Add a legend with title
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Gardening Styles", fontsize='small')

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()