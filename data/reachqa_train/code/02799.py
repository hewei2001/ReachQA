import matplotlib.pyplot as plt
import numpy as np

# Data preparation
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
solar_flares = np.array([120, 150, 180, 210, 260, 230, 270])
sunspots = np.array([90, 110, 160, 190, 230, 200, 240])  # Hypothetical sunspot numbers

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plot the line chart for solar flares
axs[0].plot(decades, solar_flares, color='orange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Solar Flares Detected')
axs[0].set_title('Solar Flare Detection over Decades\nMonitoring Frequency for Space Weather Analysis', fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel('Decade', fontsize=12)
axs[0].set_ylabel('Number of Solar Flares', fontsize=12)
annotations = [("Cycle 20 Peak", 1960, 120), ("Cycle 21 Peak", 1980, 180), ("Cycle 22 Peak", 1990, 210), ("Halloween Storms", 2000, 260), ("Solar Cycle 24", 2010, 230), ("Cycle 25 Surge", 2020, 270)]
for text, x, y in annotations:
    axs[0].annotate(text, xy=(x, y), xytext=(-60, 10), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='grey'), fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', fontsize=10, frameon=True)

# Plot the bar chart for sunspots
axs[1].bar(decades, sunspots, color='blue', alpha=0.7, label='Average Sunspots per Decade')
axs[1].set_title('Average Sunspots per Decade\nCorrelation with Solar Flares', fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel('Decade', fontsize=12)
axs[1].set_ylabel('Average Number of Sunspots', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6, axis='y')
axs[1].legend(loc='upper left', fontsize=10, frameon=True)

# Adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the charts
plt.show()