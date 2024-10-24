import matplotlib.pyplot as plt
import numpy as np

# Data: Study hours (per week) and corresponding exam scores (%)
study_hours = [5, 8, 12, 15, 20, 18, 10, 7, 14, 17, 25, 23, 9, 11, 13]
exam_scores = [55, 65, 78, 88, 90, 85, 70, 60, 80, 89, 95, 92, 67, 75, 83]

# Initialize the plot
plt.figure(figsize=(12, 8))
plt.scatter(study_hours, exam_scores, color='blue', alpha=0.6, edgecolors='w', s=100)

# Fit and plot a linear regression line
m, b = np.polyfit(study_hours, exam_scores, 1)
plt.plot(study_hours, np.array(study_hours) * m + b, color='red', linestyle='--', linewidth=2, label='Trend Line')

# Customize plot labels and title
plt.title("Math Mastery Exam:\nStudy Hours vs. Exam Scores", fontsize=16, fontweight='bold')
plt.xlabel("Study Hours (per week)", fontsize=12)
plt.ylabel("Exam Score (%)", fontsize=12)

# Add grid and legend
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='lower right')

# Automatic layout adjustment
plt.tight_layout()

# Show the plot
plt.show()