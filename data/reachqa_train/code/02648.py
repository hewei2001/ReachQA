import matplotlib.pyplot as plt
import numpy as np

# Data for urban tree planting initiative
park_sizes = np.array([2, 5, 3, 7, 10, 15, 20, 25, 30, 35, 50])  # Park size in hectares
aqi_improvements = np.array([1.2, 2.5, 1.7, 3.4, 4.5, 5.2, 6.8, 7.5, 8.9, 9.3, 11.5])  # AQI Improvement
years = np.array([2018, 2019, 2018, 2017, 2020, 2016, 2019, 2018, 2017, 2021, 2016])  # Year of plantation
efforts_scale = np.array([100, 150, 120, 180, 250, 300, 400, 450, 500, 550, 600])  # Scale of tree planting efforts

# Plotting the scatter chart
plt.figure(figsize=(12, 8))
scatter = plt.scatter(park_sizes, aqi_improvements, c=years, s=efforts_scale, alpha=0.7, cmap='viridis', edgecolor='k')

# Title and axis labels
plt.title('Impact of Urban Tree Planting on City Air Quality\nCorrelation of Park Size with AQI Improvement',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Park Size (Hectares)', fontsize=12)
plt.ylabel('AQI Improvement (Points)', fontsize=12)

# Adding a colorbar to indicate the year of plantation
cbar = plt.colorbar(scatter)
cbar.set_label('Year of Plantation', fontsize=12)

# Annotating significant park improvements
significant_parks = {35: 'Central Park Initiative', 50: 'Grand City Park'}

for park_size, label in significant_parks.items():
    idx = np.where(park_sizes == park_size)[0][0]
    plt.annotate(label,
                 xy=(park_sizes[idx], aqi_improvements[idx]),
                 xytext=(park_sizes[idx] + 2, aqi_improvements[idx] + 0.5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, ha='right', color='black', backgroundcolor='white')

# Custom legend for point sizes
sizes = [100, 300, 500]
labels = ['Small Scale Efforts', 'Medium Scale Efforts', 'Large Scale Efforts']
handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                      markersize=np.sqrt(size), markerfacecolor='gray', alpha=0.7) for label, size in zip(labels, sizes)]
plt.legend(title='Effort Scale', handles=handles, loc='upper left', frameon=True, fontsize=10)

# Adding grid for better readability
plt.grid(True, linestyle='--', color='grey', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()