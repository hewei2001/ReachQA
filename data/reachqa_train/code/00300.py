import matplotlib.pyplot as plt
import numpy as np

# Define continents and milestone years
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
years = ['2000', '2005', '2010', '2015', '2020']

# Internet access data (% of population)
connectivity_data = np.array([
    [2, 5, 10, 25, 40],   # Africa
    [10, 20, 30, 50, 70],  # Asia
    [30, 50, 70, 80, 90],  # Europe
    [40, 60, 75, 85, 95],  # North America
    [10, 20, 35, 50, 65],  # South America
    [50, 60, 70, 85, 90]   # Australia
])

# Calculate average connectivity over years for overlay
average_connectivity = np.mean(connectivity_data, axis=0)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Heatmap for Internet access data
cax = ax1.imshow(connectivity_data, cmap='Blues', aspect='auto', interpolation='nearest')

# Add color bar
cbar = fig.colorbar(cax, ax=ax1, pad=0.02)
cbar.set_label('Internet Access (% of population)', fontsize=12)

# Set axis labels and ticks for the heatmap
ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years, fontsize=11, rotation=45)
ax1.set_yticks(np.arange(len(continents)))
ax1.set_yticklabels(continents, fontsize=11)

# Annotate each cell with the connectivity value
for i in range(len(continents)):
    for j in range(len(years)):
        ax1.text(j, i, f'{connectivity_data[i, j]}%', ha='center', va='center', color='black', fontsize=10)

# Enable gridlines
ax1.grid(which='major', color='gray', linestyle='--', linewidth=0.5)

# Secondary y-axis for the average connectivity line plot
ax2 = ax1.twinx()
ax2.plot(years, average_connectivity, color='red', marker='o', linestyle='-', linewidth=2, label='Avg Connectivity')
ax2.set_ylabel('Average Connectivity (%)', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')

# Multi-line title
plt.title('Mapping the Evolution of Internet Connectivity\nAcross Continents (2000-2020) with Average Trend Overlay', fontsize=16, fontweight='bold')

# Add legend for the line plot
ax2.legend(loc='upper left', bbox_to_anchor=(0.85, 0.95), fontsize=10)

# Adjust layout to prevent clipping of tick-labels and titles
plt.tight_layout()

# Display the plot
plt.show()