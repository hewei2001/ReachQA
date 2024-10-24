import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Manually crafted study hours and exam scores data
study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
exam_scores = np.array([55, 60, 65, 68, 72, 78, 80, 84, 88, 93])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(study_hours, exam_scores, color='darkblue', edgecolor='black', s=100, alpha=0.7, label='Student Data')

# Create a smooth curve using spline interpolation
X_Y_Spline = make_interp_spline(study_hours, exam_scores, k=3)  # k=3 for cubic spline
X_ = np.linspace(study_hours.min(), study_hours.max(), 500)
Y_ = X_Y_Spline(X_)

# Plot the smooth fitting line
plt.plot(X_, Y_, color='lightcoral', linewidth=2.5, label='Trend Line')

# Add title and labels
plt.title('Impact of Study Hours on Mathematics Exam Performance\n(EduTech University Analysis)', fontsize=14, fontweight='bold')
plt.xlabel('Weekly Study Hours', fontsize=12)
plt.ylabel('Mathematics Exam Score', fontsize=12)

# Set axis limits for better visualization
plt.xlim(0, 22)
plt.ylim(50, 100)

# Add grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()