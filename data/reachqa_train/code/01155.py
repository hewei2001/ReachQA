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

# Calculate means for each category
means = [np.mean(scores) for scores in data]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the vertical box plot with enhancements
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, 
                boxprops=dict(color='blue', facecolor='lightgrey'),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'),
                medianprops=dict(color='darkred', linewidth=2),
                meanprops=dict(marker='o', markerfacecolor='black', markeredgecolor='black'),
                showmeans=True)

# Color boxes with a gradient and update mean points
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(colors[i])

# Scatter the actual data points
for i, scores in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(scores))  # jitter the x positions
    ax.plot(y, scores, 'r.', alpha=0.6)

# Set the title and labels
ax.set_title("Remote Work Productivity Scores Across\nDifferent Industries", fontsize=16, fontweight='bold')
ax.set_xlabel("Industry", fontsize=14)
ax.set_ylabel("Productivity Score", fontsize=14)

# Set x-tick labels
ax.set_xticklabels(['Technology', 'Healthcare', 'Finance', 'Education', 'Retail'], fontsize=12, rotation=15)

# Add horizontal reference line for overall mean
overall_mean = np.mean([score for sublist in data for score in sublist])
ax.axhline(overall_mean, color='gray', linestyle='--', linewidth=1, label=f'Overall Mean: {overall_mean:.2f}')

# Enhance grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Customize annotations with arrows
ax.annotate('Highest Peak',
            xy=(1, max(technology_scores)), xycoords='data',
            xytext=(0.8, max(technology_scores) + 3), textcoords='data',
            arrowprops=dict(arrowstyle="->", color='blue'),
            fontsize=11, color='#1f77b4')

ax.annotate('Varied Range',
            xy=(2, 76), xycoords='data',
            xytext=(1.8, 78), textcoords='data',
            arrowprops=dict(arrowstyle="->", color='orange'),
            fontsize=11, color='#ff7f0e')

ax.annotate('Stable Scores',
            xy=(3, np.median(finance_scores)), xycoords='data',
            xytext=(2.8, np.median(finance_scores) + 2), textcoords='data',
            arrowprops=dict(arrowstyle="->", color='green'),
            fontsize=11, color='#2ca02c')

# Display the legend
ax.legend(loc='upper right', fontsize=11)

# Ensure layout is tidy
plt.tight_layout()

# Show the plot
plt.show()