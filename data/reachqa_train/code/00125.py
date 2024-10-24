import matplotlib.pyplot as plt
import numpy as np

# Data: Number of coffee cups consumed per day by individuals in different professions
software_engineers = [4, 5, 6, 7, 4, 5, 6, 5, 8, 7, 5, 6, 4, 3, 7, 6, 5, 7, 8, 9]
teachers = [2, 3, 3, 4, 2, 3, 3, 3, 4, 5, 4, 2, 3, 4, 3, 3, 2, 4, 3, 3]
healthcare_workers = [3, 4, 5, 4, 6, 5, 6, 7, 5, 6, 4, 5, 4, 6, 5, 5, 7, 4, 5, 4]
writers = [1, 2, 2, 3, 3, 1, 2, 2, 3, 3, 1, 2, 3, 1, 2, 3, 3, 2, 1, 2]
artists = [0, 1, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 1, 2, 0, 1, 2, 1, 0]

# Combine data into a list for the box plot
data = [software_engineers, teachers, healthcare_workers, writers, artists]

# Define labels for each profession
profession_labels = ['Software Engineers', 'Teachers', 'Healthcare Workers', 'Writers', 'Artists']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Creating the box plot
boxplot = ax.boxplot(data, vert=True, patch_artist=True, notch=True, widths=0.6)

# Customize the box plot colors
colors = ['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'khaki']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot
ax.set_title('Coffee Consumption Patterns Across Professions', fontsize=14, pad=20)
ax.set_xlabel('Profession', fontsize=12)
ax.set_ylabel('Coffee Cups per Day', fontsize=12)

# Customize x-axis with profession labels
ax.set_xticklabels(profession_labels, rotation=30, fontsize=10, ha='right')

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()