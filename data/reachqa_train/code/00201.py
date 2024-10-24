import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
ecoville_temps = [16, 16.1, 16.2, 16.0, 16.3, 16.5, 16.7, 16.8, 16.9, 17.0, 17.1]
megacity_temps = [18, 18.2, 18.5, 18.7, 19.0, 19.3, 19.5, 19.8, 20.0, 20.2, 20.5]

# Create plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the data
ax.plot(years, ecoville_temps, color='green', marker='o', linestyle='-', linewidth=2, markersize=6, label='EcoVille')
ax.plot(years, megacity_temps, color='red', marker='x', linestyle='-', linewidth=2, markersize=6, label='MegaCity')

# Annotating significant points with no overlap
for i, temp in enumerate(ecoville_temps):
    if i in [0, 5, 10]:  # Annotating the first, midpoint, and last year
        ax.annotate(f'{temp}°C', xy=(years[i], temp), xytext=(-40, 10), textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', color='green'), fontsize=10, color='green')

for i, temp in enumerate(megacity_temps):
    if i in [0, 5, 10]:  # Annotating the first, midpoint, and last year
        ax.annotate(f'{temp}°C', xy=(years[i], temp), xytext=(10, -15), textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', color='red'), fontsize=10, color='red')

# Title and labels
ax.set_title('Urban Temperature Trends: EcoVille vs. MegaCity\n2010-2020', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Annual Temperature (°C)', fontsize=12)

# Grid, legend, and background
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('#f7f7f7')
ax.legend(loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()