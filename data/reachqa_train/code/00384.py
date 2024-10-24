import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Data: Engagement Scores and Final Grades based on Digital Content Usage (Hours)
digital_content_hours = np.array([2, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35])
engagement_scores = np.array([55, 65, 70, 75, 80, 85, 88, 90, 92, 95, 97])
final_grades = np.array([50, 60, 63, 68, 72, 76, 80, 83, 85, 89, 92])

# Polynomial fit for trend line
p = Polynomial.fit(digital_content_hours, final_grades, 2)
trend_line = p.linspace(n=100)

# Create figure and main scatter plot
fig, ax1 = plt.subplots(figsize=(12, 8))
scatter = ax1.scatter(
    digital_content_hours, 
    final_grades, 
    c=engagement_scores, 
    cmap='viridis', 
    s=150, 
    edgecolor='k', 
    alpha=0.7
)

# Overlay trend line
ax1.plot(trend_line[0], trend_line[1], color='red', linewidth=2, label='Polynomial Fit')

# Add color bar for engagement scores
cbar = plt.colorbar(scatter)
cbar.set_label('Engagement Score', fontsize=12)

# Customize axes and labels
ax1.set_title('Impact of Digital Content Usage on Student Performance', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Digital Content Usage (Hours/Week)', fontsize=12)
ax1.set_ylabel('Final Grade (%)', fontsize=12)
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Secondary y-axis for engagement scores
ax2 = ax1.twinx()
ax2.plot(digital_content_hours, engagement_scores, color='dodgerblue', marker='o', linestyle='--', label='Engagement Score')
ax2.set_ylabel('Engagement Score', fontsize=12, color='dodgerblue')

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()