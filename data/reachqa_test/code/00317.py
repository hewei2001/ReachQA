import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
amenities = ['Walking Trails', 'Playgrounds', 'Sports Courts', 'Picnic Areas']

# Visits data in thousands
visits_data = np.array([
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],  # Walking Trails
    [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],  # Playgrounds
    [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],  # Sports Courts
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]   # Picnic Areas
])

# Hypothetical average duration of visits (hours)
duration_data = np.array([
    [1.5, 1.7, 1.8, 2.0, 2.1, 2.2, 2.4, 2.5, 2.6, 2.8, 3.0],  # Walking Trails
    [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2],  # Playgrounds
    [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],  # Sports Courts
    [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]   # Picnic Areas
])

# Create subplots: 1 row, 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), constrained_layout=True)

# Stacked Area Chart
ax1.stackplot(years, visits_data, labels=amenities, 
              colors=['#6baed6', '#fd8d3c', '#31a354', '#756bb1'], alpha=0.8)
ax1.set_title('Rising Trends in Urban Green Spaces:\nCity Park Utilization (2010-2020)', 
              fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Visits (in thousands)', fontsize=12)
ax1.legend(loc='upper left', title='Amenities', fontsize=10, bbox_to_anchor=(1.02, 1))
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.grid(True, linestyle='--', alpha=0.7)

# Line Plot for Average Duration
for i, amenity in enumerate(amenities):
    ax2.plot(years, duration_data[i], marker='o', label=amenity)
ax2.set_title('Average Duration of Visits\nby Amenity (2010-2020)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Duration (hours)', fontsize=12)
ax2.legend(loc='upper left', title='Amenities', fontsize=10)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.grid(True, linestyle='--', alpha=0.7)

# Display the charts
plt.show()