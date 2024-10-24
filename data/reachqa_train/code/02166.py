import matplotlib.pyplot as plt

# Test scores for five schools
lincoln_scores = [78, 82, 85, 90, 87, 83, 89, 95, 91, 88, 90, 77, 85, 82, 86, 87, 93, 92, 81, 79]
kennedy_scores = [84, 89, 85, 87, 92, 88, 90, 85, 91, 80, 86, 83, 95, 93, 88, 84, 87, 89, 90, 92]
roosevelt_scores = [72, 78, 80, 77, 79, 82, 85, 87, 88, 76, 81, 83, 86, 75, 80, 77, 84, 79, 82, 76]
jefferson_scores = [88, 92, 90, 86, 94, 89, 91, 95, 93, 87, 92, 88, 90, 91, 87, 94, 96, 92, 90, 88]
washington_scores = [85, 88, 82, 87, 90, 86, 89, 84, 91, 82, 90, 88, 87, 85, 92, 93, 89, 88, 90, 87]

# Aggregate the scores for the box plot
all_scores = [lincoln_scores, kennedy_scores, roosevelt_scores, jefferson_scores, washington_scores]

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.boxplot(all_scores, vert=True, patch_artist=True, notch=True,
           boxprops=dict(facecolor='lightblue', color='navy'),
           whiskerprops=dict(color='navy'),
           capprops=dict(color='navy'),
           flierprops=dict(markerfacecolor='red', marker='o', markersize=7, linestyle='none', markeredgecolor='navy'),
           medianprops=dict(color='green'))

# Set chart titles and labels
ax.set_title("Math Mastery Unveiled:\nComparative Analysis of Standardized Test Scores Across Schools", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Schools", fontsize=14)
ax.set_ylabel("Math Test Scores", fontsize=14)

# X-axis labels
ax.set_xticklabels(['Lincoln High', 'Kennedy Prep', 'Roosevelt Academy', 'Jefferson School', 'Washington Institute'], fontsize=12)

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight notable observations
ax.annotate('Top Performer', xy=(4, 94), xytext=(3.5, 96),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, fontweight='bold', color='black')

# Tight layout to prevent clipping
plt.tight_layout()

# Show plot
plt.show()