import matplotlib.pyplot as plt
import numpy as np

# Data preparation
cardio_hours = [5, 6, 5, 4, 3, 3, 2, 1, 6, 7, 8, 6]
strength_training_hours = [3, 4, 5, 4, 5, 5, 6, 7, 4, 3, 3, 2]
yoga_hours = [2, 1, 3, 4, 5, 6, 7, 8, 2, 3, 3, 4]
hiit_hours = [4, 5, 4, 3, 2, 2, 1, 1, 4, 5, 6, 7]
data = [cardio_hours, strength_training_hours, yoga_hours, hiit_hours]
exercise_types = ['Cardio', 'Strength\nTraining', 'Yoga', 'HIIT']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Calculate mean workout hours for each exercise type
mean_hours = [np.mean(hours) for hours in data]

# Create the figure and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
fig.suptitle("Analysis of Weekly Workout Hours by Exercise Type\nA Study of Fitness Preferences", fontsize=16, weight='bold')

# Subplot 1: Boxplot
axes[0].boxplot(data, vert=False, patch_artist=True, labels=exercise_types, notch=True, whis=1.5)
for patch, color in zip(axes[0].artists, colors):
    patch.set_facecolor(color)
plt.setp(axes[0].lines, color='black', linestyle='--')
axes[0].set_xlabel("Weekly Workout Hours", fontsize=12)
axes[0].set_ylabel("Exercise Type", fontsize=12)
axes[0].set_title("Distribution of Workout Hours", fontsize=14)
axes[0].xaxis.grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Bar Chart
axes[1].bar(exercise_types, mean_hours, color=colors, edgecolor='black')
for i, mean in enumerate(mean_hours):
    axes[1].text(i, mean + 0.1, f'{mean:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
axes[1].set_title("Average Weekly Workout Hours", fontsize=14)
axes[1].set_ylabel("Average Hours", fontsize=12)
axes[1].set_xlabel("Exercise Type", fontsize=12)

# Automatically adjust layout to fit all elements
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()