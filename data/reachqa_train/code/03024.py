import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2010, 2020)

# Construct the artificial data for wheat yield (in tons per hectare)
wheat_yield = np.array([3.2, 3.4, 3.5, 3.8, 3.7, 4.0, 4.1, 4.2, 3.9, 4.3])
error = np.array([0.2, 0.25, 0.15, 0.3, 0.25, 0.3, 0.2, 0.3, 0.35, 0.3])

# Artificial data for average rainfall in millimeters
rainfall = np.array([560, 580, 600, 590, 620, 610, 625, 630, 640, 615])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the wheat yield data with error bars
ax1.errorbar(years, wheat_yield, yerr=error, fmt='-o', color='forestgreen',
             ecolor='lightcoral', elinewidth=3, capsize=4, label='Wheat Yield')
ax1.set_title('Wheat Yield and Rainfall Trends\n(2010-2019)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Yield (tons/ha)', fontsize=12, color='forestgreen')
ax1.set_xticks(years)
ax1.set_yticks(np.arange(3.0, 4.5, 0.2))
ax1.tick_params(axis='y', labelcolor='forestgreen')
ax1.grid(linestyle='--', alpha=0.7)

# Introduce a secondary y-axis for rainfall data
ax2 = ax1.twinx()
ax2.plot(years, rainfall, 's--', color='royalblue', label='Average Rainfall')
ax2.set_ylabel('Rainfall (mm)', fontsize=12, color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')
ax2.set_yticks(np.arange(550, 660, 10))

# Combining legends from both plots
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10)

# Add a narrative text for context
ax1.text(2010.5, 4.25, "Yield variability due to climatic and biological factors",
         fontsize=10, color='darkblue', bbox=dict(facecolor='lightgrey', alpha=0.5))

# Improve layout
fig.tight_layout()

# Display the plot
plt.show()