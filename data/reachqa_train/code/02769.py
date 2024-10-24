import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
budget = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220])  # Allocated budget in millions of dollars
estimated_cost = np.array([110, 125, 138, 145, 158, 172, 178, 185, 198, 207, 218])  # Estimated costs in millions
error_margin = np.array([5, 7, 8, 6, 9, 6, 10, 8, 7, 5, 6])  # Error margins in millions

# Plotting
plt.figure(figsize=(12, 7))
plt.errorbar(years, estimated_cost, yerr=error_margin, fmt='-o', capsize=5, color='tab:blue', alpha=0.8,
             label='Estimated Mission Cost', linestyle='-', marker='o')
plt.plot(years, budget, 's-', color='tab:green', linewidth=2, markersize=5, label='Allocated Budget')

# Adding title and labels
plt.title('Lunar Exploration Budget and Estimated Mission Costs\nA Decade Review', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Millions of Dollars', fontsize=12)

# Adding a grid
plt.grid(True, linestyle='--', alpha=0.6)

# Customizing the x-ticks
plt.xticks(years, rotation=45)

# Adding legend
plt.legend(loc='upper left', fontsize=10)

# Highlighting potential cost overruns or savings
for i, (year, cost, budget_year) in enumerate(zip(years, estimated_cost, budget)):
    if cost > budget_year:
        plt.annotate('Overrun', xy=(year, cost), xytext=(year, cost + 12),
                     arrowprops=dict(facecolor='red', shrink=0.05), fontsize=9, color='red', ha='center')
    elif cost < budget_year - error_margin[i]:
        plt.annotate('Savings', xy=(year, cost), xytext=(year, cost - 15),
                     arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, color='green', ha='center')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()