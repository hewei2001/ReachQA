import matplotlib.pyplot as plt

# Data for grape yields in tons over the years 2015-2020
bordeaux_yields = [15, 18, 14, 20, 16, 19]
napa_valley_yields = [22, 24, 23, 26, 25, 24]
tuscany_yields = [14, 16, 15, 17, 14, 16]
rioja_yields = [13, 15, 12, 14, 13, 15]
marlborough_yields = [17, 19, 18, 20, 17, 19]

# Organize data for box plot
yield_data = [
    bordeaux_yields,
    napa_valley_yields,
    tuscany_yields,
    rioja_yields,
    marlborough_yields
]

# Define labels for the wine regions
regions = ['Bordeaux', 'Napa Valley', 'Tuscany', 'Rioja', 'Marlborough']

# Create the plot
plt.figure(figsize=(12, 7))

# Create boxplot
plt.boxplot(yield_data, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightblue', color='darkblue', linewidth=1.5),
            whiskerprops=dict(color='darkblue', linewidth=1.5),
            capprops=dict(color='darkblue', linewidth=1.5),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', color='darkblue', alpha=0.5))

# Title and axis labels
plt.title('Annual Distribution of Harvest Yields in Different Wine Regions\n(2015-2020)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Wine Regions', fontsize=12)
plt.ylabel('Grape Yields (Tons)', fontsize=12)

# Set x-tick labels
plt.xticks(ticks=range(1, len(regions)+1), labels=regions, rotation=15)

# Add a grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show plot
plt.show()