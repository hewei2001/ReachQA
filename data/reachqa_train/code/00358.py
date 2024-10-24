import matplotlib.pyplot as plt
import numpy as np

# Define years and error rates for two labs
years = np.arange(2013, 2024)
error_rates_lab1 = np.array([0.15, 0.13, 0.12, 0.10, 0.09, 0.08, 0.07, 0.05, 0.04, 0.03, 0.02])
error_rates_lab2 = np.array([0.14, 0.12, 0.11, 0.09, 0.08, 0.07, 0.06, 0.05, 0.03, 0.03, 0.02])

# Define error margins for each year
error_margins_lab1 = np.array([0.02, 0.018, 0.016, 0.014, 0.012, 0.011, 0.01, 0.009, 0.008, 0.007, 0.005])
error_margins_lab2 = np.array([0.018, 0.016, 0.015, 0.013, 0.011, 0.01, 0.009, 0.008, 0.006, 0.005, 0.004])

# Additional data: Number of experiments conducted
experiments_lab1 = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
experiments_lab2 = np.array([90, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# Subplot 1: Error bar plot for error rates over time
ax1.errorbar(years, error_rates_lab1, yerr=error_margins_lab1, fmt='-o', color='blue', label='Quantum Lab A', capsize=4, capthick=2, alpha=0.7)
ax1.errorbar(years, error_rates_lab2, yerr=error_margins_lab2, fmt='-s', color='green', label='Quantum Lab B', capsize=4, capthick=2, alpha=0.7)
ax1.set_title("Advancements in Quantum Computing:\nError Rates Over Time", fontsize=14, weight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Error Rate", fontsize=12)
ax1.set_ylim(0, 0.2)
ax1.set_xlim(2012, 2024)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title="Research Labs", title_fontsize='13', fontsize='11', loc='upper right')

# Subplot 2: Stacked bar chart for number of experiments
ax2.bar(years, experiments_lab1, color='lightblue', label='Quantum Lab A')
ax2.bar(years, experiments_lab2, bottom=experiments_lab1, color='lightgreen', label='Quantum Lab B')
ax2.set_title("Number of Experiments Conducted by Year", fontsize=14, weight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Number of Experiments", fontsize=12)
ax2.set_ylim(0, 450)
ax2.set_xlim(2012, 2024)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(title="Research Labs", title_fontsize='13', fontsize='11', loc='upper left')

plt.show()