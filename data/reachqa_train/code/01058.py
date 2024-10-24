import matplotlib.pyplot as plt
import numpy as np

# Departments
departments = ['Research & Dev', 'Marketing', 'HR', 'Sales', 'IT', 'Customer Service']

# Satisfaction scores for work-life balance initiatives
satisfaction_scores = {
    'Research & Dev': [8, 9, 7, 9, 6, 8, 9, 10, 7, 8],
    'Marketing': [6, 5, 7, 6, 6, 5, 7, 8, 6, 5],
    'HR': [9, 8, 8, 9, 7, 8, 8, 9, 9, 8],
    'Sales': [5, 6, 5, 4, 6, 5, 6, 7, 5, 6],
    'IT': [7, 8, 8, 7, 6, 7, 7, 8, 7, 6],
    'Customer Service': [6, 5, 6, 5, 7, 6, 5, 6, 5, 6]
}

# Extract data for plotting
data = [satisfaction_scores[dept] for dept in departments]

# Create horizontal box plot
plt.figure(figsize=(10, 6))
bplot = plt.boxplot(data, vert=False, patch_artist=True, labels=departments,
                    boxprops=dict(facecolor='lightblue', color='navy', alpha=0.7),
                    whiskerprops=dict(color='navy'),
                    capprops=dict(color='navy'),
                    medianprops=dict(color='darkred', linewidth=2),
                    flierprops=dict(marker='o', color='red', alpha=0.5),
                    notch=True, whis=1.5)

# Colorize each box differently
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FFB6C1']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Add title and labels
plt.title("Impact of Work-Life Balance Initiatives\non Employee Satisfaction Across Departments", fontsize=14, fontweight='bold')
plt.xlabel("Satisfaction Score (1-10)", fontsize=12)
plt.ylabel("Departments", fontsize=12)

# Add grid for clarity
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate with average satisfaction score per department
for i, scores in enumerate(data):
    mean_score = np.mean(scores)
    plt.text(mean_score + 0.1, i + 1, f'Avg: {mean_score:.1f}', verticalalignment='center', color='darkgreen')

# Automatically adjust the layout for better fit and visibility
plt.tight_layout()

# Display plot
plt.show()