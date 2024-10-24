import matplotlib.pyplot as plt
import numpy as np

# Data: Engagement Scores and Final Grades based on Digital Content Usage (Hours)
digital_content_hours = np.array([2, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35])
engagement_scores = np.array([55, 65, 70, 75, 80, 85, 88, 90, 92, 95, 97])
final_grades = np.array([50, 60, 63, 68, 72, 76, 80, 83, 85, 89, 92])

# Create scatter plot
plt.figure(figsize=(10, 7))
scatter = plt.scatter(
    digital_content_hours, 
    final_grades, 
    c=engagement_scores, 
    cmap='viridis', 
    s=150, 
    edgecolor='k', 
    alpha=0.7
)

# Add a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Engagement Score', fontsize=12)

# Add titles and labels
plt.title('Impact of Digital Content on Student Performance\nBased on Engagement and Final Grades', fontsize=14, fontweight='bold')
plt.xlabel('Digital Content Usage (Hours/Week)', fontsize=12)
plt.ylabel('Final Grade (%)', fontsize=12)

# Customize grid
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()