import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data
cities = ["City A", "City B", "City C", "City D", "City E"]
green_space_area = np.array([10, 15, 5, 20, 8])  # in square kilometers
aqi = np.array([50, 40, 80, 30, 70])  # Air Quality Index (lower is better)
num_parks = np.array([5, 8, 2, 10, 3])  # Number of parks

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot for AQI vs Green Space Area
axs[0].scatter(green_space_area, aqi, color='forestgreen', s=100, alpha=0.7, label='City Data Points')
slope, intercept, r_value, p_value, std_err = stats.linregress(green_space_area, aqi)
line = slope * green_space_area + intercept
axs[0].plot(green_space_area, line, color='darkorange', linewidth=2, label='Fitted Line: AQI vs Green Space')

for i, city in enumerate(cities):
    axs[0].annotate(city, (green_space_area[i], aqi[i]), textcoords="offset points", xytext=(0, 5), ha='center')

axs[0].set_title("Impact of Urban Green Spaces on Air Quality\n(AQI vs Green Space Area)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Green Space Area (sq km)", fontsize=14)
axs[0].set_ylabel("Air Quality Index (AQI)", fontsize=14)
axs[0].set_xlim(0, 25)
axs[0].set_ylim(0, 100)
axs[0].set_xticks(np.arange(0, 26, 5))
axs[0].set_yticks(np.arange(0, 101, 10))
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].legend(title="Legend", fontsize=10)

# Bar plot for Number of Parks
axs[1].bar(cities, num_parks, color='skyblue', alpha=0.8)
axs[1].set_title("Number of Parks per City", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Cities", fontsize=14)
axs[1].set_ylabel("Number of Parks", fontsize=14)
axs[1].set_ylim(0, max(num_parks) + 2)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()