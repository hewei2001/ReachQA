import matplotlib.pyplot as plt
import numpy as np

# Original data for electric vehicle projections (in millions)
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
ev_projections = np.array([4, 8, 15, 25, 35, 50])
error_margin = np.array([0.5, 1, 1.5, 2, 2.5, 3])

# Additional related data: Annual growth rate (%) of EVs
ev_growth_rate = np.array([100, 87.5, 66.67, 66.67, 40, 42.86])  # Growth rates compared to previous year

# Plot setup with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Line chart with error bars
axs[0].errorbar(years, ev_projections, yerr=error_margin, fmt='-o', color='green', 
                ecolor='lightgray', elinewidth=2, capsize=5, alpha=0.8,
                label='EV Adoption Projections')
axs[0].set_title('Projected Growth of Electric Vehicles\nAdoption Worldwide (2020-2025)', fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Number of EVs (Millions)', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 60, 10))
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(loc='upper left', fontsize=10, frameon=False)

# Annotate significant data points in subplot 1
for year, projection, error in zip(years, ev_projections, error_margin):
    axs[0].annotate(f'{projection}M±{error}M', (year, projection + error + 2),
                    ha='center', fontsize=9, color='darkgreen',
                    bbox=dict(facecolor='lightgreen', alpha=0.5, boxstyle='round,pad=0.3'))

# Subplot 2: Bar chart for annual growth rate
axs[1].bar(years, ev_growth_rate, color='skyblue', alpha=0.7, label='Annual Growth Rate (%)')
axs[1].set_title('Annual Growth Rate of EV Adoption\n(2020-2025)', fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Rate (%)', fontsize=12)
axs[1].set_xticks(years)
axs[1].set_yticks(np.arange(0, 120, 20))
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].legend(loc='upper right', fontsize=10, frameon=False)

# Annotate bars with growth rates in subplot 2
for year, rate in zip(years, ev_growth_rate):
    axs[1].annotate(f'{rate:.2f}%', (year, rate + 2),
                    ha='center', fontsize=9, color='darkblue',
                    bbox=dict(facecolor='lightblue', alpha=0.5, boxstyle='round,pad=0.3'))

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()