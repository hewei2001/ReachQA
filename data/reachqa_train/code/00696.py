import matplotlib.pyplot as plt
import numpy as np

# Define the years and average solar energy production (in GWh) for each year
years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

# Calculate year-over-year percentage change in solar energy production
percent_change = np.diff(average_production) / average_production[:-1] * 100

# Create subplots: 1 row, 2 columns
fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# First subplot: Line chart with error bars
axs[0].errorbar(
    years, average_production, yerr=error, fmt='-o', color='teal', ecolor='lightcoral',
    linestyle='-', capsize=5, capthick=2, markerfacecolor='navy', alpha=0.8, label='Avg. Solar Production'
)
axs[0].set_title('Decadal Trends in Solar Energy Production:\n2010-2020', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[0].set_ylabel('Average Production (GWh)', fontsize=12, fontweight='bold')
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(280, 470, 20))
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', fontsize=10)
axs[0].text(2010.5, 440, 'Variability due to weather conditions', fontsize=10, style='italic', bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 5})

# Second subplot: Bar chart showing percentage change
axs[1].bar(years[1:], percent_change, color='navy', alpha=0.7, label='Yearly % Change')
axs[1].set_title('Yearly Percentage Change\nin Solar Production', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[1].set_ylabel('Percentage Change (%)', fontsize=12, fontweight='bold')
axs[1].set_xticks(years[1:])
axs[1].set_xticklabels(years[1:], rotation=45)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper right', fontsize=10)

# Display the plot
plt.show()