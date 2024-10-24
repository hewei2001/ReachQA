import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years from 2025 to 2040
years = np.arange(2025, 2041)

# Performance scores for autonomous robots in different sports
robo_soccer_scores = np.array([60, 63, 67, 72, 78, 85, 93, 102, 112, 123, 135, 148, 162, 177, 193, 210])
cyber_basketball_scores = np.array([50, 54, 59, 65, 72, 80, 89, 99, 110, 122, 135, 149, 164, 180, 197, 215])
digital_tennis_scores = np.array([55, 58, 62, 67, 73, 80, 88, 97, 107, 118, 130, 143, 157, 172, 188, 205])

# Additional dataset for Robo-Agility scores
robo_agility_scores = np.array([40, 44, 49, 55, 62, 70, 79, 89, 100, 112, 125, 139, 154, 170, 187, 205])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(16, 9))

# Plot scatter points for each sport
ax.scatter(years, robo_soccer_scores, label='Robo-Soccer', color='blue', s=50, alpha=0.7, edgecolor='k')
ax.scatter(years, cyber_basketball_scores, label='Cyber-Basketball', color='green', s=50, alpha=0.7, edgecolor='k')
ax.scatter(years, digital_tennis_scores, label='Digital Tennis', color='red', s=50, alpha=0.7, edgecolor='k')

# Spline interpolation for smooth fitting
year_smooth = np.linspace(2025, 2040, 300)
robo_soccer_spline = make_interp_spline(years, robo_soccer_scores)(year_smooth)
cyber_basketball_spline = make_interp_spline(years, cyber_basketball_scores)(year_smooth)
digital_tennis_spline = make_interp_spline(years, digital_tennis_scores)(year_smooth)

# Plot the smooth curves
ax.plot(year_smooth, robo_soccer_spline, color='blue', linestyle='-', linewidth=2)
ax.plot(year_smooth, cyber_basketball_spline, color='green', linestyle='-', linewidth=2)
ax.plot(year_smooth, digital_tennis_spline, color='red', linestyle='-', linewidth=2)

# Overlay plot for Robo-Agility as bar chart
ax.bar(years - 0.3, robo_agility_scores, width=0.5, color='purple', alpha=0.5, label='Robo-Agility')

# Add chart details
title = 'Projected Growth of Autonomous Sports Robots: 2025-2040\n'
title += 'Performance Scores in Key Sports and Robo-Agility'
ax.set_title(title, fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(40, 251, 20))
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.legend(loc='upper left', fontsize=10, title='Metrics', title_fontsize='13')

# Use tight layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()