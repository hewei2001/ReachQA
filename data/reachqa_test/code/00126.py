import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Original Data for the number of startups in incubation programs (in thousands)
years = np.arange(2010, 2020)
startups_participating = np.array([1.5, 2.1, 3.0, 4.0, 4.5, 5.5, 6.2, 7.0, 8.0, 8.8])
patents_filed = np.array([20, 25, 35, 50, 55, 70, 82, 95, 110, 130])

# Derived Data: Average Patents per Startup
avg_patents_per_startup = patents_filed / startups_participating

# Create smooth spline for original data
x_smooth = np.linspace(startups_participating.min(), startups_participating.max(), 500)
spl = make_interp_spline(startups_participating, patents_filed, k=3)
y_smooth = spl(x_smooth)

# Set up subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Scatter plot with smooth line
ax1.scatter(startups_participating, patents_filed, color='navy', s=100, edgecolor='black', label='Patents Data')
ax1.plot(x_smooth, y_smooth, color='crimson', linestyle='-', linewidth=2, label='Trend Line')

# Annotate years on the first subplot
for i, year in enumerate(years):
    ax1.annotate(year, (startups_participating[i], patents_filed[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Set title, labels, and limits for the first subplot
ax1.set_title("Incubation Programs and Innovation\nA Decade of Tech Startups", fontsize=14, weight='bold', ha='center')
ax1.set_xlabel('Startups in Incubation Programs (thousands)', fontsize=12)
ax1.set_ylabel('Number of Patents Filed', fontsize=12)
ax1.set_xlim(1, 10)
ax1.set_ylim(15, 140)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left')

# Second subplot: Bar chart of average patents per startup
ax2.bar(years, avg_patents_per_startup, color='teal', edgecolor='black')
ax2.set_title('Average Patents per Startup Over Time', fontsize=14, weight='bold', ha='center')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Average Patents per Startup', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()