import matplotlib.pyplot as plt
import numpy as np

# Define innovation scores for each industry
healthcare_scores = [65, 67, 70, 72, 74, 75, 76, 78, 80]
automotive_scores = [50, 55, 57, 58, 62, 65, 67, 68, 70]
finance_scores = [60, 63, 68, 70, 74, 77, 80, 82, 85]
retail_scores = [45, 48, 50, 52, 54, 56, 58, 60]
entertainment_scores = [50, 55, 58, 60, 65, 68, 70, 72, 75]

# Compile data into a list
data = [healthcare_scores, automotive_scores, finance_scores, retail_scores, entertainment_scores]

# Define industry labels
industries = ['Healthcare', 'Automotive', 'Finance', 'Retail', 'Entertainment']

# Define custom colors for each category
box_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Initialize the plot
plt.figure(figsize=(14, 7))

# Create the horizontal box plot
bplot = plt.boxplot(data, vert=False, patch_artist=True, notch=True,
                    boxprops=dict(facecolor='lightblue', color='darkblue', linewidth=1.5),
                    whiskerprops=dict(color='black', linewidth=1.5),
                    capprops=dict(color='black', linewidth=1.5),
                    flierprops=dict(marker='o', color='red', markersize=8),
                    medianprops=dict(color='darkred', linewidth=2))

# Customize box colors
for patch, color in zip(bplot['boxes'], box_colors):
    patch.set_facecolor(color)

# Add industry labels to y-axis
plt.yticks(np.arange(1, len(industries) + 1), industries)

# Add titles and labels
plt.title("AI Innovation Scores Across Industries\nThe Rise of Artificial Intelligence by Sector",
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Innovation Score", fontsize=12)
plt.ylabel("Industries", fontsize=12)

# Add grid lines for clarity
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()