import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1960s to the 2020s
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Hypothetical number of solar flares detected each decade
solar_flares = np.array([120, 150, 180, 210, 260, 230, 270])

# Set up the plot
plt.figure(figsize=(12, 7))

# Plot the line chart
plt.plot(decades, solar_flares, color='orange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Solar Flares Detected')

# Title and labels
plt.title('Solar Flare Detection over Decades\nMonitoring Frequency for Space Weather Analysis', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Number of Solar Flares', fontsize=14)

# Annotate significant events in solar activity
annotations = [
    ("Cycle 20 Peak", 1960, 120),
    ("Cycle 21 Peak", 1980, 180),
    ("Cycle 22 Peak", 1990, 210),
    ("Halloween Storms", 2000, 260),
    ("Solar Cycle 24", 2010, 230),
    ("Cycle 25 Surge", 2020, 270)
]
for text, x, y in annotations:
    plt.annotate(text, xy=(x, y), xytext=(-60, 10),
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", color='grey'), fontsize=10)

# Customize the grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=True)

# Adjust layout to avoid clipping
plt.tight_layout()

# Display the chart
plt.show()