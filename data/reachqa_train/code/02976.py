import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Original Data: Years from 2020 to 2030
years = np.arange(2020, 2031)
# Manually generated data for star-gazing sessions
sessions = np.array([150, 160, 175, 180, 195, 210, 230, 255, 290, 320, 350])

# Related Data: Number of astronomy clubs formed each year
clubs_formed = np.array([5, 7, 8, 12, 15, 20, 24, 28, 35, 40, 50])

# Define a quadratic function for curve fitting
def quadratic_fit(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the quadratic function to the data
params, _ = curve_fit(quadratic_fit, years, sessions)

# Generate a smooth curve for plotting using more points
smooth_years = np.linspace(2020, 2030, 300)
smooth_sessions = quadratic_fit(smooth_years, *params)

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for actual data
scatter = ax1.scatter(years, sessions, color='purple', label='Actual Sessions', s=100, edgecolor='white', zorder=3)
# Plot smooth fitting curve
line, = ax1.plot(smooth_years, smooth_sessions, color='green', label='Trend Line (Quadratic Fit)', linewidth=2, zorder=2)

# Add title and labels with line breaks for clarity
plt.title('Mapping the Sky:\nThe Rise of Astronomy Interest through Star-Gazing Sessions and Club Formations (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Sessions', fontsize=14, color='purple')

# Customize ticks for clarity
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 401, 50))

# Create secondary y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('Astronomy Clubs Formed', fontsize=14, color='navy')
bar = ax2.bar(years, clubs_formed, color='navy', alpha=0.3, label='Clubs Formed', zorder=1)
ax2.set_yticks(np.arange(0, 51, 10))

# Annotate a significant trend in 2028
ax1.annotate('Significant boost in 2028', xy=(2028, 255), xytext=(2024, 280),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Legends for both plots
fig.legend(loc='upper left', fontsize=12, bbox_to_anchor=(0.1, 0.95), bbox_transform=ax1.transAxes)

# Add grid lines for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()