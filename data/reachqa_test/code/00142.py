import matplotlib.pyplot as plt
import numpy as np

# Define years and corresponding growth data for each environmental condition
years = np.arange(2015, 2023)
growth_dry = np.array([10, 11, 12, 13, 14, 14.5, 15, 15.5])
growth_moderate = np.array([15, 16, 17, 18, 19, 20, 21, 22])
growth_humid = np.array([12, 13, 14, 15, 16, 17, 18, 19])

# Standard deviations for growth data
std_dry = np.array([1] * len(growth_dry))
std_moderate = np.array([1.5] * len(growth_moderate))
std_humid = np.array([0.8] * len(growth_humid))

# Hypothetical average precipitation data (mm/year)
precipitation_dry = np.array([200, 220, 230, 240, 250, 255, 260, 265])
precipitation_moderate = np.array([500, 520, 530, 540, 550, 560, 570, 580])
precipitation_humid = np.array([800, 820, 830, 850, 870, 880, 890, 900])

# Create the figure and two subplots side by side
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), constrained_layout=True)

# Plot the growth data with error bars on the first subplot
axes[0].errorbar(years, growth_dry, yerr=std_dry, fmt='-o', color='sandybrown', capsize=5, label='Dry', alpha=0.9)
axes[0].errorbar(years, growth_moderate, yerr=std_moderate, fmt='-o', color='forestgreen', capsize=5, label='Moderate', alpha=0.9)
axes[0].errorbar(years, growth_humid, yerr=std_humid, fmt='-o', color='royalblue', capsize=5, label='Humid', alpha=0.9)
axes[0].set_title("Annual Growth of Arboreus magnificus\nUnder Different Environmental Conditions (2015-2022)", fontsize=14, weight='bold')
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Average Growth Height (cm)", fontsize=12)
axes[0].grid(linestyle='--', alpha=0.6)
axes[0].legend(loc='upper left', fontsize=10)
axes[0].set_xticks(years)
axes[0].set_xlim(years[0] - 0.5, years[-1] + 0.5)

# Plot the precipitation data on the second subplot
width = 0.25
axes[1].bar(years - width, precipitation_dry, width=width, color='sandybrown', label='Dry', alpha=0.8)
axes[1].bar(years, precipitation_moderate, width=width, color='forestgreen', label='Moderate', alpha=0.8)
axes[1].bar(years + width, precipitation_humid, width=width, color='royalblue', label='Humid', alpha=0.8)
axes[1].set_title("Average Precipitation\nfor Different Conditions (2015-2022)", fontsize=14, weight='bold')
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Precipitation (mm)", fontsize=12)
axes[1].grid(linestyle='--', alpha=0.6)
axes[1].legend(loc='upper left', fontsize=10)
axes[1].set_xticks(years)

# Display the chart
plt.show()