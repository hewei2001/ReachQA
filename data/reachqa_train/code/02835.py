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

# Economic impact data for bar chart (in billion dollars)
economic_impact = np.array([5, 12, 22, 40, 65, 70, 90, 120, 150])

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Subplot 1: Scatter plot with trend line
ax1.scatter(years, cultural_impact, color='navy', alpha=0.7, s=100, label="AI Innovations")
for i, innovation in enumerate(innovations):
    ax1.text(years[i], cultural_impact[i] + 2, innovation, fontsize=9, ha='center', color='darkred')

years_new = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, cultural_impact, k=3)
cultural_impact_smooth = spl(years_new)

ax1.plot(years_new, cultural_impact_smooth, color='orangered', linewidth=2, linestyle='--', label='Trend Line')
ax1.set_title('Cultural Impact of AI Innovations\nOver Time (2000 - 2040)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year of Innovation', fontsize=12)
ax1.set_ylabel('Cultural Impact Score', fontsize=12)
ax1.set_xticks(np.arange(2000, 2045, 5))
ax1.set_yticks(np.arange(0, 110, 10))
ax1.set_ylim(0, 100)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left')

# Subplot 2: Bar chart for economic impact
ax2.bar(years, economic_impact, color='darkorange', alpha=0.7, label="Economic Impact")
ax2.set_title('Economic Impact of AI Innovations\n(2000 - 2040)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year of Innovation', fontsize=12)
ax2.set_ylabel('Economic Impact (in billion $)', fontsize=12)
ax2.set_xticks(np.arange(2000, 2045, 5))
ax2.set_yticks(np.arange(0, 200, 20))
ax2.set_ylim(0, 160)
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()