import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average monthly coffee consumption (cups) for different types
espresso_consumption = [20, 23, 25, 30, 35, 37, 39, 42, 45, 47, 50]
cappuccino_consumption = [15, 17, 20, 22, 18, 20, 23, 25, 27, 30, 28]
cold_brew_consumption = [5, 8, 12, 15, 18, 20, 22, 27, 30, 33, 35]

# Standard deviations for error bars
espresso_std = [2, 3, 2, 3, 3, 2, 3, 4, 3, 2, 3]
cappuccino_std = [3, 2, 4, 3, 2, 3, 4, 3, 2, 3, 4]
cold_brew_std = [1, 2, 3, 2, 3, 3, 2, 3, 4, 3, 2]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each coffee type with error bars
ax.errorbar(years, espresso_consumption, yerr=espresso_std, label='Espresso',
            fmt='-o', capsize=5, linestyle='--', color='darkorange', alpha=0.8)
ax.errorbar(years, cappuccino_consumption, yerr=cappuccino_std, label='Cappuccino',
            fmt='-^', capsize=5, linestyle='-', color='teal', alpha=0.8)
ax.errorbar(years, cold_brew_consumption, yerr=cold_brew_std, label='Cold Brew',
            fmt='-s', capsize=5, linestyle='-.', color='purple', alpha=0.8)

# Customize the plot
ax.set_title('Coffee Consumption Patterns\nin Writers\' Retreats Over the Decade', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Consumption (Cups)', fontsize=12)
ax.set_xticks(years)
ax.set_xlim(2010, 2020)
ax.set_ylim(0, 60)
ax.legend(title="Coffee Type", fontsize=10, loc='upper left')

# Enable grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for neatness
plt.tight_layout()

# Display the plot
plt.show()