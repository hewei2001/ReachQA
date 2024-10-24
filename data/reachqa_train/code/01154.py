import matplotlib.pyplot as plt
import numpy as np

# Define productivity scores for different industries
technology_scores = [85, 90, 87, 92, 88, 94, 89, 93, 95, 86]
healthcare_scores = [70, 75, 72, 74, 71, 73, 69, 76, 74, 72]
finance_scores = [82, 78, 80, 79, 84, 77, 85, 81, 83, 79]
education_scores = [65, 68, 67, 70, 66, 69, 71, 64, 68, 67]
retail_scores = [60, 62, 59, 58, 61, 63, 57, 64, 60, 62]

# Combine data into a list
data = [technology_scores, healthcare_scores, finance_scores, education_scores, retail_scores]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the vertical box plot
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, 
                boxprops=dict(facecolor='lightgray', color='blue'),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'),
                medianprops=dict(color='darkred', linewidth=2))

# Customize box colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set the title and labels
ax.set_title("Remote Work Productivity Scores\nAcross Different Industries", fontsize=16, fontweight='bold')
ax.set_xlabel("Industry", fontsize=14)
ax.set_ylabel("Productivity Score", fontsize=14)

# Set x-tick labels
ax.set_xticklabels(['Technology', 'Healthcare', 'Finance', 'Education', 'Retail'], fontsize=12)

# Add annotations for insights
ax.text(1.1, 95, 'High Peak', fontsize=11, color='#1f77b4')
ax.text(2.1, 76, 'Varied Range', fontsize=11, color='#ff7f0e')
ax.text(3.1, 85, 'Stable Scores', fontsize=11, color='#2ca02c')

# Enhance grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure layout is tidy
plt.tight_layout()

# Show the plot
plt.show()