import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Data preparation
years = np.arange(2010, 2026)
discovery_rate = np.array([12, 18, 24, 35, 29, 37, 46, 52, 61, 70, 80, 95, 102, 110, 115, 125])
error_margin = np.array([2, 3, 2, 4, 5, 3, 6, 4, 5, 7, 6, 5, 8, 7, 9, 6])

# Cumulative discoveries (hypothetical example)
cumulative_discoveries = np.cumsum(discovery_rate)

# Creating the figure and grid specification
fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])

# First subplot: Line chart with error bars
ax1 = fig.add_subplot(gs[0])
ax1.errorbar(years, discovery_rate, yerr=error_margin, fmt='-o', ecolor='lightcoral', 
             elinewidth=2, capsize=5, capthick=2, color='darkblue', alpha=0.9, 
             label='Exoplanet Discoveries')
ax1.set_title('Cosmic Discovery Rate\nof Exoplanets (2010-2025)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Exoplanets Discovered', fontsize=12)
ax1.grid(linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, shadow=True)
ax1.set_xlim(2009, 2026)
ax1.set_ylim(0, 140)

# Second subplot: Bar chart of cumulative discoveries
ax2 = fig.add_subplot(gs[1])
bars = ax2.bar(years, cumulative_discoveries, color='mediumseagreen', alpha=0.8)
ax2.set_title('Cumulative Discoveries\n(2010-2025)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Cumulative Exoplanets', fontsize=12)
ax2.set_xlim(2009, 2026)
ax2.set_ylim(0, cumulative_discoveries[-1] + 20)
ax2.bar_label(bars, fmt='%d', padding=3)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Show plot
plt.show()