import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

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
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each sector's index data with error bars
ax.errorbar(years, healthcare_index, yerr=healthcare_std, label='Healthcare', fmt='-o', color='#1f77b4', alpha=0.8, ecolor='lightblue', elinewidth=2, capsize=4)
ax.errorbar(years, manufacturing_index, yerr=manufacturing_std, label='Manufacturing', fmt='-^', color='#2ca02c', alpha=0.8, ecolor='lightgreen', elinewidth=2, capsize=4)
ax.errorbar(years, agriculture_index, yerr=agriculture_std, label='Agriculture', fmt='-s', color='#ff7f0e', alpha=0.8, ecolor='peachpuff', elinewidth=2, capsize=4)
ax.errorbar(years, retail_index, yerr=retail_std, label='Retail', fmt='-d', color='#9467bd', alpha=0.8, ecolor='thistle', elinewidth=2, capsize=4)
ax.errorbar(years, defense_index, yerr=defense_std, label='Defense', fmt='-x', color='#d62728', alpha=0.8, ecolor='lightcoral', elinewidth=2, capsize=4)

# Add title and labels
ax.set_title("Robotic Innovation Index (2018-2022)\nAcross Different Sectors", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Innovation Index", fontsize=14)

# Set x-ticks to show years and adjust their size
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=12)
ax.set_yticks(np.arange(35, 101, 5))
ax.set_yticklabels(np.arange(35, 101, 5), fontsize=12)

# Minor ticks for more granularity
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

# Add a legend
ax.legend(loc='upper left', fontsize=12, frameon=False)

# Enable grid
ax.grid(True, linestyle='--', which='major', alpha=0.5)

# Annotate points of interest
for i, txt in enumerate(healthcare_index):
    ax.annotate(f'{txt}', (years[i], healthcare_index[i]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=10, color='blue')

# Additional subplot for mean trend line
mean_index = (healthcare_index + manufacturing_index + agriculture_index + retail_index + defense_index) / 5
ax.plot(years, mean_index, linestyle='--', color='black', label='Average Index', linewidth=1.5)
ax.annotate('Average Trend', xy=(2022, mean_index[-1]), xytext=(2022, mean_index[-1]+2), fontsize=11, ha='center', color='black', arrowprops=dict(facecolor='black', shrink=0.05))

# Adjust layout to ensure no overlap
plt.tight_layout()

# Show the plot
plt.show()