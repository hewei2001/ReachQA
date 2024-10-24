import matplotlib.pyplot as plt
import numpy as np

# Define study hours and corresponding test scores for 30 students
study_hours = np.array([4, 6, 3, 8, 10, 12, 5, 9, 7, 13,
                        11, 2, 15, 14, 7, 4, 6, 10, 5, 9,
                        8, 3, 11, 12, 14, 9, 6, 5, 10, 7])

# Simulated test scores with some variance added
test_scores = np.array([55, 65, 50, 72, 85, 90, 60, 78, 67, 94,
                        88, 42, 98, 95, 68, 54, 63, 82, 59, 76,
                        71, 49, 83, 88, 92, 77, 60, 56, 84, 69])

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(study_hours, test_scores, color='mediumslateblue', alpha=0.7, edgecolors='black', linewidth=0.5, s=100)

# Title and labels
plt.title("Star Student: Exploring Study Hours vs. Test Scores", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Study Hours per Week", fontsize=12)
plt.ylabel("Test Scores (out of 100)", fontsize=12)

# Customize ticks for better clarity
plt.xticks(np.arange(0, 17, 2))
plt.yticks(np.arange(40, 110, 10))

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Annotations to highlight specific observations
plt.annotate('High Performer', xy=(15, 98), xytext=(12, 90),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=10, color='darkred', fontweight='bold')

plt.annotate('Average Performance Zone', xy=(7, 68), xytext=(3, 80),
             arrowprops=dict(facecolor='green', arrowstyle='->'),
             fontsize=10, color='green', fontweight='bold')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()