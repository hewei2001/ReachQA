import matplotlib.pyplot as plt
import numpy as np

# Define years and success rates
years = np.array([1400, 1425, 1450, 1475, 1500])
success_rates_early = np.array([45, 50, 55, 60, 65])
success_rates_late = np.array([60, 65, 70, 75, 80])
error_early = np.array([5, 4, 4, 3, 3])
error_late = np.array([4, 3, 3, 2, 2])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot success rates with error bars
ax.errorbar(years, success_rates_early, yerr=error_early, fmt='o-', color='royalblue',
            ecolor='lightblue', elinewidth=2, capsize=5, capthick=2,
            label='Early Period (1400-1450)', alpha=0.8)
ax.errorbar(years, success_rates_late, yerr=error_late, fmt='s-', color='darkorange',
            ecolor='peachpuff', elinewidth=2, capsize=5, capthick=2,
            label='Late Period (1451-1500)', alpha=0.8)

# Set title and labels
ax.set_title("Navigating the Waters:\nHistorical Trends in Maritime Exploration Success",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Success Rate (%)', fontsize=12)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.6, axis='y')
ax.legend(loc='lower right', fontsize=12)

# Customize spines visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()