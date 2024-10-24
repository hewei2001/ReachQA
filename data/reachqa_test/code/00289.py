import matplotlib.pyplot as plt
import numpy as np

# Define the extended years and regions
years = np.arange(2010, 2023)
subregions = [
    'Northern Africa', 'Sub-Saharan Africa', 
    'East Asia', 'South Asia', 
    'Western Europe', 'Eastern Europe',
    'North America', 'Central America', 
    'South America', 
    'Australia', 'New Zealand'
]

# Expanded data for multiple indices (Happiness, Economic, Environmental)
happiness_index = np.array([
    [4.0, 4.1, 4.2, 4.3, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3],
    [3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0],
    [5.0, 5.2, 5.4, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5],
    [4.8, 4.9, 5.0, 5.2, 5.3, 5.4, 5.5, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2],
    [6.0, 6.2, 6.4, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5],
    [5.8, 5.9, 6.0, 6.1, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1],
    [7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7],
    [6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0],
    [5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7],
    [7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4],
    [7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2]
])
economic_index = happiness_index + np.random.normal(0.1, 0.2, happiness_index.shape)
environmental_index = happiness_index + np.random.normal(0.05, 0.15, happiness_index.shape)

# Set up a figure with multiple subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 18))
indices = ['Happiness Index', 'Economic Index', 'Environmental Index']
datasets = [happiness_index, economic_index, environmental_index]
cmaps = ['YlGnBu', 'Oranges', 'Purples']

for ax, data, cmap, index in zip(axes, datasets, cmaps, indices):
    # Rotate and prepare the data matrix
    data_flipped = np.flipud(data)

    # Plot the heatmap
    cax = ax.imshow(data_flipped, cmap=cmap, aspect='auto', interpolation='nearest')

    # Set axis labels and title
    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels(years, rotation=45, ha='right')
    ax.set_yticks(np.arange(len(subregions)))
    ax.set_yticklabels(reversed(subregions))
    ax.set_title(f'Global {index} Across Subregions (2010-2022)', fontsize=14, pad=15)

    # Add a color bar
    cbar = fig.colorbar(cax, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label(f'{index} (1-10)', rotation=270, labelpad=15)

    # Annotate each cell with the index value
    for i in range(data_flipped.shape[0]):
        for j in range(data_flipped.shape[1]):
            text = ax.text(j, i, f'{data_flipped[i, j]:.1f}',
                           ha='center', va='center', color='black', fontsize=8)

# Adjust layout to ensure readability
plt.tight_layout()

# Display the plot
plt.show()