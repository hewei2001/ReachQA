import numpy as np
import matplotlib.pyplot as plt

# Years of data collection
years = np.arange(2010, 2021)

# Average installations (in thousands) for each state over the years
installations_state_a = np.array([10, 12, 14, 15, 17, 20, 23, 28, 35, 40, 45])
installations_state_b = np.array([8, 10, 12, 16, 21, 25, 30, 34, 39, 42, 44])
installations_state_c = np.array([5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])

# Error margins representing variability or uncertainty in installations (in thousands)
error_state_a = np.array([1.0, 1.5, 1.3, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 2.7, 3.0])
error_state_b = np.array([0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.1, 2.3, 2.6, 2.9, 3.1])
error_state_c = np.array([0.5, 0.7, 1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2, 2.5, 2.8])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data with error bars for each state
ax.errorbar(years, installations_state_a, yerr=error_state_a, label='State A', fmt='-o', capsize=5, color='blue', alpha=0.75)
ax.errorbar(years, installations_state_b, yerr=error_state_b, label='State B', fmt='-s', capsize=5, color='green', alpha=0.75)
ax.errorbar(years, installations_state_c, yerr=error_state_c, label='State C', fmt='-^', capsize=5, color='red', alpha=0.75)

# Set chart details
ax.set_title("Solar Panel Installations (2010-2020):\nTracking Growth and Variability Across States", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Average Installations (in thousands)", fontsize=12)
ax.set_xticks(years)
ax.set_xlim(2009, 2021)
ax.set_ylim(0, 50)
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(title="States", title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()