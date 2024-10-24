import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years of observation
years = np.arange(1, 11)

# Practice hours (in hundreds) and Performance scores (out of 100)
musician_data = {
    "Musician 1": (np.array([1.2, 1.8, 2.5, 3.0, 3.7, 4.2, 4.8, 5.0, 5.5, 6.0]), np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])),
    "Musician 2": (np.array([0.8, 1.5, 2.0, 2.3, 2.8, 3.5, 4.0, 4.2, 4.9, 5.3]), np.array([45, 50, 55, 58, 62, 68, 73, 78, 83, 87])),
    "Musician 3": (np.array([1.5, 2.0, 2.8, 3.3, 3.9, 4.5, 5.2, 5.6, 6.1, 6.5]), np.array([52, 57, 63, 67, 72, 78, 83, 88, 92, 97])),
    "Musician 4": (np.array([0.5, 1.0, 1.7, 2.0, 2.5, 3.0, 3.8, 4.0, 4.3, 4.8]), np.array([40, 48, 52, 56, 60, 65, 71, 74, 77, 81])),
    "Musician 5": (np.array([0.9, 1.3, 2.1, 2.7, 3.3, 4.0, 4.5, 4.9, 5.2, 5.8]), np.array([47, 51, 58, 64, 69, 76, 82, 85, 89, 94]))
}

years_smooth = np.linspace(years.min(), years.max(), 300)
colors = ['#ff6347', '#4682b4', '#32cd32', '#ff69b4', '#ffa500']

plt.figure(figsize=(14, 8))
for i, (musician, data) in enumerate(musician_data.items()):
    hours, scores = data
    spline = make_interp_spline(years, scores, k=3)
    
    # Scatter plot for practice hours vs performance score
    plt.scatter(years, scores, color=colors[i], label=f"{musician}", s=50, alpha=0.7, edgecolors='w')
    # Smooth spline curve
    plt.plot(years_smooth, spline(years_smooth), color=colors[i], linestyle='-', linewidth=2)

# Enhancements
plt.title("The Symphony of Practice: Linking Hours to Mastery", fontsize=16, fontweight='bold')
plt.xlabel("Years of Practice", fontsize=12)
plt.ylabel("Performance Score", fontsize=12)
plt.legend(title="Musicians", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(years)

# Auto-adjust layout
plt.tight_layout()

# Display the plot
plt.show()