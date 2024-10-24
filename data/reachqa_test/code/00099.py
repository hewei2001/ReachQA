import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for weekly study hours and corresponding GPA values
study_hours = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
gpa = np.array([2.0, 2.3, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.65, 3.68])

# Define a related but different data set: Engagement Scores
engagement_scores = np.array([30, 45, 55, 60, 70, 80, 85, 90, 92, 94])

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create a scatter plot for study hours vs. GPA
ax1.scatter(study_hours, gpa, color='navy', label='Student GPA Data', s=80, alpha=0.7, edgecolor='k')

# Smooth fitting using spline interpolation
X_Y_Spline = make_interp_spline(study_hours, gpa)
X_ = np.linspace(study_hours.min(), study_hours.max(), 500)
Y_ = X_Y_Spline(X_)

# Plot the smooth fitting line
ax1.plot(X_, Y_, color='orange', linewidth=2.5, linestyle='-', label='GPA Trend Line')

# Create a bar plot for Engagement Scores with a secondary y-axis
ax2 = ax1.twinx()
ax2.bar(study_hours, engagement_scores, width=3, color='lightgreen', alpha=0.5, label='Engagement Score')

# Annotations for significant insights
annotations = {
    10: "Balanced Schedule",
    25: "Optimal Study Hours",
    50: "Plateau Effect"
}

for hour, text in annotations.items():
    idx = np.where(study_hours == hour)[0][0]
    y_position = gpa[idx] + 0.15 if hour % 2 == 0 else gpa[idx] - 0.2
    ax1.annotate(
        text,
        xy=(hour, gpa[idx]),
        xytext=(hour + 2, y_position),
        arrowprops=dict(facecolor='grey', arrowstyle="->"),
        fontsize=9,
        bbox=dict(facecolor='lightgray', alpha=0.7, edgecolor='none')
    )

# Titles and labels
ax1.set_title('Correlation Between Study Hours and Academic Performance\nwith Engagement Scores', fontsize=16, fontweight='bold')
ax1.set_xlabel('Weekly Study Hours', fontsize=12)
ax1.set_ylabel('GPA (Grade Point Average)', fontsize=12, color='navy')
ax2.set_ylabel('Engagement Score', fontsize=12, color='darkgreen')

# Customize the grid and aesthetics
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legends
ax1.legend(loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()