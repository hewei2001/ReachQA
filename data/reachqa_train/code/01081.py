import matplotlib.pyplot as plt
import numpy as np

# Data: Years and EV registration percentages
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
ev_percentages = np.array([0.5, 0.8, 1.5, 2.3, 3.2, 5.0, 7.8, 12.0, 18.5, 25.0])
# Error values indicate variance (in percentage points)
errors = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0])

# Plotting the line chart with error bars
plt.figure(figsize=(10, 6))
plt.errorbar(
    years, ev_percentages, yerr=errors, fmt='-o', ecolor='lightgray', 
    capsize=5, elinewidth=2, markeredgewidth=2, color='teal', label='EV Adoption Rate'
)

# Title and labels
plt.title("Riding the Electric Wave:\nA Decade of EV Adoption in Metropolis", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Percentage of Vehicle Registrations", fontsize=12)

# Add legend
plt.legend(loc='upper left', fontsize='medium')

# Grid and layout adjustments
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 30, 5))

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display plot
plt.show()