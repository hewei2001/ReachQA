import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding tree growth data (in cm)
years = np.arange(2013, 2024)
tree_growth = np.array([15.2, 15.8, 15.5, 16.0, 16.3, 16.7, 17.1, 17.3, 17.6, 18.0, 18.5])

# Create a smooth line using cubic spline interpolation
xnew = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, tree_growth, k=3)
smooth_growth = spl(xnew)

# Plotting the scatter chart
plt.figure(figsize=(14, 8))
plt.scatter(years, tree_growth, color='sienna', label='Annual Measurements', s=100, zorder=5, edgecolor='black')
plt.plot(xnew, smooth_growth, color='forestgreen', linewidth=2.5, label='Fitted Growth Trend', linestyle='--')

# Adding labels and title
plt.title("Impact of Climate Change on Tree Growth:\nA Decade of Transformation", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14, fontweight='semibold')
plt.ylabel('Average Tree Growth (cm)', fontsize=14, fontweight='semibold')

# Customize ticks and grid
plt.xticks(years, rotation=45)
plt.yticks(np.arange(15, 19.5, 0.5))
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='grey')

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True, title='Data Series')

# Annotating significant trends
plt.annotate('Notable Growth Increase', xy=(2021, 18.0), xytext=(2015.5, 18.3),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=11, color='darkred', fontweight='bold')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()