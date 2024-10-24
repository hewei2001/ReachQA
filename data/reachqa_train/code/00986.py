import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

# Data for vacation destinations
regions = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania']
tourist_percentages = [30, 25, 20, 10, 10, 5]

# Extended data for an additional visualization
yearly_data = {
    'Europe': [25, 28, 30, 29, 30],
    'Asia': [20, 22, 24, 24, 25],
    'North America': [18, 19, 20, 20, 20],
    'South America': [8, 9, 10, 10, 10],
    'Africa': [7, 8, 9, 9, 10],
    'Oceania': [4, 5, 5, 5, 5]
}
years = [2019, 2020, 2021, 2022, 2023]

# Colors for each region
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a figure and a set of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Pie chart with gradient wedges
wedges, texts, autotexts = ax1.pie(
    tourist_percentages,
    labels=regions,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2, linestyle='-'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Customize the text properties
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10)

# Title configuration
ax1.set_title('Global Travel Resurgence in 2023:\nPopular Vacation Destinations', fontsize=14, fontweight='bold', pad=20)

# Adding a central circle for the donut appearance
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

# Line plot showing yearly trends
for region, color in zip(yearly_data.keys(), colors):
    ax2.plot(years, yearly_data[region], label=region, marker='o', color=color)

ax2.set_title('Trends in Tourist Percentages (2019-2023)', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Year')
ax2.set_ylabel('Percentage (%)')
ax2.legend(title="Regions", bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(True)

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Display the plot
plt.show()