import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define years and fictional data for the number of digital art projects and creativity index
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022])
digital_art_projects = np.array([5, 10, 15, 20, 30, 45, 60, 80, 100, 130, 170, 220])
creativity_index = np.array([50, 55, 60, 65, 72, 78, 84, 90, 96, 102, 108, 115])

# Create the scatter plot
plt.figure(figsize=(12, 7))
plt.scatter(digital_art_projects, creativity_index, color='darkcyan', label='Digital Art Projects')

# Fit a smooth curve using cubic spline interpolation
spline = make_interp_spline(digital_art_projects, creativity_index, k=3)  # Cubic spline
projects_range = np.linspace(min(digital_art_projects), max(digital_art_projects), 300)
creativity_smooth = spline(projects_range)

# Plot the smooth fitting curve
plt.plot(projects_range, creativity_smooth, color='lightcoral', linewidth=2.5, label='Creativity Trend')

# Set the title and labels
plt.title("The Digital Canvas:\nImpact of Digital Art Projects on Creativity Index", 
          fontsize=14, fontweight='bold', ha='center')
plt.xlabel("Number of Digital Art Projects", fontsize=12)
plt.ylabel("Creativity Index", fontsize=12)

# Add a legend to differentiate data points and trend line
plt.legend(title="Legend", loc='upper left', fontsize='medium')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()