import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define years for the timeline
years = np.arange(2010, 2021)

# Renewable energy adoption data for different regions
renewable_adoption = {
    'North America': [10, 12, 13, 15, 18, 20, 23, 25, 28, 31, 35],
    'Europe': [15, 18, 21, 25, 28, 32, 36, 41, 45, 50, 55],
    'Asia': [5, 7, 10, 12, 15, 18, 20, 24, 30, 37, 45],
    'Africa': [2, 3, 5, 7, 9, 11, 13, 16, 19, 22, 26],
    'South America': [8, 10, 12, 14, 16, 20, 24, 28, 33, 38, 44]
}

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors and styles for each region
styles = {
    'North America': {'color': 'blue', 'linestyle': '-', 'marker': 'o'},
    'Europe': {'color': 'green', 'linestyle': '--', 'marker': 's'},
    'Asia': {'color': 'red', 'linestyle': '-.', 'marker': '^'},
    'Africa': {'color': 'orange', 'linestyle': ':', 'marker': 'd'},
    'South America': {'color': 'purple', 'linestyle': '-', 'marker': 'v'}
}

# Plot each region's data
for region, adoption in renewable_adoption.items():
    style = styles[region]
    ax.plot(years, adoption, label=region, **style, linewidth=2)
    # Annotate significant data points
    max_adoption_year = years[np.argmax(adoption)]
    ax.scatter(max_adoption_year, max(adoption), color=style['color'], s=100, edgecolor='black')
    for year, percent in zip(years, adoption):
        ax.annotate(f'{percent}%', (year, percent), textcoords="offset points",
                    xytext=(-10, 10), ha='center', fontsize=9,
                    color=style['color'], backgroundcolor='white', alpha=0.8)

# Add a multi-line title and axis labels
plt.title('Decade of Green:\nRenewable Energy Adoption Across Regions (2010-2020)', 
          fontsize=18, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Renewable Energy (% of Total Consumption)', fontsize=14)

# Set y-axis range, customize tick marks, and add gridlines
plt.ylim(0, 60)
plt.xticks(years)
plt.yticks(np.arange(0, 61, 5))
plt.grid(True, linestyle='--', alpha=0.6)

# Highlight periods with background shading
ax.axvspan(2010, 2015, facecolor='gray', alpha=0.1)
ax.axvspan(2015, 2020, facecolor='lightblue', alpha=0.1)

# Add a legend, positioned to avoid data occlusion
handles = [Patch(color=styles[region]['color'], label=region) for region in renewable_adoption]
plt.legend(title='Regions', handles=handles, loc='upper left', fontsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()