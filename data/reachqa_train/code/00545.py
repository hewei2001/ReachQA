import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years from 2025 to 2040
years = np.arange(2025, 2041)

# Performance scores for autonomous robots in different sports
robo_soccer_scores = np.array([60, 63, 67, 72, 78, 85, 93, 102, 112, 123, 135, 148, 162, 177, 193, 210])
cyber_basketball_scores = np.array([50, 54, 59, 65, 72, 80, 89, 99, 110, 122, 135, 149, 164, 180, 197, 215])
digital_tennis_scores = np.array([55, 58, 62, 67, 73, 80, 88, 97, 107, 118, 130, 143, 157, 172, 188, 205])

# Create a figure and axis
plt.figure(figsize=(14, 8))

# Plot scatter points for each sport
plt.scatter(years, robo_soccer_scores, label='Robo-Soccer', color='blue', s=50, alpha=0.7, edgecolor='k')
plt.scatter(years, cyber_basketball_scores, label='Cyber-Basketball', color='green', s=50, alpha=0.7, edgecolor='k')
plt.scatter(years, digital_tennis_scores, label='Digital Tennis', color='red', s=50, alpha=0.7, edgecolor='k')

# Spline interpolation for smooth fitting
year_smooth = np.linspace(2025, 2040, 300)
robo_soccer_spline = make_interp_spline(years, robo_soccer_scores)(year_smooth)
cyber_basketball_spline = make_interp_spline(years, cyber_basketball_scores)(year_smooth)
digital_tennis_spline = make_interp_spline(years, digital_tennis_scores)(year_smooth)

# Plot the smooth curves
plt.plot(year_smooth, robo_soccer_spline, color='blue', linestyle='-', linewidth=2)
plt.plot(year_smooth, cyber_basketball_spline, color='green', linestyle='-', linewidth=2)
plt.plot(year_smooth, digital_tennis_spline, color='red', linestyle='-', linewidth=2)

# Add chart details
plt.title('Projected Growth of Autonomous Sports Robots: 2025-2040\nPerformance Scores in Key Sports', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Performance Score', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(50, 251, 25))
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(loc='upper left', fontsize=10, title='Sports Discipline', title_fontsize='13')

# Use tight layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()