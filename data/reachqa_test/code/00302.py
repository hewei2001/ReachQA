import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Patch

# Initialize Seaborn with the desired style
sns.set(style='darkgrid')

# Define years
years = np.arange(2025, 2035)

# Mission data for each agency
missions_nasa = np.array([12, 15, 14, 18, 20, 17, 22, 25, 24, 28])
errors_nasa = np.array([1, 1.5, 1, 2, 1.5, 1, 2, 2.5, 1.5, 3])

missions_esa = np.array([10, 12, 13, 15, 16, 17, 18, 19, 20, 22])
errors_esa = np.array([1, 1, 1, 1.5, 1, 1.5, 1, 2, 1.5, 2])

missions_cnsa = np.array([8, 11, 10, 13, 15, 14, 16, 17, 19, 21])
errors_cnsa = np.array([0.5, 1, 0.5, 1.5, 1, 1.5, 1, 2, 2.5, 1.5])

# Create plot with enhanced style
plt.figure(figsize=(16, 10))

# Plot with error bars for each agency with enhanced styles
plt.errorbar(years, missions_nasa, yerr=errors_nasa, label='NASA', fmt='-o', capsize=5, color='royalblue', alpha=0.9, linestyle='--', linewidth=2)
plt.errorbar(years, missions_esa, yerr=errors_esa, label='ESA', fmt='-s', capsize=5, color='forestgreen', alpha=0.9, linestyle=':', linewidth=2)
plt.errorbar(years, missions_cnsa, yerr=errors_cnsa, label='CNSA', fmt='-^', capsize=5, color='firebrick', alpha=0.9, linestyle='-.', linewidth=2)

# Add annotations for key data points
max_missions = np.max([missions_nasa, missions_esa, missions_cnsa])
for i, year in enumerate(years):
    if missions_nasa[i] == max_missions or missions_esa[i] == max_missions or missions_cnsa[i] == max_missions:
        plt.annotate(f'{year}', (year, max_missions + 1), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, fontweight='bold')

# Add title, labels, and legend
plt.title("Annual Space Missions (2025-2034)\nRenaissance of Space Exploration", fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Missions', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, max_missions + 5, 2))
plt.legend(title='Space Agencies', loc='upper left', fontsize=12)

# Grid for better readability
plt.grid(axis='both', linestyle='--', alpha=0.5)

# Add a custom legend with patches
legend_elements = [Patch(facecolor='royalblue', edgecolor='w', label='NASA'),
                   Patch(facecolor='forestgreen', edgecolor='w', label='ESA'),
                   Patch(facecolor='firebrick', edgecolor='w', label='CNSA')]
plt.legend(handles=legend_elements, title='Space Agencies', loc='upper left')

# Layout adjustment
plt.tight_layout()

# Display plot
plt.show()