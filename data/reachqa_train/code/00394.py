import matplotlib.pyplot as plt
import numpy as np

# Decades for x-axis
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Percentage of usage by platforms over time (fictional data)
email_usage = np.array([80, 70, 55, 40, 30])
instant_messaging_usage = np.array([10, 20, 25, 30, 25])
social_media_usage = np.array([0, 5, 15, 25, 30])
video_conferencing_usage = np.array([5, 3, 5, 15, 20])
collaborative_workspaces_usage = np.array([5, 2, 0, 5, 15])

# Stack the usage data
usage_data = np.vstack([email_usage, instant_messaging_usage, social_media_usage, video_conferencing_usage, collaborative_workspaces_usage])

# Define colors for each communication platform
colors = ['#e63946', '#f1a208', '#4a4e69', '#9a8c98', '#c9ada7']

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(decades, usage_data, labels=[
    'Email', 'Instant Messaging', 'Social Media',
    'Video Conferencing', 'Collaborative Workspaces'], colors=colors, alpha=0.85)

# Customize the chart
ax.set_title('Evolution of Digital Communication Platforms\nOver the Decades', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage of Total Usage', fontsize=12)
ax.set_xlim(decades[0], decades[-1])
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))

# Add a legend outside the main plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Platforms', fontsize=10, title_fontsize='12', frameon=False)

# Enhance layout for readability and avoid occlusion
plt.xticks(decades)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to fit legend

# Show the plot
plt.show()