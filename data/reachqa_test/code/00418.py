import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
platforms = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'TikTok',
             'WeChat', 'QQ', 'Douyin', 'Sina Weibo', 'Telegram',
             'Snapchat', 'LinkedIn', 'Pinterest', 'Twitter']
users_millions = [2900, 2500, 2000, 1400, 1200, 1100, 590, 520, 516, 500, 450, 350, 300, 290]

# Generate a color map, where color represents the region
colors = plt.cm.Set3(np.linspace(0, 1, len(platforms)))

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(16, 9))

# Plot the horizontal bar chart with log scale on x-axis
ax.set_xscale('log')
bars = ax.barh(platforms, users_millions, color=colors)

# Add data labels with proportions and absolute values
total_users = sum(users_millions)
for bar, users in zip(bars, users_millions):
    width = bar.get_width()
    ax.text(width + 10, bar.get_y() + bar.get_height() / 2,
            f'{users}M ({users/total_users:.1%})', va='center', fontweight='bold')

# Set plot title, split it into multiple lines if needed, and adjust padding
ax.set_title('The Art\nof Influence:\n\nA Deep Dive into Social Media Platforms\' Global Impact', fontsize=16, pad=30)

# Set labels
ax.set_xlabel('Monthly Active Users (in Millions)', fontsize=14)
ax.set_ylabel('Social Media Platforms', fontsize=14)

# Adjust y-axis labels to be centered on each bar
ax.set_yticks(np.arange(len(platforms)))
ax.set_yticklabels(platforms)

# Rotate y-axis labels for better visibility
plt.yticks(rotation=0)

# Adjust x-axis limits and major locator
ax.set_xlim(0, max(users_millions) * 1.1)
ax.xaxis.set_major_locator(plt.MultipleLocator(500))

# Highlight the largest platforms by making their bars slightly thicker
largest_platforms = ['Facebook', 'YouTube', 'WhatsApp']
for bar, platform in zip(bars, platforms):
    if platform in largest_platforms:
        bar.set_width(bar.get_width() * 1.05)
        bar.set_height(bar.get_height() * 1.05)

# Add a grid for better readability
ax.grid(True, which='major', axis='x', linestyle='--', linewidth='0.5', color='gray')

# Use tight_layout to prevent cropping any part of the plot
plt.tight_layout()

# Show the plot
plt.show()