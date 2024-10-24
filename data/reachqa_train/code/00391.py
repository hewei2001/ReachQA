import matplotlib.pyplot as plt
import numpy as np

# Data setup: meditation session durations (in minutes) for different age groups across decades
# Each list represents durations for a specific age group in a specific decade
data_1980s = {
    '18-30': [15, 20, 22, 25, 30, 35, 40, 18, 23],
    '31-50': [20, 25, 27, 35, 40, 45, 50, 30, 32],
    '51+': [30, 35, 40, 45, 50, 55, 60, 45, 50]
}

data_2000s = {
    '18-30': [20, 25, 28, 30, 35, 40, 45, 26, 29],
    '31-50': [25, 30, 32, 40, 45, 50, 55, 35, 38],
    '51+': [35, 40, 45, 50, 55, 60, 65, 55, 60]
}

data_2020s = {
    '18-30': [25, 30, 35, 40, 45, 50, 55, 35, 38],
    '31-50': [30, 35, 40, 50, 55, 60, 65, 45, 48],
    '51+': [40, 45, 50, 60, 65, 70, 75, 65, 70]
}

# Combine data into lists for the boxplot
data = [
    data_1980s['18-30'], data_1980s['31-50'], data_1980s['51+'],
    data_2000s['18-30'], data_2000s['31-50'], data_2000s['51+'],
    data_2020s['18-30'], data_2020s['31-50'], data_2020s['51+'],
]

# Labels for each box plot
labels = [
    '18-30 (1980s)', '31-50 (1980s)', '51+ (1980s)',
    '18-30 (2000s)', '31-50 (2000s)', '51+ (2000s)',
    '18-30 (2020s)', '31-50 (2020s)', '51+ (2020s)'
]

# Create the box plot
fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(data, patch_artist=True, vert=True, notch=True,
                 boxprops=dict(facecolor='#b2df8a', color='#33a02c'),
                 whiskerprops=dict(color='#33a02c'),
                 capprops=dict(color='#33a02c'),
                 medianprops=dict(color='#e31a1c'))

# Customize colors for the boxes
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add customizations
ax.set_title('The Evolution of Mindfulness:\nMeditation Practices Across the Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Age Group and Decade', fontsize=12)
ax.set_ylabel('Meditation Duration (minutes)', fontsize=12)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()