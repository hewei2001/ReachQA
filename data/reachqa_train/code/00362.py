import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Define years from 2030 to 2040
years = np.arange(2030, 2041)

# Enhanced power generation data in GW for different energy sources
solar = np.array([100 + 5*i + (5 * np.sin(i/2)) for i in range(len(years))])
nuclear = np.array([200 + 10*i - (2 * np.sin(i)) for i in range(len(years))])
fusion = np.array([50 + 15*i + (10 * np.cos(i/3)) for i in range(len(years))])
antimatter = np.array([10 * (2 ** (i // 2)) + (5 * np.sin(i/4)) for i in range(len(years))])  # Doubling with slight variation

# Related data: Efficiency improvements (%)
efficiency_solar = np.array([80 + 1.5*i for i in range(len(years))])
efficiency_nuclear = np.array([75 + 0.5*i for i in range(len(years))])
efficiency_fusion = np.array([60 + 2*i for i in range(len(years))])
efficiency_antimatter = np.array([50 + 3*i for i in range(len(years))])

# Create the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 8))

# Plot the main chart - Line Plot for Power Generation
axes[0].plot(years, solar, label='Solar', color='gold', linewidth=2, marker='o', alpha=0.8)
axes[0].plot(years, nuclear, label='Nuclear', color='orange', linewidth=2, linestyle='--', marker='s', alpha=0.8)
axes[0].plot(years, fusion, label='Fusion', color='cyan', linewidth=2, linestyle='-.', marker='^', alpha=0.8)
axes[0].plot(years, antimatter, label='Antimatter', color='magenta', linewidth=2, linestyle=':', marker='D', alpha=0.8)

# Title and labels for the line plot
axes[0].set_title("Journey to Deep Space:\nPower Generation Over Time", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Year", fontsize=10)
axes[0].set_ylabel("Power Generation (GW)", fontsize=10)
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend(loc='upper left', fontsize=9)
axes[0].set_xticks(years)
axes[0].set_yticks(np.arange(0, 500, 50))

# Plot annotations for the line plot
for i, year in enumerate(years):
    if i % 2 == 0:  # Annotate every other year for clarity
        axes[0].annotate(f'{solar[i]:.1f} GW', (year, solar[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7, color='gold')
        axes[0].annotate(f'{nuclear[i]:.1f} GW', (year, nuclear[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=7, color='orange')
        axes[0].annotate(f'{fusion[i]:.1f} GW', (year, fusion[i]), textcoords="offset points", xytext=(0, -30), ha='center', fontsize=7, color='cyan')
        axes[0].annotate(f'{antimatter[i]:.1f} GW', (year, antimatter[i]), textcoords="offset points", xytext=(0, -45), ha='center', fontsize=7, color='magenta')

# Plot the additional chart - Bar Plot for Efficiency Improvements
bar_width = 0.2
x_indices = np.arange(len(years))

axes[1].bar(x_indices - 1.5*bar_width, efficiency_solar, width=bar_width, label='Solar', color='gold', alpha=0.7)
axes[1].bar(x_indices - 0.5*bar_width, efficiency_nuclear, width=bar_width, label='Nuclear', color='orange', alpha=0.7)
axes[1].bar(x_indices + 0.5*bar_width, efficiency_fusion, width=bar_width, label='Fusion', color='cyan', alpha=0.7)
axes[1].bar(x_indices + 1.5*bar_width, efficiency_antimatter, width=bar_width, label='Antimatter', color='magenta', alpha=0.7)

# Title and labels for the bar plot
axes[1].set_title("Efficiency Improvements Over Time", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Year", fontsize=10)
axes[1].set_ylabel("Efficiency (%)", fontsize=10)
axes[1].set_xticks(x_indices)
axes[1].set_xticklabels(years, rotation=45)
axes[1].legend(loc='upper left', fontsize=9)
axes[1].yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{int(y)}%'))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()