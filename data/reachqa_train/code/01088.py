import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2030
years = np.arange(2000, 2031)

# Extended and more complex adoption data
e_learning_platforms = [4, 5, 6, 7, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 86, 88, 90, 91, 92, 93]
virtual_classrooms = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20, 25, 28, 32, 35, 38, 40, 42, 45, 50, 52, 54, 55, 57, 58, 59, 60, 60, 61, 62]
digital_textbooks = [3, 4, 5, 6, 7, 9, 11, 14, 18, 20, 25, 30, 35, 40, 43, 45, 48, 50, 52, 55, 58, 60, 62, 64, 66, 67, 68, 69, 70, 70, 71]
educational_apps = [0, 0, 1, 2, 3, 5, 7, 9, 11, 15, 18, 22, 27, 30, 35, 40, 43, 47, 50, 53, 55, 58, 60, 63, 65, 66, 67, 68, 69, 70, 71]
vr_education = [0, 0, 0, 0, 1, 1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 23, 25, 28, 30, 32, 35, 38, 40, 42, 43, 45, 46, 47, 48, 49, 50]

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Plot each stacked bar
ax.bar(years, e_learning_platforms, label='E-Learning Platforms', color='#ff9999', alpha=0.8)
ax.bar(years, virtual_classrooms, bottom=e_learning_platforms, label='Virtual Classrooms', color='#66b3ff', alpha=0.8)
bottom_base = np.array(e_learning_platforms) + np.array(virtual_classrooms)
ax.bar(years, digital_textbooks, bottom=bottom_base, label='Digital Textbooks', color='#99ff99', alpha=0.8)
combined_base = bottom_base + np.array(digital_textbooks)
ax.bar(years, educational_apps, bottom=combined_base, label='Educational Apps', color='#ffcc99', alpha=0.8)
combined_base_2 = combined_base + np.array(educational_apps)
ax.bar(years, vr_education, bottom=combined_base_2, label='VR in Education', color='#c2c2f0', alpha=0.8)

# Title and labels
ax.set_title('Digital Transformation of Education Over Time\n(2000-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage Adoption (%)', fontsize=14)

# X-axis configuration
ax.set_xticks(years[::3])
ax.set_xticklabels(years[::3], rotation=45, ha='right')

# Add grid lines, legend, and annotations
ax.grid(alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=12, title='Digital Tools')
ax.annotate('Rapid Adoption', xy=(2015, 100), xytext=(2012, 120),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, color='black')

# Use tight layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()