import matplotlib.pyplot as plt
import numpy as np

# Define additional cities and expand the data
cities = [
    'Metropolis', 'Gotham', 'Star City', 'Central City', 'Atlantis',
    'Coast City', 'National City', 'Blüdhaven', 'Fawcett City', 'Smallville'
]

# Expanded hypothetical monthly PM2.5 concentration data for each city in µg/m^3
pm25_data = [
    [30, 28, 35, 33, 26, 29, 32, 31, 27, 25, 30, 28, 34, 32, 30, 33],  # Metropolis
    [45, 47, 44, 46, 50, 52, 48, 49, 51, 53, 47, 46, 54, 55, 50, 48],  # Gotham
    [15, 18, 16, 20, 19, 21, 17, 22, 20, 18, 16, 19, 23, 21, 19, 18],  # Star City
    [25, 27, 24, 29, 31, 30, 28, 26, 23, 25, 27, 28, 29, 26, 24, 27],  # Central City
    [40, 42, 39, 43, 38, 44, 45, 41, 46, 44, 42, 40, 47, 43, 39, 41],  # Atlantis
    [28, 30, 27, 29, 31, 33, 29, 30, 32, 34, 30, 28, 27, 31, 30, 28],  # Coast City
    [22, 24, 21, 23, 27, 26, 25, 22, 28, 24, 23, 21, 25, 27, 24, 22],  # National City
    [37, 39, 36, 38, 41, 42, 40, 39, 43, 41, 38, 37, 40, 42, 39, 37],  # Blüdhaven
    [32, 34, 31, 33, 36, 35, 34, 32, 37, 35, 33, 31, 36, 34, 32, 33],  # Fawcett City
    [18, 20, 17, 19, 23, 22, 20, 18, 24, 20, 19, 17, 21, 23, 18, 19]   # Smallville
]

# Create a subplot with a second plot for additional analysis
fig, ax1 = plt.subplots(figsize=(14, 10))
ax2 = ax1.twinx()

# Create a vertical box plot
box = ax1.boxplot(pm25_data, vert=True, patch_artist=True, notch=True,
                  positions=np.arange(1, len(cities) + 1),
                  boxprops=dict(facecolor='lightblue', color='darkblue', linewidth=1.5),
                  whiskerprops=dict(color='darkblue', linewidth=1.5),
                  capprops=dict(color='darkblue', linewidth=1.5),
                  medianprops=dict(color='red', linewidth=2),
                  flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none'))

# Overlay a plot of the mean values with a line for each city
mean_values = [np.mean(data) for data in pm25_data]
ax2.plot(np.arange(1, len(cities) + 1), mean_values, color='green', linestyle='--', marker='D', label='Mean Values', linewidth=2)

# Add annotations for mean values
for i, mean in enumerate(mean_values, start=1):
    ax2.annotate(f'{mean:.1f}', (i, mean), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Set chart title and labels
ax1.set_title('Comparative Urban Air Quality Across Various Cities: PM2.5 Concentration Analysis', fontsize=15, pad=20)
ax1.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax2.set_ylabel('Mean PM2.5 Concentration (µg/m³)', fontsize=12)
ax1.set_xticks(np.arange(1, len(cities) + 1))
ax1.set_xticklabels(cities, rotation=30, fontsize=11)

# Add grid for readability and manage layout
ax1.grid(True, linestyle='--', alpha=0.7, axis='y')
fig.tight_layout()

# Add legend for the mean values line
ax2.legend(loc='upper right', fontsize=10)

# Display the plot
plt.show()