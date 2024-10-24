import matplotlib.pyplot as plt
import numpy as np

# Extended years of data
years = np.arange(2010, 2024)

# Constructing engagement hours for various platforms over extended years
video_streaming = np.array([5, 7, 9, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
social_networking = np.array([3, 4, 6, 7, 9, 10, 11, 12, 13, 15, 17, 18, 20, 22])
online_news = np.array([2, 3, 4, 6, 7, 9, 10, 12, 14, 15, 17, 16, 14, 12])
podcasts = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
gaming = np.array([2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20])
e_books = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8])
web_browsing = np.array([4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 19])

# Prepare data for stacked area chart
platforms = [video_streaming, social_networking, online_news, podcasts, gaming, e_books, web_browsing]
platform_labels = ['Video Streaming', 'Social Networking', 'Online News', 'Podcasts', 'Gaming', 'E-books', 'Web Browsing']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Create plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area plot
ax.stackplot(years, *platforms, labels=platform_labels, colors=colors, alpha=0.8)

# Customizing the chart
ax.set_title('Trends in Digital Content Consumption (2010-2023)\nAnalyzing the Shift in User Engagement Across Platforms', 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Engagement Hours', fontsize=12)

# Set x-ticks with a proper step and rotation
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, rotation=45)

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Platforms', fontsize=10)

# Enhance plot aesthetics
ax.grid(alpha=0.3)
plt.tight_layout()

# Display the plot
plt.show()