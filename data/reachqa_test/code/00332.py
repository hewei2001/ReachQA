import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Define weeks
weeks = np.arange(1, 21)

# Define vocabulary sizes for different proficiency levels (in hundreds)
vocabulary_size_beginner = [2, 3, 5, 7, 12, 15, 17, 19, 25, 28, 34, 38, 42, 50, 54, 60, 65, 70, 72, 78]
vocabulary_size_intermediate = [10, 12, 15, 17, 20, 23, 26, 30, 33, 36, 40, 45, 50, 55, 60, 65, 70, 74, 78, 80]
vocabulary_size_advanced = [50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 84, 85, 87, 88, 89, 90]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Add scatter plots with a color gradient
cmap_beginner = plt.get_cmap('Blues')
cmap_intermediate = plt.get_cmap('Greens')
cmap_advanced = plt.get_cmap('Reds')

ax.scatter(weeks, vocabulary_size_beginner, c=weeks, cmap=cmap_beginner, label='Beginner', alpha=0.8, s=100, marker='o', edgecolors='black')
ax.scatter(weeks, vocabulary_size_intermediate, c=weeks, cmap=cmap_intermediate, label='Intermediate', alpha=0.8, s=100, marker='^', edgecolors='black')
ax.scatter(weeks, vocabulary_size_advanced, c=weeks, cmap=cmap_advanced, label='Advanced', alpha=0.8, s=100, marker='s', edgecolors='black')

# Add trend lines
slope_b, intercept_b, _, _, _ = stats.linregress(weeks, vocabulary_size_beginner)
slope_i, intercept_i, _, _, _ = stats.linregress(weeks, vocabulary_size_intermediate)
slope_a, intercept_a, _, _, _ = stats.linregress(weeks, vocabulary_size_advanced)

ax.plot(weeks, slope_b*weeks + intercept_b, color='navy', linestyle='--', lw=1.5)
ax.plot(weeks, slope_i*weeks + intercept_i, color='darkgreen', linestyle='--', lw=1.5)
ax.plot(weeks, slope_a*weeks + intercept_a, color='darkred', linestyle='--', lw=1.5)

# Customize plot aesthetics
ax.set_title("Vocabulary Development in Language Learning\nAcross Different Proficiency Levels", fontsize=16, weight='bold', color='darkblue')
ax.set_xlabel("Weeks of Learning", fontsize=12, weight='bold')
ax.set_ylabel("Vocabulary Size (in hundreds)", fontsize=12, weight='bold')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(title="Proficiency Level", fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Annotate key points
ax.annotate('Rapid Growth', xy=(14, 50), xytext=(7, 65),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='blue', weight='bold')

ax.annotate('Plateau Region', xy=(15, 85), xytext=(10, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='red', weight='bold')

# Additional detailed data visualization
ax.plot([], [], ' ', label="Trend Lines for each Level")  # Dummy entry for legend

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()