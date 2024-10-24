import matplotlib.pyplot as plt
import numpy as np

# Frequency data of meteor showers observed by ancient civilizations
data = [
    [5, 8, 12, 15, 6],   # Mesopotamia
    [10, 12, 15, 20, 25],  # Ancient Egypt
    [18, 22, 25, 30, 35],  # Mayan Civilization
    [8, 12, 14, 16, 17],   # Ancient Greece
    [20, 25, 30, 35, 40]   # Ancient China
]

# Creating the vertical box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Boxplot with customization for better visual distinction
ax.boxplot(data, 
           patch_artist=True, notch=True,
           boxprops=dict(facecolor="lightblue", color="darkblue"),
           capprops=dict(color="black"),
           whiskerprops=dict(color="darkgray", linestyle='-'),
           flierprops=dict(markeredgecolor="red", marker='o', markersize=8),
           medianprops=dict(color="gold"))

# Title and labels
ax.set_title('Ancient Meteor Showers\nFrequency Observations Across Civilizations', fontsize=14, fontweight='bold')
ax.set_ylabel('Recorded Frequency of Showers', fontsize=12)
ax.set_xticklabels(['Mesopotamia', 'Ancient Egypt', 'Maya', 'Greece', 'China'], fontsize=10)

# Add grid and set the background color
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#eaeaf2')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()