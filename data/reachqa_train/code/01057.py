import matplotlib.pyplot as plt
import numpy as np

# Define finer time resolution (half-yearly data)
years = np.arange(2010, 2021, 0.5)

# Constructing more detailed data for each gardening technique
balcony_gardening = np.array([10, 15, 20, 22, 25, 30, 32, 35, 37, 40, 42, 45, 47, 48, 49, 50, 52, 53, 55, 57, 58, 60])
vertical_gardening = np.array([5, 7, 10, 12, 15, 18, 19, 22, 23, 27, 30, 32, 35, 38, 40, 42, 45, 47, 48, 50, 55, 60])
community_gardens = np.array([20, 22, 25, 28, 30, 35, 36, 40, 42, 45, 47, 50, 52, 54, 56, 58, 60, 61, 62, 63, 65, 67])
hydroponic_gardening = np.array([1, 1, 2, 3, 5, 7, 8, 12, 14, 18, 20, 25, 28, 30, 35, 40, 42, 45, 48, 50, 58, 60])
container_gardening = np.array([3, 5, 7, 10, 12, 15, 18, 21, 23, 26, 29, 33, 36, 38, 40, 41, 42, 43, 44, 45, 46, 47])

# Combine data for stacking
gardening_trends = np.vstack([balcony_gardening, vertical_gardening, community_gardens, hydroponic_gardening, container_gardening])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(16, 9))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
ax.stackplot(years, gardening_trends, labels=[
    "Balcony Gardening", "Vertical Gardening", "Community Gardens", "Hydroponic Gardening", "Container Gardening"],
    colors=colors, alpha=0.8)

# Set the title and labels
ax.set_title("Urban Gardening Trends: A Decade of Growth\nCity Green Initiatives (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Popularity Index", fontsize=12)

# Add grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Annotate key trends
ax.annotate('Hydroponics Surge', xy=(2020, 60), xytext=(2016, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, fontweight='bold', color='black')

# Overlay trend lines (Moving Average)
for i, technique in enumerate(gardening_trends):
    ax.plot(years, np.convolve(technique, np.ones(4)/4, mode='same'), linestyle='--', color=colors[i])

# Rotate x-axis labels for clarity
plt.xticks(years, rotation=45)

# Add a legend with title
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Gardening Styles", fontsize='small')

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()