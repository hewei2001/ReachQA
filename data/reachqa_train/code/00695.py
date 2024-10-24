import matplotlib.pyplot as plt
import numpy as np

# Define the years and average solar energy production (in GWh) for each year
years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])

# Variability in production due to weather conditions, representing ± potential deviations
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

# Create the line chart with error bars
plt.figure(figsize=(12, 6))
plt.errorbar(
    years, average_production, yerr=error, fmt='-o', color='teal', ecolor='lightcoral',
    linestyle='-', capsize=5, capthick=2, markerfacecolor='navy', alpha=0.8, label='Avg. Solar Production'
)

# Customizing plot aesthetics
plt.title('Decadal Trends in Solar Energy Production:\n2010-2020', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Average Production (GWh)', fontsize=12, fontweight='bold')
plt.xticks(years, rotation=45)
plt.yticks(np.arange(280, 470, 20))
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Add descriptive text box
plt.text(2010.5, 440, 'Variability due to weather conditions', fontsize=10, style='italic', bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 5})

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()