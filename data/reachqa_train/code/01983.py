import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Apply a built-in style similar to 'seaborn-darkgrid'
plt.style.use('ggplot')

# Define the years
years = np.arange(2010, 2021)

# Popularity data for different fashion styles
vintage = np.array([20, 25, 30, 35, 37, 40, 42, 45, 50, 55, 60])
streetwear = np.array([15, 20, 25, 30, 40, 50, 55, 60, 62, 65, 70])
athleisure = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
sustainable_fashion = np.array([1, 2, 4, 6, 9, 13, 18, 25, 33, 42, 52])

# Plot the line chart
fig, ax = plt.subplots(figsize=(14, 9))

# Plot each line with distinct styles
ax.plot(years, vintage, marker='o', linestyle='-', color='#d62728', linewidth=2, label='Vintage')
ax.plot(years, streetwear, marker='s', linestyle='--', color='#1f77b4', linewidth=2, label='Streetwear')
ax.plot(years, athleisure, marker='^', linestyle=':', color='#2ca02c', linewidth=2, label='Athleisure')
ax.plot(years, sustainable_fashion, marker='x', linestyle='-.', color='#ff7f0e', linewidth=2, label='Sustainable Fashion')

# Annotate the lines with relevant values
highlight_years = [2015, 2020]
for year, v, s, a, su in zip(years, vintage, streetwear, athleisure, sustainable_fashion):
    if year in highlight_years:
        ax.annotate(f'{v}', xy=(year, v), xytext=(-10, 10), textcoords='offset points', color='#d62728', fontsize=10, fontweight='bold')
        ax.annotate(f'{s}', xy=(year, s), xytext=(-10, 10), textcoords='offset points', color='#1f77b4', fontsize=10, fontweight='bold')
        ax.annotate(f'{a}', xy=(year, a), xytext=(-10, 10), textcoords='offset points', color='#2ca02c', fontsize=10, fontweight='bold')
        ax.annotate(f'{su}', xy=(year, su), xytext=(-10, 10), textcoords='offset points', color='#ff7f0e', fontsize=10, fontweight='bold')

# Enhance the plot with titles and labels
ax.set_title("Decade of Fashion:\nPopularity Trends from 2010 to 2020", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Popularity Index", fontsize=14)

# Add a legend and grid for better readability
ax.legend(loc='upper left', fontsize='medium', title="Fashion Styles", title_fontsize='medium', frameon=True)
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.8)

# Rotate x-axis labels for better visibility
plt.xticks(years, rotation=45)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Use a secondary axis for highlighting overall trends
ax2 = ax.twinx()
ax2.set_ylabel('Normalized Index', fontsize=14)
normalized_data = (vintage + streetwear + athleisure + sustainable_fashion) / 4
ax2.plot(years, normalized_data, color='grey', alpha=0.3, linewidth=2, label='Average Trend')
ax2.legend(loc='lower right', fontsize='medium', frameon=True)

# Highlight significant period with a vertical span
ax.axvspan(2013, 2016, color='gray', alpha=0.2, label="Notable Shift")
ax.legend(loc='upper left', fontsize='medium', title="Fashion Styles", title_fontsize='medium', frameon=True)

# Use tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()