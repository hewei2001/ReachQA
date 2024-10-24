import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define decades and corresponding indices for technological innovation and environmental impact
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Technological Innovation Index (Arbitrary Units)
tech_innovation_index = np.array([50, 65, 85, 110, 135, 155])

# Environmental Impact Index (Arbitrary Units)
env_impact_index = np.array([210, 190, 165, 145, 125, 115])

# Create a smooth curve using spline interpolation
years = np.linspace(decades.min(), decades.max(), 300)
tech_spline = make_interp_spline(decades, tech_innovation_index, k=3)(years)
env_spline = make_interp_spline(decades, env_impact_index, k=3)(years)

# Initialize the plot
plt.figure(figsize=(14, 8))

# Scatter plot for technological innovation and environmental impact
plt.scatter(decades, tech_innovation_index, color='dodgerblue', marker='o', s=100, label='Tech Innovation', zorder=3)
plt.scatter(decades, env_impact_index, color='forestgreen', marker='s', s=100, label='Environmental Impact', zorder=3)

# Smooth fitting lines with confidence intervals
plt.plot(years, tech_spline, color='dodgerblue', linestyle='-', linewidth=2, alpha=0.7, zorder=2)
plt.fill_between(years, tech_spline * 0.9, tech_spline * 1.1, color='dodgerblue', alpha=0.1)

plt.plot(years, env_spline, color='forestgreen', linestyle='-', linewidth=2, alpha=0.7, zorder=2)
plt.fill_between(years, env_spline * 0.9, env_spline * 1.1, color='forestgreen', alpha=0.1)

# Title and axis labels
plt.title('Technological Advancement vs\nEnvironmental Impact Across Decades', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Decades', fontsize=14)
plt.ylabel('Index (Arbitrary Units)', fontsize=14)

# Custom ticks and grid
plt.xticks(decades, labels=['1970s', '1980s', '1990s', '2000s', '2010s', '2020s'], fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5, zorder=1)

# Add annotations for key points
plt.annotate('Start of Tech Boom', xy=(1980, 65), xytext=(1985, 90),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
plt.annotate('Start of Decline in Impact', xy=(2000, 145), xytext=(2005, 170),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Add legend
plt.legend(loc='upper right', fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()