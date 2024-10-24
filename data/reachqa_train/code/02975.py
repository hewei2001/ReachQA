import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data: Years from 2020 to 2030
years = np.arange(2020, 2031)

# Manually generated data for star-gazing sessions to depict growth
sessions = np.array([150, 160, 175, 180, 195, 210, 230, 255, 290, 320, 350])

# Define a quadratic function for curve fitting
def quadratic_fit(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the quadratic function to the data
params, _ = curve_fit(quadratic_fit, years, sessions)

# Generate a smooth curve for plotting using more points
smooth_years = np.linspace(2020, 2030, 300)
smooth_sessions = quadratic_fit(smooth_years, *params)

# Plotting
plt.figure(figsize=(12, 8))

# Scatter plot for actual data
plt.scatter(years, sessions, color='purple', label='Actual Sessions', s=100, edgecolor='white', zorder=3)

# Plot smooth fitting curve
plt.plot(smooth_years, smooth_sessions, color='green', label='Trend Line (Quadratic Fit)', linewidth=2, zorder=2)

# Add title and labels with line breaks for clarity
plt.title('Mapping the Sky:\nThe Rise of Astronomy Interest through Star-Gazing Sessions (2020-2030)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Sessions', fontsize=14)

# Annotate a significant trend in 2028
plt.annotate('Significant boost in 2028', xy=(2028, 255), xytext=(2024, 280),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Customize ticks for clarity
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 401, 50))

# Legend to differentiate scatter points and fitting line
plt.legend(loc='upper left', fontsize=12)

# Add grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()