import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Year Range for projections
years = np.array([2023, 2025, 2027, 2029, 2031, 2033])

# Projected employment growth percentages
healthcare_growth = np.array([4, 6, 9, 12, 15, 18])
manufacturing_growth = np.array([2, 4, 5, 8, 11, 14])
retail_growth = np.array([3, 5, 7, 11, 14, 17])
it_growth = np.array([6, 8, 12, 15, 18, 22])
logistics_growth = np.array([5, 7, 10, 12, 16, 20])

# Colors for the scatter plots
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8633']

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Define a smooth fitting function
def smooth_curve(x, y):
    x_new = np.linspace(x.min(), x.max(), 300)
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_new)
    return x_new, y_smooth

# Plot scatter and smooth fit for each industry
for growth, color, label in zip([healthcare_growth, manufacturing_growth, retail_growth, it_growth, logistics_growth],
                                colors,
                                ['Healthcare', 'Manufacturing', 'Retail', 'Information Technology', 'Logistics']):
    ax.scatter(years, growth, color=color, label=f'{label} Growth')
    x_smooth, y_smooth = smooth_curve(years, growth)
    ax.plot(x_smooth, y_smooth, color=color, alpha=0.6)

# Customizing the plot
ax.set_title('Impact of AI and Robotics on Industry Employment Growth\n(2023-2033)', fontsize=16, loc='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Projected Employment Growth (%)', fontsize=12)
ax.legend(title='Industry Sectors', fontsize=10, loc='upper left')
ax.set_xlim(2023, 2033)
ax.set_ylim(0, 25)
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()