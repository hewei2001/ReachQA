import matplotlib.pyplot as plt
import numpy as np

# Expanded data for additional cities
cities = ["Sunville", "Overcast", "Cloudy Town", "Clearwater", "Rainberg", 
          "Windy Ridge", "Fogville", "Shadytown", "Brighton", "Stormville"]
cloud_coverage = [10, 80, 60, 20, 90, 40, 70, 55, 15, 95]  # Cloud coverage in percentage
solar_power = [900, 200, 400, 850, 150, 500, 300, 350, 880, 120]  # Solar power generation in MW
wind_power = [300, 450, 400, 320, 200, 600, 350, 410, 330, 100]  # Wind power generation in MW

# Create a new figure with a grid layout
fig, ax1 = plt.subplots(figsize=(14, 10))

# Scatter plot for cloud coverage vs solar power
bubble_sizes = np.array([20, 30, 25, 35, 15, 40, 20, 25, 30, 10]) * 10  # Example populations
scatter = ax1.scatter(cloud_coverage, solar_power, s=bubble_sizes, c=wind_power, 
                      cmap='coolwarm', edgecolor='black', alpha=0.8)

# Annotate each city
for i, city in enumerate(cities):
    ax1.annotate(city, (cloud_coverage[i], solar_power[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Labels and title
ax1.set_xlabel('Cloud Coverage (%)', fontsize=12)
ax1.set_ylabel('Solar Power Generation (MW)', fontsize=12)
ax1.set_title('Impact of Cloud Coverage on Solar and Wind Power Generation\nAcross Various Cities', fontsize=14, fontweight='bold')

# Add colorbar for wind power
cbar = plt.colorbar(scatter)
cbar.set_label('Wind Power Generation (MW)', fontsize=12)

# Overlay a trend line
m, b = np.polyfit(cloud_coverage, solar_power, 1)
ax1.plot(cloud_coverage, m*np.array(cloud_coverage) + b, linestyle='--', color='gray', linewidth=1)

# Secondary y-axis for wind power trend line
ax2 = ax1.twinx()
m_wind, b_wind = np.polyfit(cloud_coverage, wind_power, 1)
ax2.plot(cloud_coverage, m_wind*np.array(cloud_coverage) + b_wind, linestyle='--', color='orange', linewidth=1)
ax2.set_ylabel('Wind Power Trend', color='orange', fontsize=12)

# Adding grid and layout adjustments
ax1.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()