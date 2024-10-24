import matplotlib.pyplot as plt
import numpy as np

# Data for urban tree planting initiative
park_sizes = np.array([2, 5, 3, 7, 10, 15, 20, 25, 30, 35, 50])
aqi_improvements = np.array([1.2, 2.5, 1.7, 3.4, 4.5, 5.2, 6.8, 7.5, 8.9, 9.3, 11.5])
years = np.array([2018, 2019, 2018, 2017, 2020, 2016, 2019, 2018, 2017, 2021, 2016])
efforts_scale = np.array([100, 150, 120, 180, 250, 300, 400, 450, 500, 550, 600])

# Cumulative efforts data for additional plot
unique_years = np.unique(years)
cumulative_efforts = np.array([efforts_scale[years == year].sum() for year in unique_years])

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# First subplot: Scatter plot
scatter = axs[0].scatter(park_sizes, aqi_improvements, c=years, s=efforts_scale, 
                         alpha=0.7, cmap='viridis', edgecolor='k')
axs[0].set_title('Impact of Urban Tree Planting on City Air Quality\nCorrelation of Park Size with AQI Improvement',
                 fontsize=14, fontweight='bold')
axs[0].set_xlabel('Park Size (Hectares)', fontsize=12)
axs[0].set_ylabel('AQI Improvement (Points)', fontsize=12)
axs[0].grid(True, linestyle='--', color='grey', alpha=0.6)

# Annotating significant parks
significant_parks = {35: 'Central Park Initiative', 50: 'Grand City Park'}
for park_size, label in significant_parks.items():
    idx = np.where(park_sizes == park_size)[0][0]
    axs[0].annotate(label,
                    xy=(park_sizes[idx], aqi_improvements[idx]),
                    xytext=(park_sizes[idx] + 2, aqi_improvements[idx] + 0.5),
                    arrowprops=dict(facecolor='black', arrowstyle='->'),
                    fontsize=10, ha='right', color='black', backgroundcolor='white')

# Adding a colorbar
cbar = fig.colorbar(scatter, ax=axs[0])
cbar.set_label('Year of Plantation', fontsize=12)

# Custom legend for point sizes
sizes = [100, 300, 500]
labels = ['Small Scale Efforts', 'Medium Scale Efforts', 'Large Scale Efforts']
handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                      markersize=np.sqrt(size), markerfacecolor='gray', alpha=0.7) for label, size in zip(labels, sizes)]
axs[0].legend(title='Effort Scale', handles=handles, loc='upper left', frameon=True, fontsize=10)

# Second subplot: Bar chart for cumulative efforts over years
axs[1].bar(unique_years, cumulative_efforts, color='darkcyan', alpha=0.8)
axs[1].set_title('Cumulative Tree Planting Efforts Over Years', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Efforts Scale', fontsize=12)
axs[1].set_xticks(unique_years)
axs[1].grid(axis='y', linestyle='--', color='grey', alpha=0.6)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plots
plt.show()