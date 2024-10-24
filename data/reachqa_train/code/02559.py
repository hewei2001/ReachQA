import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define the years and corresponding number of developers
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
developers = np.array([100, 150, 200, 300, 500, 800, 1300, 2100, 3500, 5000, 6000])

# Calculate the year-over-year growth rate
growth_rate = np.diff(developers) / developers[:-1] * 100  # Percentage growth
growth_years = years[1:]  # Corresponding years for growth rate

# Spline for original data
x_new = np.linspace(years.min(), years.max(), 300)
spline = make_interp_spline(years, developers, k=3)
developers_smooth = spline(x_new)

# Set up the plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Original developers plot
ax1.scatter(years, developers, color='darkblue', edgecolor='black', s=100, zorder=3, label='Developers')
ax1.plot(x_new, developers_smooth, color='deepskyblue', linewidth=3, linestyle='-', label='Adoption Trend Line')
ax1.set_title('Journey Through the Digital Landscape:\nA Decade of InnovateLang Trends', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Developers', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.annotate(f'Peak: {developers.max()} developers', xy=(years[-1], developers.max()),
             xytext=(years[-3], developers.max() - 1500),
             arrowprops=dict(facecolor='gray', shrink=0.05, width=1.5, headwidth=8),
             fontsize=10, color='red', fontweight='bold')

# Growth rate plot
ax2.bar(growth_years, growth_rate, color='lightcoral', edgecolor='black')
ax2.set_title('Annual Growth Rate of Developers', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

# Ensure readability
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()