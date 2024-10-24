import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest
years = np.array([1977, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

# Cumulative data return in gigabytes (hypothetical values)
data_return = np.array([0.1, 0.5, 1.5, 3.0, 4.0, 4.5, 5.0, 5.5, 5.75, 6.0])
data_errors = np.array([0.05, 0.1, 0.2, 0.25, 0.2, 0.15, 0.1, 0.1, 0.05, 0.05])

# Hypothetical data processing efficiency in percentage
data_efficiency = np.array([20, 40, 55, 65, 72, 80, 85, 88, 92, 95])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the primary data with error bars
ax1.errorbar(years, data_return, yerr=data_errors, fmt='-o', ecolor='tomato', capsize=5, 
             capthick=2, elinewidth=2, markerfacecolor='dodgerblue', markersize=7, 
             label='Cumulative Data Return (GB)')
ax1.set_title("Exploration Trends of the Outer Solar System:\nVoyager Missions", fontsize=16, weight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Cumulative Data Return (GB)", fontsize=14, color='navy')
ax1.tick_params(axis='y', labelcolor='navy')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=12)
ax1.set_yticks(np.arange(0, 7, 1))
ax1.grid(linestyle='--', alpha=0.6)

# Add a secondary axis for data efficiency
ax2 = ax1.twinx()
ax2.plot(years, data_efficiency, color='forestgreen', linestyle='--', marker='s', markersize=7,
         label='Data Processing Efficiency (%)')
ax2.fill_between(years, 0, data_efficiency, color='forestgreen', alpha=0.1)
ax2.set_ylabel("Data Processing Efficiency (%)", fontsize=14, color='forestgreen')
ax2.tick_params(axis='y', labelcolor='forestgreen')
ax2.set_yticks(np.arange(0, 101, 10))

# Add annotations for specific years
ax1.annotate('Voyager 1 Launch', xy=(1977, 0.1), xytext=(1977, 1),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
ax1.annotate('First Jupiter Flyby', xy=(1979, 0.5), xytext=(1982, 2),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85), fontsize=12, frameon=False)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()