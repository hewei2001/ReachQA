import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from collections import defaultdict

# Data: Monthly coffee consumption (in cups)
coffee_consumption = np.array([10, 12, 15, 18, 22, 25, 30, 28, 24, 20, 18, 15])

# Data: Corresponding productivity score (scale 0-10)
productivity_score = np.array([6, 6.5, 7, 7.5, 8, 8.5, 9, 8.7, 8.2, 7.8, 7.5, 7])

# New data: Average work hours per month
average_work_hours = np.array([160, 162, 165, 168, 172, 175, 180, 178, 174, 170, 168, 165])

# Handle duplicates by averaging productivity scores for duplicate coffee consumption values
consumption_dict = defaultdict(list)
for cons, prod in zip(coffee_consumption, productivity_score):
    consumption_dict[cons].append(prod)

unique_coffee_consumption = np.array(sorted(consumption_dict.keys()))
averaged_productivity_score = np.array([np.mean(consumption_dict[cons]) for cons in unique_coffee_consumption])

# Create a scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(coffee_consumption, productivity_score, color='darkorange', edgecolor='k', s=100, alpha=0.8, label='Productivity vs. Coffee')

# Smooth curve fitting using cubic spline
spline = interpolate.make_interp_spline(unique_coffee_consumption, averaged_productivity_score)
smooth_x = np.linspace(unique_coffee_consumption.min(), unique_coffee_consumption.max(), 300)
smooth_y = spline(smooth_x)
plt.plot(smooth_x, smooth_y, color='mediumseagreen', lw=3, label='Productivity Trend')

# Overlay plot: Line plot of work hours
plt.plot(coffee_consumption, average_work_hours/20, marker='o', color='steelblue', linewidth=2, linestyle='--', label='Work Hours (scaled)')

# Title and labels
plt.title('Coffee Consumption vs. Productivity\n& Work Hours in a Tech Startup', fontsize=16, weight='bold')
plt.xlabel('Monthly Coffee Consumption (Cups)', fontsize=14)
plt.ylabel('Productivity Score / Work Hours (Scaled)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Legend and grid
plt.legend(fontsize=12, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

# Use tight layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()