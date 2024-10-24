import matplotlib.pyplot as plt
import numpy as np

# Define departments
departments = ['Development', 'Marketing', 'HR', 'IT Support', 'Sales']

# Construct satisfaction score data for each department
development_scores = [8, 7, 9, 7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 7]
marketing_scores = [6, 5, 7, 6, 6, 5, 7, 6, 5, 6, 4, 6, 5, 7]
hr_scores = [9, 8, 9, 10, 9, 8, 9, 10, 8, 9, 10, 9, 10, 9]
it_support_scores = [7, 6, 6, 7, 5, 6, 7, 6, 7, 5, 6, 7, 6, 5]
sales_scores = [5, 6, 5, 4, 5, 6, 5, 6, 7, 5, 4, 6, 5, 4]

# Combine data
data = [development_scores, marketing_scores, hr_scores, it_support_scores, sales_scores]

# Calculate means for annotation
means = [np.mean(d) for d in data]

# Calculate variances for subplot
variances = [np.var(d) for d in data]

# Set up the figure and subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Main box plot
boxplot = axes[0].boxplot(data, vert=False, patch_artist=True, labels=departments, 
                          boxprops=dict(color='black'), whiskerprops=dict(color='black'),
                          capprops=dict(color='black'), medianprops=dict(color='red'),
                          flierprops=dict(marker='o', color='orange', alpha=0.5), notch=True)

# Color gradient setup for boxes
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Overlay individual data points with jitter
for i, scores in enumerate(data):
    y = np.random.normal(i + 1, 0.04, size=len(scores))  # jitter
    axes[0].plot(scores, y, 'r.', alpha=0.5)

# Add mean annotations
for i, mean in enumerate(means):
    axes[0].annotate(f'Mean: {mean:.2f}', xy=(mean, i+1), xytext=(5, 0),
                     textcoords='offset points', ha='right', va='center', color='darkblue')

# Vertical reference lines
axes[0].axvline(x=5, color='grey', linestyle='--', linewidth=1, alpha=0.7, label='Neutral Threshold')
axes[0].axvline(x=8, color='purple', linestyle='--', linewidth=1, alpha=0.7, label='High Satisfaction')

# Customize the plot
axes[0].set_title("Employee Satisfaction Across Departments\nTech Company Survey Results", fontsize=16, fontweight='bold')
axes[0].set_xlabel("Satisfaction Score (0 - Very Dissatisfied, 10 - Very Satisfied)", fontsize=12)
axes[0].set_ylabel("Department", fontsize=12)
axes[0].legend(loc='upper right')

# Add a grid for better readability
axes[0].grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Variance bar plot as subplot
axes[1].barh(departments, variances, color=colors)
axes[1].set_title("Variance in Satisfaction Scores by Department", fontsize=14)
axes[1].set_xlabel("Variance", fontsize=12)
axes[1].set_ylabel("Department", fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()