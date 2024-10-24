import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding tree growth data (in cm)
years = np.arange(2013, 2024)
tree_growth = np.array([15.2, 15.8, 15.5, 16.0, 16.3, 16.7, 17.1, 17.3, 17.6, 18.0, 18.5])

# Calculate annual growth rate percentage
growth_rate = np.diff(tree_growth) / tree_growth[:-1] * 100
growth_rate_years = years[1:]

# Create a smooth line using cubic spline interpolation for the growth data
xnew = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, tree_growth, k=3)
smooth_growth = spl(xnew)

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), sharex=True)

# First subplot: Line and scatter plot for tree growth
ax1.scatter(years, tree_growth, color='sienna', label='Annual Measurements', s=100, zorder=5, edgecolor='black')
ax1.plot(xnew, smooth_growth, color='forestgreen', linewidth=2.5, label='Fitted Growth Trend', linestyle='--')
ax1.set_title("Impact of Climate Change on Tree Growth:\nA Decade of Transformation", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, fontweight='semibold')
ax1.set_ylabel('Average Tree Growth (cm)', fontsize=12, fontweight='semibold')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='grey')
ax1.legend(loc='upper left', fontsize=10, frameon=True, shadow=True, title='Data Series')
ax1.annotate('Notable Growth Increase', xy=(2021, 18.0), xytext=(2016, 18.3),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkred', fontweight='bold')

# Second subplot: Bar chart for annual growth rate percentage
ax2.bar(growth_rate_years, growth_rate, color='teal', edgecolor='black', alpha=0.7)
ax2.set_title("Annual Growth Rate Percentage", fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12, fontweight='semibold')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, fontweight='semibold')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='grey')

# Annotate significant changes in growth rate
for year, rate in zip(growth_rate_years, growth_rate):
    if abs(rate) > 3:  # Highlight significant changes
        ax2.annotate(f'{rate:.1f}%', (year, rate), textcoords="offset points",
                     xytext=(0, 10), ha='center', fontsize=9, color='navy', fontweight='bold')

# Tight layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()