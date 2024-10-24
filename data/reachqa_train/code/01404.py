import numpy as np
import matplotlib.pyplot as plt

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Mean computation time reduction for various quantum algorithms (in minutes)
algo_A_time_reduction = np.array([30, 28, 25, 23, 20, 18, 15, 13, 10, 8, 5])
algo_B_time_reduction = np.array([45, 42, 38, 35, 32, 30, 27, 25, 22, 20, 18])
algo_C_time_reduction = np.array([50, 48, 45, 42, 40, 37, 35, 33, 30, 28, 25])

# Standard deviations for each algorithm to show the uncertainty in measurements
algo_A_std = np.array([2, 2.5, 2, 1.8, 1.5, 1.3, 1.2, 1, 0.8, 0.7, 0.5])
algo_B_std = np.array([3, 2.7, 2.5, 2.2, 2, 1.8, 1.5, 1.3, 1, 0.9, 0.7])
algo_C_std = np.array([3.5, 3, 2.8, 2.5, 2.3, 2, 1.8, 1.5, 1.2, 1, 0.8])

# Create the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data with error bars
ax.errorbar(years, algo_A_time_reduction, yerr=algo_A_std, label='Quantum Algorithm A',
            fmt='o-', color='#ff9999', capsize=5, capthick=2, elinewidth=1.5, linewidth=2, alpha=0.8)

ax.errorbar(years, algo_B_time_reduction, yerr=algo_B_std, label='Quantum Algorithm B',
            fmt='s-', color='#66b3ff', capsize=5, capthick=2, elinewidth=1.5, linewidth=2, alpha=0.8)

ax.errorbar(years, algo_C_time_reduction, yerr=algo_C_std, label='Quantum Algorithm C',
            fmt='^-', color='#99ff99', capsize=5, capthick=2, elinewidth=1.5, linewidth=2, alpha=0.8)

# Customize the plot
ax.set_title('Quantum Algorithm Efficiency Advancements\n2013-2023 Symposium Overview',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Computation Time Reduction (minutes)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 61, 5))
ax.legend(title='Algorithm', fontsize=12, loc='upper right', frameon=True)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Highlight trend insights with annotations
ax.annotate('Major Breakthrough in 2020', xy=(2020, 13), xytext=(2015, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='darkred')

# Enhance layout to prevent label overlap
plt.tight_layout()

# Display the chart
plt.show()