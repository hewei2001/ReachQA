import matplotlib.pyplot as plt
import numpy as np

# Years of data
years = np.array([2018, 2019, 2020, 2021, 2022])

# Engagement hours (average monthly hours per user)
video_streaming = np.array([20, 23, 29, 35, 40])
social_networking = np.array([18, 19, 21, 22, 25])
online_news = np.array([12, 13, 15, 17, 16])
podcasts = np.array([5, 7, 10, 12, 15])
gaming = np.array([8, 9, 10, 14, 18])

# Prepare data for stacked area chart
platforms = [video_streaming, social_networking, online_news, podcasts, gaming]
platform_labels = ['Video Streaming', 'Social Networking', 'Online News', 'Podcasts', 'Gaming']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create plot
plt.figure(figsize=(12, 7))

# Stacked area plot
plt.stackplot(years, *platforms, labels=platform_labels, colors=colors, alpha=0.8)

# Customizing the chart
plt.title('Trends in Digital Content Consumption (2018-2022)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Monthly Engagement Hours', fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Platforms', fontsize=10)
plt.xticks(years, fontsize=10)

# Enhance plot aesthetics
plt.grid(alpha=0.3)
plt.tight_layout()

# Display the plot
plt.show()