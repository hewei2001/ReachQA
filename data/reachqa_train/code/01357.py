import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2023)

# Define renewable energy data as a percentage of total energy consumption for each country
germany = np.array([10, 12, 15, 18, 22, 25, 29, 34, 38, 42, 46, 49, 52])
spain = np.array([13, 14, 16, 19, 23, 27, 30, 35, 39, 43, 47, 50, 53])
france = np.array([8, 9, 12, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41])
italy = np.array([11, 12, 14, 17, 21, 24, 28, 32, 36, 40, 44, 47, 50])
sweden = np.array([20, 22, 25, 28, 32, 36, 40, 44, 48, 51, 54, 57, 60])

# Define carbon emissions reduction data
emissions_germany = np.array([0, 1, 2, 3, 5, 8, 10, 15, 18, 20, 23, 25, 28])
emissions_spain = np.array([1, 2, 3, 5, 7, 9, 12, 16, 19, 21, 24, 27, 30])
emissions_france = np.array([0, 1, 2, 3, 5, 6, 9, 11, 14, 17, 20, 22, 25])
emissions_italy = np.array([0, 1, 3, 4, 6, 8, 11, 13, 16, 19, 22, 24, 27])
emissions_sweden = np.array([1, 2, 4, 6, 9, 11, 13, 17, 20, 23, 26, 28, 30])

# Set up the plot with a dual y-axis
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot renewable energy data
ax1.plot(years, germany, marker='o', linestyle='-', color='blue', linewidth=2, label='Germany')
ax1.plot(years, spain, marker='s', linestyle='-', color='green', linewidth=2, label='Spain')
ax1.plot(years, france, marker='^', linestyle='-', color='red', linewidth=2, label='France')
ax1.plot(years, italy, marker='D', linestyle='-', color='purple', linewidth=2, label='Italy')
ax1.plot(years, sweden, marker='*', linestyle='-', color='orange', linewidth=2, label='Sweden')

# Primary y-axis (Renewable Energy)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Energy from Renewable Sources', fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_xticklabels(years, rotation=45)
ax1.grid(True, linestyle='--', alpha=0.7)

# Create a secondary y-axis for carbon emissions
ax2 = ax1.twinx()
width = 0.5  # width of the bars

# Plot emissions reduction as a bar plot
ax2.bar(years - width/2, emissions_germany, width=width, color='blue', alpha=0.3, label='Germany Emissions')
ax2.bar(years - width/2, emissions_spain, width=width, color='green', alpha=0.3, label='Spain Emissions')
ax2.bar(years - width/2, emissions_france, width=width, color='red', alpha=0.3, label='France Emissions')
ax2.bar(years - width/2, emissions_italy, width=width, color='purple', alpha=0.3, label='Italy Emissions')
ax2.bar(years - width/2, emissions_sweden, width=width, color='orange', alpha=0.3, label='Sweden Emissions')

# Secondary y-axis (Carbon Emissions Reduction)
ax2.set_ylabel('Carbon Emissions Reduction (Million Tonnes)', fontsize=12)
ax2.set_yticks(np.arange(0, 31, 5))

# Combine legends from both plots
lines_labels_1 = ax1.get_legend_handles_labels()
lines_labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_labels_1[0] + lines_labels_2[0], lines_labels_1[1] + lines_labels_2[1], loc='upper left', fontsize=10)

# Title and layout adjustments
plt.title('Renewable Energy Adoption & Carbon Emissions Reduction in Europe (2010-2022)', fontsize=16, fontweight='bold', ha='center')
plt.tight_layout()

# Display the plot
plt.show()