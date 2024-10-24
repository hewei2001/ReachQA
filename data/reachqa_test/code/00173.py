import matplotlib.pyplot as plt
import numpy as np

# Regions and Seasons
regions = ['North', 'South', 'East', 'West']
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

# Sightings data for each species in each season per region
sightings = {
    'Sparrows': [120, 150, 200, 250],
    'Pigeons': [180, 130, 220, 270],
    'Robins': [90, 160, 180, 210],
    'Starlings': [130, 170, 230, 280]
}

# Aggregate seasonal data across regions for line plot
seasonal_totals = np.array([
    [np.mean([sightings['Sparrows'][i], sightings['Pigeons'][i], 
              sightings['Robins'][i], sightings['Starlings'][i]]) for i in range(len(regions))]
    for _ in range(len(seasons))
]).T

# Prepare data for plotting
positions = np.arange(len(regions))
sparrows = np.array(sightings['Sparrows'])
pigeons = np.array(sightings['Pigeons'])
robins = np.array(sightings['Robins'])
starlings = np.array(sightings['Starlings'])

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Stacked Bar Chart
ax1.bar(positions, sparrows, label='Sparrows', color='saddlebrown', alpha=0.7)
ax1.bar(positions, pigeons, bottom=sparrows, label='Pigeons', color='gray', alpha=0.7)
ax1.bar(positions, robins, bottom=sparrows + pigeons, label='Robins', color='red', alpha=0.7)
ax1.bar(positions, starlings, bottom=sparrows + pigeons + robins, label='Starlings', color='purple', alpha=0.7)
ax1.set_ylabel('Number of Sightings')
ax1.set_xlabel('Regions')
ax1.set_title('Seasonal Trends in Urban Bird Watching\nA Study of Common Sightings', fontsize=14, weight='bold')
ax1.set_xticks(positions)
ax1.set_xticklabels(regions)
ax1.legend(title='Bird Species', bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Line Plot for Seasonal Trends
for i, season in enumerate(seasons):
    ax2.plot(regions, seasonal_totals[:, i], marker='o', label=season)
ax2.set_ylabel('Average Sightings per Species')
ax2.set_xlabel('Regions')
ax2.set_title('Average Bird Sightings Per Season Across Regions', fontsize=12, weight='bold')
ax2.legend(title='Seasons', bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Show the plot
plt.show()