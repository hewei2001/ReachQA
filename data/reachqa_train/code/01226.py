import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Expanded data set for 50 students
study_hours = np.array([4, 6, 3, 8, 10, 12, 5, 9, 7, 13, 11, 2, 15, 14, 7, 4, 6, 10, 5, 9,
                        8, 3, 11, 12, 14, 9, 6, 5, 10, 7, 5, 8, 12, 13, 14, 15, 16, 10, 11, 2,
                        3, 4, 5, 7, 6, 8, 9, 10, 11, 12])

# Corresponding test scores with variance
test_scores = np.array([55, 65, 50, 72, 85, 90, 60, 78, 67, 94, 88, 42, 98, 95, 68, 54, 63, 82, 59, 76,
                        71, 49, 83, 88, 92, 77, 60, 56, 84, 69, 62, 70, 86, 90, 93, 97, 100, 80, 87, 48,
                        51, 57, 62, 66, 64, 74, 79, 82, 85, 89])

# Divide students into two groups for comparison
group_labels = np.array(['A'] * 25 + ['B'] * 25)
colors = ['mediumslateblue' if label == 'A' else 'salmon' for label in group_labels]

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# Plot for study hours vs test scores with group differentiation
ax[0].scatter(study_hours, test_scores, color=colors, alpha=0.7, edgecolors='black', linewidth=0.5, s=100)
ax[0].set_title("Study Hours vs. Test Scores: Group Comparison", fontsize=14, fontweight='bold', pad=15)
ax[0].set_xlabel("Study Hours per Week", fontsize=12)
ax[0].set_ylabel("Test Scores (out of 100)", fontsize=12)
ax[0].set_xticks(np.arange(0, 18, 2))
ax[0].set_yticks(np.arange(40, 110, 10))
ax[0].grid(True, linestyle='--', alpha=0.6)

# Add regression line
X = study_hours.reshape(-1, 1)
y = test_scores
reg = LinearRegression().fit(X, y)
reg_line = reg.predict(X)
ax[0].plot(study_hours, reg_line, color='darkblue', linestyle='dashed', linewidth=1.5)

# Annotate significant points
ax[0].annotate('High Performer', xy=(15, 98), xytext=(12, 90),
               arrowprops=dict(facecolor='red', arrowstyle='->'),
               fontsize=10, color='darkred', fontweight='bold')

ax[0].annotate('Average Performance', xy=(7, 68), xytext=(3, 80),
               arrowprops=dict(facecolor='green', arrowstyle='->'),
               fontsize=10, color='green', fontweight='bold')

# Second subplot for variance and distribution
mean_scores = [np.mean(test_scores[group_labels == 'A']), np.mean(test_scores[group_labels == 'B'])]
ax[1].bar(['Group A', 'Group B'], mean_scores, color=['mediumslateblue', 'salmon'], alpha=0.7)
ax[1].set_title("Average Test Scores by Group", fontsize=14, fontweight='bold', pad=15)
ax[1].set_ylabel("Average Test Score", fontsize=12)
ax[1].set_ylim(40, 100)
ax[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()