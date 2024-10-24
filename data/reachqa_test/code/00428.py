import matplotlib.pyplot as plt
import numpy as np

# Weeks of the semester
weeks = np.arange(1, 16)

# Specific scores for each subject (adjusted to be more realistic)
math_scores = 50 + 5 * np.sin(0.5 * weeks) + 2 * weeks + np.array([1, -2, 3, -4, 2, 3, -1, 0, 4, -3, 1, 2, -1, 2, -2])
science_scores = 48 + 4 * np.cos(0.3 * weeks) + 1.5 * weeks + np.array([-2, 1, -3, 2, 3, -1, 1, -2, 3, 4, -3, -1, 2, 3, 1])
english_scores = 60 + 4 * np.sin(0.2 * weeks) + 1.8 * weeks + np.array([2, -1, 2, -2, 3, 0, -1, 2, 1, -3, 3, -2, 1, 0, 2])
history_scores = 42 + 3 * np.cos(0.4 * weeks) + 1.7 * weeks + np.array([-3, 1, 2, -1, 1, 3, -2, -1, 4, -2, 0, 3, 1, -1, 1])
art_scores = 55 + 2 * np.sin(0.5 * weeks) + 1.3 * weeks + np.array([0, 2, -1, 3, -2, 1, 4, -1, 0, 2, -3, 1, 2, 0, -2])

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each subject
ax.plot(weeks, math_scores, label='Mathematics', marker='o', linewidth=2)
ax.plot(weeks, science_scores, label='Science', marker='s', linewidth=2)
ax.plot(weeks, english_scores, label='English', marker='^', linewidth=2)
ax.plot(weeks, history_scores, label='History', marker='d', linewidth=2)
ax.plot(weeks, art_scores, label='Art', marker='x', linewidth=2)

# Add title and axis labels
ax.set_title("Student Progress Over a Semester", fontsize=16, fontweight='bold')
ax.set_xlabel('Weeks of Semester', fontsize=14)
ax.set_ylabel('Average Score (%)', fontsize=14)

# Add legend
ax.legend(loc='upper left', fontsize=12, title='Subjects')

# Enable grid with a simpler style
ax.grid(True, linestyle='-', alpha=0.3)

# Annotate significant events with adjusted coordinates
ax.annotate('Math Mid-term Boost', xy=(8, 81), xytext=(9, 85),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Science Week Challenge', xy=(10, 63), xytext=(9.5, 70),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='red')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()
