import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define data for years and urban produce yield
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
yield_data = np.array([2.5, 2.7, 3.0, 3.6, 4.2, 4.9, 5.6, 6.3, 7.1, 8.0, 9.2])

# Related data for investment in urban gardening
investment_data = np.array([20, 22, 24, 28, 35, 40, 55, 60, 70, 85, 95])  # Hypothetical data in $K

# Smooth curve using cubic spline interpolation for yield data
X_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, yield_data, k=3)
Y_smooth = spl(X_smooth)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the line chart for urban produce yield
ax1.scatter(years, yield_data, color='#FF5733', label='Annual Yield', s=100, alpha=0.7, edgecolors='black')
ax1.plot(X_smooth, Y_smooth, color='#3375FF', linewidth=2.5, label='Yield Trend Line')

# Title and labels
plt.title("Urban Gardening & Produce Yield\nGrowth and Investments in Greenview (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Produce Yield (Metric Tons)", fontsize=12, color='#3375FF')
ax1.tick_params(axis='y', labelcolor='#3375FF')
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 11, 1))
ax1.grid(True, linestyle='--', alpha=0.6)

# Secondary bar chart for investment
ax2 = ax1.twinx()
ax2.bar(years, investment_data, color='#76D7C4', alpha=0.6, label='Investment ($K)', width=0.4, align='center')
ax2.set_ylabel("Investment in Urban Gardening ($K)", fontsize=12, color='#76D7C4')
ax2.tick_params(axis='y', labelcolor='#76D7C4')
ax2.set_yticks(np.arange(0, 101, 10))

# Annotations for significant years
ax1.annotate("New Techniques Introduced", xy=(2016, 5.6), xytext=(2014, 7.5),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, fontweight='bold', color='green')

# Legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()