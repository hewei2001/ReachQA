import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Data setup
years = np.arange(2013, 2024)
algo_A_time_reduction = np.array([30, 28, 25, 23, 20, 18, 15, 13, 10, 8, 5])
algo_B_time_reduction = np.array([45, 42, 38, 35, 32, 30, 27, 25, 22, 20, 18])
algo_C_time_reduction = np.array([50, 48, 45, 42, 40, 37, 35, 33, 30, 28, 25])
algo_A_std = np.array([2, 2.5, 2, 1.8, 1.5, 1.3, 1.2, 1, 0.8, 0.7, 0.5])
algo_B_std = np.array([3, 2.7, 2.5, 2.2, 2, 1.8, 1.5, 1.3, 1, 0.9, 0.7])
algo_C_std = np.array([3.5, 3, 2.8, 2.5, 2.3, 2, 1.8, 1.5, 1.2, 1, 0.8])

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Plot data with enhanced error bars and shading
ax.errorbar(years, algo_A_time_reduction, yerr=algo_A_std, label='Quantum Algorithm A',
            fmt='o-', color='#e63946', capsize=5, capthick=2, elinewidth=1.5, linewidth=2, alpha=0.8)
ax.fill_between(years, algo_A_time_reduction - algo_A_std, algo_A_time_reduction + algo_A_std, color='#e63946', alpha=0.2)

ax.errorbar(years, algo_B_time_reduction, yerr=algo_B_std, label='Quantum Algorithm B',
            fmt='s-', color='#457b9d', capsize=5, capthick=2, elinewidth=1.5, linewidth=2, alpha=0.8)
ax.fill_between(years, algo_B_time_reduction - algo_B_std, algo_B_time_reduction + algo_B_std, color='#457b9d', alpha=0.2)

ax.errorbar(years, algo_C_time_reduction, yerr=algo_C_std, label='Quantum Algorithm C',
            fmt='^-', color='#2a9d8f', capsize=5, capthick=2, elinewidth=1.5, linewidth=2, alpha=0.8)
ax.fill_between(years, algo_C_time_reduction - algo_C_std, algo_C_time_reduction + algo_C_std, color='#2a9d8f', alpha=0.2)

# Highlight and annotate
ax.annotate('Major Breakthrough\nin 2020', xy=(2020, 13), xytext=(2015.5, 22),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12, color='darkred', ha='center')

# Customizing axes and grid
ax.set_title('Quantum Algorithm Efficiency Advancements\n2013-2023 Symposium Overview',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Computation Time Reduction (minutes)', fontsize=14)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 61, 5))
ax.legend(title='Algorithm', fontsize=12, loc='upper right', frameon=True)
ax.grid(True, linestyle='--', alpha=0.5)

# Add trend lines
z_A = np.polyfit(years, algo_A_time_reduction, 3)
p_A = np.poly1d(z_A)
ax.plot(years, p_A(years), ":", color="#e63946", linewidth=1.5, label='Trend A')

z_B = np.polyfit(years, algo_B_time_reduction, 3)
p_B = np.poly1d(z_B)
ax.plot(years, p_B(years), ":", color="#457b9d", linewidth=1.5, label='Trend B')

z_C = np.polyfit(years, algo_C_time_reduction, 3)
p_C = np.poly1d(z_C)
ax.plot(years, p_C(years), ":", color="#2a9d8f", linewidth=1.5, label='Trend C')

# Improve layout
plt.tight_layout()

# Display the chart
plt.show()