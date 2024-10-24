import matplotlib.pyplot as plt

# Original test scores for five schools
lincoln_scores = [78, 82, 85, 90, 87, 83, 89, 95, 91, 88, 90, 77, 85, 82, 86, 87, 93, 92, 81, 79]
kennedy_scores = [84, 89, 85, 87, 92, 88, 90, 85, 91, 80, 86, 83, 95, 93, 88, 84, 87, 89, 90, 92]
roosevelt_scores = [72, 78, 80, 77, 79, 82, 85, 87, 88, 76, 81, 83, 86, 75, 80, 77, 84, 79, 82, 76]
jefferson_scores = [88, 92, 90, 86, 94, 89, 91, 95, 93, 87, 92, 88, 90, 91, 87, 94, 96, 92, 90, 88]
washington_scores = [85, 88, 82, 87, 90, 86, 89, 84, 91, 82, 90, 88, 87, 85, 92, 93, 89, 88, 90, 87]

# Simulated average scores over 5 years for each school
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
avg_scores_lincoln = [82, 84, 88, 90, 92]
avg_scores_kennedy = [87, 88, 89, 90, 92]
avg_scores_roosevelt = [76, 78, 81, 83, 85]
avg_scores_jefferson = [90, 92, 94, 96, 97]
avg_scores_washington = [86, 87, 88, 90, 91]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Box plot
all_scores = [lincoln_scores, kennedy_scores, roosevelt_scores, jefferson_scores, washington_scores]
axes[0].boxplot(all_scores, vert=True, patch_artist=True, notch=True,
                boxprops=dict(facecolor='lightblue', color='navy'),
                whiskerprops=dict(color='navy'),
                capprops=dict(color='navy'),
                flierprops=dict(markerfacecolor='red', marker='o', markersize=7, linestyle='none', markeredgecolor='navy'),
                medianprops=dict(color='green'))

# Labels for box plot
axes[0].set_title("Box Plot of Test Scores Across Schools", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Schools", fontsize=12)
axes[0].set_ylabel("Math Test Scores", fontsize=12)
axes[0].set_xticklabels(['Lincoln High', 'Kennedy Prep', 'Roosevelt Academy', 'Jefferson School', 'Washington Institute'], fontsize=10)
axes[0].yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add annotation
axes[0].annotate('Top Performer', xy=(4, 94), xytext=(3.5, 96),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, fontweight='bold', color='black')

# Line plot
axes[1].plot(years, avg_scores_lincoln, label='Lincoln High', marker='o')
axes[1].plot(years, avg_scores_kennedy, label='Kennedy Prep', marker='o')
axes[1].plot(years, avg_scores_roosevelt, label='Roosevelt Academy', marker='o')
axes[1].plot(years, avg_scores_jefferson, label='Jefferson School', marker='o')
axes[1].plot(years, avg_scores_washington, label='Washington Institute', marker='o')

# Labels for line plot
axes[1].set_title("Trend of Average Test Scores Over 5 Years", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Years", fontsize=12)
axes[1].set_ylabel("Average Math Test Scores", fontsize=12)
axes[1].legend(loc='lower left', fontsize=10)
axes[1].yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()