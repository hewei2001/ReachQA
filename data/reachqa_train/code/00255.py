import matplotlib.pyplot as plt
import numpy as np

# Define satisfaction scores for each department
satisfaction_data = {
    'Engineering': [7, 8, 8, 7, 6, 7, 9, 8, 7, 8, 9, 9, 8, 7, 8, 6, 7, 9, 7, 8],
    'Design': [6, 5, 7, 6, 5, 5, 7, 6, 5, 6, 6, 5, 5, 6, 7, 5, 6],
    'Marketing': [8, 9, 8, 9, 7, 8, 8, 9, 8, 7, 9, 8, 9, 8, 9, 7],
    'HR': [7, 6, 7, 8, 6, 7, 6, 7, 8, 6, 7, 8, 8, 7, 8, 7, 7],
    'Sales': [5, 6, 5, 4, 5, 6, 7, 5, 6, 5, 6, 5, 5, 4, 5, 6],
    'Support': [6, 7, 7, 8, 6, 7, 8, 9, 6, 7, 8, 6, 7, 6, 7, 8, 7]
}

# Extract department names and corresponding data
departments = list(satisfaction_data.keys())
scores = list(satisfaction_data.values())

# Create a vertical box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(scores, vert=True, patch_artist=True, notch=True, widths=0.5,
                  boxprops=dict(facecolor='#ADD8E6', color='darkblue', linewidth=1.5),
                  capprops=dict(color='darkblue', linewidth=1.5),
                  whiskerprops=dict(color='darkblue', linewidth=1.5),
                  flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'),
                  medianprops=dict(color='orange', linewidth=2))

# Title and labels
plt.title('Employee Satisfaction Survey\nResults Across Departments at TechWave', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Satisfaction Score', fontsize=12)

# Set x-tick labels to department names
plt.xticks(ticks=np.arange(1, len(departments) + 1), labels=departments, rotation=30, ha='right', fontsize=10)

# Enable grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()