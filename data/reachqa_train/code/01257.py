import matplotlib.pyplot as plt
import numpy as np

# Data for the line chart with error bars
years = np.array([1970, 1980, 1990, 2000, 2010])
guitars_production = np.array([120, 150, 180, 210, 250])
pianos_production = np.array([60, 75, 70, 85, 90])
violins_production = np.array([40, 50, 55, 60, 65])

# Errors for each production type
guitars_error = np.array([10, 12, 8, 10, 9])
pianos_error = np.array([5, 7, 6, 5, 6])
violins_error = np.array([3, 4, 3, 4, 3])

# Create the figure and axis
plt.figure(figsize=(10, 6))

# Plotting the line chart with error bars
plt.errorbar(years, guitars_production, yerr=guitars_error, fmt='-o', color='goldenrod',
             ecolor='lightgrey', capsize=4, elinewidth=1.5, alpha=0.9, label='Guitars')
plt.errorbar(years, pianos_production, yerr=pianos_error, fmt='-s', color='royalblue',
             ecolor='lightgrey', capsize=4, elinewidth=1.5, alpha=0.9, label='Pianos')
plt.errorbar(years, violins_production, yerr=violins_error, fmt='-^', color='forestgreen',
             ecolor='lightgrey', capsize=4, elinewidth=1.5, alpha=0.9, label='Violins')

# Customize the plot with title and labels
plt.title("Crescendo of Sound:\nMusical Instrument Production Trends (1970-2010)", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Production (in Thousands)", fontsize=12)

# Custom ticks and grid
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 300, 50))
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(title="Instruments", loc='upper left', fontsize='medium')

# Tight layout adjustment for readability
plt.tight_layout()

# Show the plot
plt.show()