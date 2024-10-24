import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Defining years and cultural impact scores for AI innovations
years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040])
cultural_impact = np.array([15, 28, 43, 60, 75, 67, 82, 85, 93])

# Innovation labels for scatter plot
innovations = [
    "Basic AI", "Voice Assistants", "Image Recognition",
    "AI in Entertainment", "AI-Generated Art",
    "Autonomous Vehicles", "Advanced Robotics",
    "Quantum AI", "Conscious AI"
]

# Create the plot
plt.figure(figsize=(12, 8))

# Scatter plot of AI innovations
plt.scatter(years, cultural_impact, color='navy', alpha=0.7, s=100, label="AI Innovations")

# Adding labels for each point, positioned slightly above the points
for i, innovation in enumerate(innovations):
    plt.text(years[i], cultural_impact[i] + 2, innovation, fontsize=9, ha='center', color='darkred')

# Fitting a smooth curve using a cubic spline
years_new = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, cultural_impact, k=3)
cultural_impact_smooth = spl(years_new)

# Plot the smooth fitting line
plt.plot(years_new, cultural_impact_smooth, color='orangered', linewidth=2, linestyle='--', label='Trend Line')

# Title and labels
plt.title('Cultural Impact of AI Innovations\nOver Time (2000 - 2040)', fontsize=16, fontweight='bold')
plt.xlabel('Year of Innovation', fontsize=12)
plt.ylabel('Cultural Impact Score', fontsize=12)

# Axis ticks and limits
plt.xticks(np.arange(2000, 2045, 5))
plt.yticks(np.arange(0, 110, 10))
plt.ylim(0, 100)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legend
plt.legend(loc='upper left')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()