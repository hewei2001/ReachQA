import matplotlib.pyplot as plt
import numpy as np

# Years from 2005 to 2025
years = np.arange(2005, 2026)

# Percentage adoption data for each technology
e_learning_platforms = [
    10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 86
]
virtual_classrooms = [
    5, 6, 8, 10, 12, 15, 18, 20, 25, 28, 32, 35, 38, 40, 42, 45, 50, 52, 54, 55, 57
]
digital_textbooks = [
    8, 9, 11, 14, 18, 20, 25, 30, 35, 40, 43, 45, 48, 50, 52, 55, 58, 60, 62, 64, 66
]
educational_apps = [
    2, 3, 5, 7, 9, 11, 15, 18, 22, 27, 30, 35, 40, 43, 47, 50, 53, 55, 58, 60, 63
]

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each stacked bar
ax.bar(years, e_learning_platforms, label='E-Learning Platforms', color='#ff9999', alpha=0.8)
ax.bar(years, virtual_classrooms, bottom=e_learning_platforms, label='Virtual Classrooms', color='#66b3ff', alpha=0.8)
bottom_base = np.array(e_learning_platforms) + np.array(virtual_classrooms)
ax.bar(years, digital_textbooks, bottom=bottom_base, label='Digital Textbooks', color='#99ff99', alpha=0.8)
combined_base = bottom_base + np.array(digital_textbooks)
ax.bar(years, educational_apps, bottom=combined_base, label='Educational Apps', color='#ffcc99', alpha=0.8)

# Title and labels
ax.set_title('Digital Transformation of Education (2005-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage Adoption (%)', fontsize=14)

# X-axis configuration
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

# Add grid lines and legend
ax.grid(alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=12, title='Digital Tools')

# Use tight layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()