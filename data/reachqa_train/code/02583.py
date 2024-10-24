import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array([2018, 2019, 2020, 2021, 2022])

# Robotic Innovation Index values for each sector (hypothetical values)
healthcare_index = np.array([70, 75, 82, 88, 94])
manufacturing_index = np.array([65, 70, 75, 80, 90])
agriculture_index = np.array([50, 55, 62, 70, 78])
retail_index = np.array([40, 45, 50, 52, 55])
defense_index = np.array([80, 85, 87, 90, 95])

# Standard deviations representing variability in the index
healthcare_std = np.array([2, 3, 3, 2, 2])
manufacturing_std = np.array([2, 2, 3, 3, 2])
agriculture_std = np.array([3, 2, 4, 3, 4])
retail_std = np.array([3, 2, 2, 3, 2])
defense_std = np.array([1, 1, 2, 2, 1])

# Plotting
plt.figure(figsize=(12, 8))

# Plot each sector's index data with error bars
plt.errorbar(years, healthcare_index, yerr=healthcare_std, label='Healthcare', fmt='-o', color='blue', ecolor='lightblue', elinewidth=2, capsize=4)
plt.errorbar(years, manufacturing_index, yerr=manufacturing_std, label='Manufacturing', fmt='-^', color='green', ecolor='lightgreen', elinewidth=2, capsize=4)
plt.errorbar(years, agriculture_index, yerr=agriculture_std, label='Agriculture', fmt='-s', color='orange', ecolor='peachpuff', elinewidth=2, capsize=4)
plt.errorbar(years, retail_index, yerr=retail_std, label='Retail', fmt='-d', color='purple', ecolor='thistle', elinewidth=2, capsize=4)
plt.errorbar(years, defense_index, yerr=defense_std, label='Defense', fmt='-x', color='red', ecolor='lightcoral', elinewidth=2, capsize=4)

# Add title and labels
plt.title("Robotic Innovation Index (2018-2022)\nAcross Different Sectors", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Innovation Index", fontsize=14)

# Set x-ticks to show years and adjust their size
plt.xticks(years, fontsize=12)
plt.yticks(fontsize=12)

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=False)

# Enable grid
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Show the plot
plt.show()