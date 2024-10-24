import matplotlib.pyplot as plt

# Expanded Data for grape yields in tons over the years 2010-2023
bordeaux_yields = [13, 16, 15, 18, 14, 20, 16, 19, 17, 18, 15, 19, 20, 18]
napa_valley_yields = [21, 23, 22, 24, 23, 26, 25, 24, 27, 26, 25, 28, 29, 27]
tuscany_yields = [12, 14, 13, 16, 15, 17, 14, 16, 15, 17, 16, 18, 17, 18]
rioja_yields = [11, 13, 12, 15, 12, 14, 13, 15, 14, 16, 13, 17, 15, 16]
marlborough_yields = [16, 18, 17, 19, 18, 20, 17, 19, 18, 21, 20, 22, 19, 21]
barossa_valley_yields = [14, 15, 14, 17, 15, 18, 14, 18, 16, 19, 17, 20, 18, 17]
piedmont_yields = [12, 15, 14, 17, 16, 17, 15, 18, 15, 18, 17, 19, 17, 16]

# Organize data for box plot
yield_data = [
    bordeaux_yields,
    napa_valley_yields,
    tuscany_yields,
    rioja_yields,
    marlborough_yields,
    barossa_valley_yields,
    piedmont_yields
]

# Define labels for the wine regions
regions = ['Bordeaux', 'Napa Valley', 'Tuscany', 'Rioja', 'Marlborough', 'Barossa Valley', 'Piedmont']

# Create the figure and axis
fig, ax = plt.subplots(2, 1, figsize=(14, 10))

# Create boxplot
ax[0].boxplot(yield_data, patch_artist=True, notch=True,
              boxprops=dict(facecolor='lightgreen', color='darkgreen', linewidth=1.5),
              whiskerprops=dict(color='darkgreen', linewidth=1.5),
              capprops=dict(color='darkgreen', linewidth=1.5),
              medianprops=dict(color='red', linewidth=2),
              flierprops=dict(marker='o', color='darkgreen', alpha=0.5))

# Title and axis labels
ax[0].set_title('Annual Distribution of Harvest Yields in Various Wine Regions\n(2010-2023)', fontsize=14, fontweight='bold', pad=15)
ax[0].set_xlabel('Wine Regions', fontsize=12)
ax[0].set_ylabel('Grape Yields (Tons)', fontsize=12)

# Set x-tick labels
ax[0].set_xticklabels(regions, rotation=15)

# Add a grid for readability
ax[0].grid(axis='y', linestyle='--', alpha=0.6)

# Additional subplot: Line plot of average yields over the years
years = list(range(2010, 2024))
# Calculate average yields for each year across all regions
average_yields_per_year = [
    sum(yields) / len(yields) for yields in zip(*yield_data)
]

# Line plot
ax[1].plot(years, average_yields_per_year, marker='o', color='darkblue', linewidth=2, label='Average Yields')
ax[1].set_title('Average Grape Yields Over the Years', fontsize=12, fontweight='bold', pad=10)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Average Grape Yields (Tons)', fontsize=12)
ax[1].set_xticks(years)
ax[1].legend()
ax[1].grid(linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()