import matplotlib.pyplot as plt
import numpy as np

# Original Data: Hours spent on Social Media (x-axis) and Productivity Levels (y-axis)
hours_on_social_media = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
productivity_levels = np.array([90, 85, 80, 75, 70, 65, 60, 58, 55, 50, 48, 45, 43, 40, 38])

# New Data for Additional Plot: Weekly Average Productivity for different social media usage groups
usage_categories = ['Low', 'Medium', 'High']
weekly_avg_productivity = [80, 65, 45]  # Hypothetical weekly averages

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Scatter plot with a trendline
ax[0].scatter(hours_on_social_media, productivity_levels, color='dodgerblue', edgecolor='black', s=100, alpha=0.7, label='Students')

# Adding trendline
z = np.polyfit(hours_on_social_media, productivity_levels, 1)
p = np.poly1d(z)
ax[0].plot(hours_on_social_media, p(hours_on_social_media), "r--", lw=2, label='Trendline')

# Customizing the first plot
ax[0].set_title('Impact of Social Media Usage on\nStudent Productivity Levels', fontsize=14, fontweight='bold', color='navy')
ax[0].set_xlabel('Avg Hours on Social Media per Day', fontsize=10, fontweight='bold')
ax[0].set_ylabel('Productivity Levels (0-100)', fontsize=10, fontweight='bold')
ax[0].grid(True, linestyle='--', alpha=0.6)

# Annotation
for i, txt in enumerate(productivity_levels):
    ax[0].annotate(txt, (hours_on_social_media[i], productivity_levels[i]), 
                   textcoords="offset points", xytext=(5,5), ha='center', fontsize=8, color='navy')

# Highlight particular data points
highlight_points = [(5, 70), (10, 50)]
for point in highlight_points:
    ax[0].scatter(point[0], point[1], color='red', edgecolor='black', s=150)

# Legend for the first plot
ax[0].legend(loc='upper right', fontsize=9)

# Second subplot: Bar chart
ax[1].bar(usage_categories, weekly_avg_productivity, color=['lightgreen', 'skyblue', 'salmon'], edgecolor='black')

# Customizing the second plot
ax[1].set_title('Weekly Avg Productivity by\nSocial Media Usage Groups', fontsize=14, fontweight='bold', color='darkgreen')
ax[1].set_xlabel('Social Media Usage Category', fontsize=10, fontweight='bold')
ax[1].set_ylabel('Weekly Avg Productivity Level', fontsize=10, fontweight='bold')
ax[1].grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()