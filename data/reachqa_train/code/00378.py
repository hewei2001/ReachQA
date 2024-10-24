import matplotlib.pyplot as plt
import numpy as np

# Data: Hours spent on Social Media (x-axis) and Productivity Levels (y-axis)
hours_on_social_media = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
productivity_levels = [90, 85, 80, 75, 70, 65, 60, 58, 55, 50, 48, 45, 43, 40, 38]

# Plotting the scatter chart
plt.figure(figsize=(12, 8))
plt.scatter(hours_on_social_media, productivity_levels, 
            color='dodgerblue', edgecolor='black', s=100, alpha=0.7, label='Students')

# Adding trendline
z = np.polyfit(hours_on_social_media, productivity_levels, 1)
p = np.poly1d(z)
plt.plot(hours_on_social_media, p(hours_on_social_media), "r--", lw=2, label='Trendline')

# Customizing the plot
plt.title('Impact of Social Media Usage on\nStudent Productivity Levels', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('Average Hours on Social Media per Day', fontsize=12, fontweight='bold')
plt.ylabel('Productivity Levels (0-100)', fontsize=12, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)

# Annotation
for i, txt in enumerate(productivity_levels):
    plt.annotate(txt, (hours_on_social_media[i], productivity_levels[i]), 
                 textcoords="offset points", xytext=(5,5), ha='center', fontsize=8, color='navy')

# Highlight particular data points
highlight_points = [(5, 70), (10, 50)]
for point in highlight_points:
    plt.scatter(point[0], point[1], color='red', edgecolor='black', s=150)

# Legend
plt.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()