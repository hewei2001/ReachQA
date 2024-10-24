import matplotlib.pyplot as plt
import numpy as np

# Define the years for the analysis
years = np.arange(2010, 2021)

# Crop yield data in tons per hectare (modified for better distribution)
wheat_yield = [3.2, 3.35, 3.55, 3.75, 3.9, 4.0, 4.05, 4.25, 4.35, 4.45, 4.6]
corn_yield = [4.1, 4.25, 4.45, 4.6, 4.75, 4.85, 5.0, 5.1, 5.2, 5.35, 5.5]

# Related dataset: Average rainfall in mm (modified for more variability)
rainfall = [300, 315, 305, 335, 345, 355, 365, 375, 385, 395, 410]

# Create a figure and primary axis for crop yields
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting wheat and corn yields
ax1.plot(years, wheat_yield, marker='s', linestyle='-', color='gold', label='Wheat Yield', linewidth=2, markersize=7)
ax1.plot(years, corn_yield, marker='o', linestyle='-', color='cornflowerblue', label='Corn Yield', linewidth=2, markersize=7)

# Set title and labels for the primary axis
ax1.set_title('Valley of Bounty: Crop Yield and Rainfall (2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Yield (tons/ha)', fontsize=12)

# Customize x-ticks and y-ticks for the primary axis
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend for crop yields
ax1.legend(title='Crops', fontsize=10, title_fontsize=11, loc='upper left')

# Create a secondary axis for rainfall
ax2 = ax1.twinx()
ax2.bar(years, rainfall, alpha=0.5, color='slategray', label='Average Rainfall', width=0.4, align='center')
ax2.set_ylabel('Rainfall (mm)', fontsize=12)
ax2.yaxis.grid(False)

# Add a legend for rainfall
ax2.legend(title='Environmental Factors', fontsize=10, title_fontsize=11, loc='upper right')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()