import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define the years and corresponding number of developers
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
developers = np.array([100, 150, 200, 300, 500, 800, 1300, 2100, 3500, 5000, 6000])

# Generate a smooth fitting curve using cubic splines
x_new = np.linspace(years.min(), years.max(), 300)
spline = make_interp_spline(years, developers, k=3)  # Cubic spline
developers_smooth = spline(x_new)

# Set up the plot
plt.figure(figsize=(14, 8))
plt.scatter(years, developers, color='darkblue', edgecolor='black', s=100, zorder=3, label='Developers')
plt.plot(x_new, developers_smooth, color='deepskyblue', linewidth=3, linestyle='-', label='Adoption Trend Line')

# Title and labels
plt.title('Journey Through the Digital Landscape:\nA Decade of InnovateLang Trends', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Developers', fontsize=14)

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=12)

# Highlight the peak adoption point with annotation
peak_year = years[np.argmax(developers)]
peak_devs = developers.max()
plt.annotate(f'Peak: {peak_devs} developers', xy=(peak_year, peak_devs),
             xytext=(peak_year-2, peak_devs + 1000),
             arrowprops=dict(facecolor='gray', shrink=0.05, width=1.5, headwidth=8),
             fontsize=12, color='red', fontweight='bold')

# Customize ticks for better readability
plt.xticks(years, fontsize=12)
plt.yticks(fontsize=12)

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()