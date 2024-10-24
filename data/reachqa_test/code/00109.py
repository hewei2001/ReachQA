import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
parks = ['Central Park', 'Riverside Park', 'Greenbelt', 'Meadowlands', 'Lakeview Park']
sightings = {
    'Sparrows': [120, 150, 100, 80, 90],
    'Pigeons': [200, 170, 90, 160, 110],
    'Starlings': [80, 60, 40, 70, 60],
    'Finches': [40, 30, 50, 20, 30]
}

# Data for the new line chart (Seasonal data for Pigeons sightings)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
pigeon_sightings_by_month = [50, 60, 55, 70, 65, 80, 75, 95, 85, 110, 120, 115]

# Define the positions and width for the bars
bar_width = 0.2
index = np.arange(len(parks))

# Create a figure and axis for subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Bar chart for bird sightings
ax1 = axes[0]
for i, (species, counts) in enumerate(sightings.items()):
    ax1.bar(index + i * bar_width, counts, bar_width, label=species, alpha=0.7)

# Set titles and labels for the bar chart
ax1.set_title('Feathered Friends in Avian City\nBird Species Sightings Across Urban Parks', fontsize=14, weight='bold', pad=15)
ax1.set_xlabel('Urban Parks', fontsize=11)
ax1.set_ylabel('Number of Sightings', fontsize=11)
ax1.set_xticks(index + bar_width * 1.5)
ax1.set_xticklabels(parks, rotation=30, ha='right', fontsize=10)
ax1.legend(title='Bird Species', fontsize=10, title_fontsize=11)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Second subplot: Line chart for monthly Pigeons sightings
ax2 = axes[1]
ax2.plot(months, pigeon_sightings_by_month, marker='o', linestyle='-', color='purple', label='Pigeons', linewidth=2)

# Set titles and labels for the line chart
ax2.set_title('Monthly Trend of Pigeon Sightings', fontsize=14, weight='bold', pad=15)
ax2.set_xlabel('Months', fontsize=11)
ax2.set_ylabel('Number of Sightings', fontsize=11)
ax2.legend(fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()