import matplotlib.pyplot as plt
import numpy as np

# Define the cities
cities = ['Metropolis', 'Gotham', 'Star City', 'Central City', 'Atlantis']

# Hypothetical monthly PM2.5 concentration data for each city in µg/m^3
pm25_data = [
    [30, 28, 35, 33, 26, 29, 32, 31, 27, 25, 30, 28],  # Metropolis
    [45, 47, 44, 46, 50, 52, 48, 49, 51, 53, 47, 46],  # Gotham
    [15, 18, 16, 20, 19, 21, 17, 22, 20, 18, 16, 19],  # Star City
    [25, 27, 24, 29, 31, 30, 28, 26, 23, 25, 27, 28],  # Central City
    [40, 42, 39, 43, 38, 44, 45, 41, 46, 44, 42, 40]   # Atlantis
]

# Create a vertical box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(pm25_data, vert=True, patch_artist=True, notch=True,
                  positions=np.arange(1, len(cities) + 1),
                  boxprops=dict(facecolor='lightblue', color='darkblue', linewidth=1.5),
                  whiskerprops=dict(color='darkblue', linewidth=1.5),
                  capprops=dict(color='darkblue', linewidth=1.5),
                  medianprops=dict(color='red', linewidth=2),
                  flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none'))

# Customize the appearance of the boxplot
for patch in box['boxes']:
    patch.set_facecolor('lightblue')

# Set chart title and labels
plt.title('Annual PM2.5 Levels: Urban Air Quality Across Cities', fontsize=16, pad=20)
plt.ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
plt.xticks(np.arange(1, len(cities) + 1), cities, rotation=30, fontsize=11)

# Add grid for readability
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()