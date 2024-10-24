import matplotlib.pyplot as plt
import numpy as np

# Data setup
platforms = ['Facebook', 'Instagram', 'Twitter', 'Snapchat', 'TikTok']
market_shares = [25, 20, 15, 10, 30]  # Percentage values summing to 100%

# Define colors for each platform
colors = ['#3b5998', '#e4405f', '#1da1f2', '#fffc00', '#69c9d0']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bar_container = ax.barh(platforms, market_shares, color=colors, edgecolor='black')

# Add title and labels with clear font size and weight
ax.set_title('2023 Social Media Platform Market Share', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Market Share (%)', fontsize=12)
ax.set_ylabel('Platforms', fontsize=12)

# Label each bar with the percentage value
ax.bar_label(bar_container, fmt='%.0f%%', padding=3, fontsize=11)

# Set the range of x-axis from 0 to 100 to reflect percentage scale
ax.set_xlim(0, 100)

# Improve layout to prevent text overlap and ensure clarity
plt.tight_layout()

# Display the chart
plt.show()