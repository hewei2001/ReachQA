import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Define the years, now spanning from 2000 to 2023
years = np.arange(2000, 2024)

# Tree data for each city (thousands of trees) expanded with more data points and tree species
city_data = {
    'City A': {
        'Oaks': np.linspace(5, 25, len(years)),
        'Maples': np.linspace(3, 15, len(years)),
        'Pines': np.linspace(2, 12, len(years)),
        'Birches': np.linspace(1, 10, len(years)),
        'Cedars': np.linspace(2, 11, len(years))
    },
    'City B': {
        'Oaks': np.linspace(4, 18, len(years)),
        'Maples': np.linspace(2, 10, len(years)),
        'Pines': np.linspace(3, 14, len(years)),
        'Birches': np.linspace(2, 9, len(years)),
        'Cedars': np.linspace(3, 8, len(years))
    },
    'City C': {
        'Oaks': np.linspace(3, 17, len(years)),
        'Maples': np.linspace(2, 13, len(years)),
        'Pines': np.linspace(4, 16, len(years)),
        'Birches': np.linspace(1, 8, len(years)),
        'Cedars': np.linspace(3, 10, len(years))
    }
}

# Additional city D
city_data['City D'] = {
    'Oaks': np.linspace(5, 20, len(years)),
    'Maples': np.linspace(4, 11, len(years)),
    'Pines': np.linspace(3, 9, len(years)),
    'Birches': np.linspace(2, 7, len(years)),
    'Cedars': np.linspace(1, 6, len(years))
}

# Colors for different tree species
colors = ['#8B4513', '#FF8C00', '#006400', '#8FBC8F', '#4682B4']

# Create a figure and axes for subplots with more cities
fig, axes = plt.subplots(2, 2, figsize=(20, 14), sharey=True)
axes = axes.flatten()  # Flatten to easily iterate

fig.suptitle('Urban Forest Diversity: Predominant Tree Species in Major Cities (2000-2023)',
             fontsize=16, weight='bold', y=1.05)

# Plot stacked bar charts for each city
for i, (city, data) in enumerate(city_data.items()):
    bottom = np.zeros_like(years, dtype=float)  # Initialize as float
    ax = axes[i]
    for j, (species, values) in enumerate(data.items()):
        ax.bar(years, values, bottom=bottom, color=colors[j], label=species)
        bottom += values
    
    # Calculate and plot trend line for total trees
    total_trees = sum(data.values())
    slope, intercept, *_ = linregress(years, total_trees)
    trendline = slope * years + intercept
    ax.plot(years, trendline, color='black', linestyle='--', label='Trendline')

    ax.set_title(city, fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_xticks(years[::2])  # Show every second year
    ax.set_xticklabels(years[::2], rotation=45)
    ax.grid(True, linestyle='--', alpha=0.5)

axes[0].set_ylabel('Number of Trees (Thousands)', fontsize=12)

# Add a legend with additional information
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=len(colors)+1, title='Tree Species', bbox_to_anchor=(0.5, 1.0))

# Adjust the layout to prevent overlap and ensure clarity
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()