import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = np.arange(2010, 2026)
adoption_rate = np.array([5, 6.5, 8, 9, 11, 13, 16, 20, 25, 30, 36, 43, 51, 60, 70, 82])
error_margin = np.array([0.5, 0.7, 0.8, 1.0, 1.1, 1.3, 1.5, 2.0, 2.5, 3.0, 3.5, 4.3, 5.1, 6.0, 7.0, 8.2])
investment = np.array([2, 2.2, 2.5, 2.7, 3.2, 3.8, 4.5, 5, 6, 7, 8.5, 10, 12, 15, 18, 22])  # Hypothetical investment data

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot line with error bars
ax1.errorbar(years, adoption_rate, yerr=error_margin, fmt='-o', capsize=5, color='teal', ecolor='orange', elinewidth=2, alpha=0.7, label='Adoption Rate')
ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('Adoption Rate (%)', fontsize=13, color='teal')
ax1.tick_params(axis='y', labelcolor='teal')

# Add secondary y-axis for investment data
ax2 = ax1.twinx()
ax2.plot(years, investment, 's--', color='purple', alpha=0.6, label='Investment (in billion USD)')
ax2.set_ylabel('Investment (billion USD)', fontsize=13, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Title and Subtitles
plt.title('Trend of Renewable Energy Adoption and Investment\n2010-2025', fontsize=16, fontweight='bold')

# Customize grid
ax1.grid(True, linestyle='--', alpha=0.5)

# Annotations
ax1.annotate('2020 Milestone: 25%', xy=(2020, 25), xytext=(2017, 35),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax1.annotate('Projected Peak: 82%', xy=(2025, 82), xytext=(2023, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

# Add shaded region to denote an important period
ax1.axvspan(2015, 2020, color='yellow', alpha=0.1, label='Growth Phase')

# Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Set limits
ax1.set_ylim(0, 90)
ax2.set_ylim(0, 25)
ax1.set_xlim(2010, 2025)

# Ensure layout is tidy
fig.tight_layout()

# Show plot
plt.show()