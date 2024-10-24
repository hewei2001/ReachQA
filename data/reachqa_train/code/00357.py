import matplotlib.pyplot as plt
import numpy as np

# Define years and error rates for two labs
years = np.arange(2013, 2024)
error_rates_lab1 = np.array([0.15, 0.13, 0.12, 0.10, 0.09, 0.08, 0.07, 0.05, 0.04, 0.03, 0.02])
error_rates_lab2 = np.array([0.14, 0.12, 0.11, 0.09, 0.08, 0.07, 0.06, 0.05, 0.03, 0.03, 0.02])

# Define error margins for each year
error_margins_lab1 = np.array([0.02, 0.018, 0.016, 0.014, 0.012, 0.011, 0.01, 0.009, 0.008, 0.007, 0.005])
error_margins_lab2 = np.array([0.018, 0.016, 0.015, 0.013, 0.011, 0.01, 0.009, 0.008, 0.006, 0.005, 0.004])

# Plot the data with error bars
fig, ax = plt.subplots(figsize=(10, 6))

ax.errorbar(years, error_rates_lab1, yerr=error_margins_lab1, fmt='-o', color='blue', label='Quantum Lab A', capsize=4, capthick=2, alpha=0.7)
ax.errorbar(years, error_rates_lab2, yerr=error_margins_lab2, fmt='-s', color='green', label='Quantum Lab B', capsize=4, capthick=2, alpha=0.7)

# Customize the plot
ax.set_title("Advancements in Quantum Computing:\nError Rates Over Time", fontsize=16, weight='bold', pad=15)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Error Rate", fontsize=12)
ax.set_ylim(0, 0.2)
ax.set_xlim(2012, 2024)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))  # Format y-axis as percentage
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
ax.legend(title="Research Labs", title_fontsize='13', fontsize='11', loc='upper right')

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Show plot
plt.show()