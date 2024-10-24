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

# Calculate growth rates between decades
growth_email = np.diff(email_usage)
growth_instant_messaging = np.diff(instant_messaging_usage)
growth_social_media = np.diff(social_media_usage)
growth_video_conferencing = np.diff(video_conferencing_usage)
growth_collaborative_workspaces = np.diff(collaborative_workspaces_usage)

# Stack the usage data for the area plot
usage_data = np.vstack([
    email_usage, instant_messaging_usage, social_media_usage,
    video_conferencing_usage, collaborative_workspaces_usage
])

# Colors for each communication platform
colors = ['#e63946', '#f1a208', '#4a4e69', '#9a8c98', '#c9ada7']

# Create subplots: 1 stacked area plot and 1 grouped bar plot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Stacked area plot
ax1.stackplot(decades, usage_data, labels=[
    'Email', 'Instant Messaging', 'Social Media',
    'Video Conferencing', 'Collaborative Workspaces'], colors=colors, alpha=0.85)
ax1.set_title('Evolution of Digital Communication Platforms\nOver the Decades', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Percentage of Total Usage', fontsize=12)
ax1.set_xlim(decades[0], decades[-1])
ax1.set_ylim(0, 100)
ax1.set_yticks(range(0, 101, 10))
ax1.legend(loc='upper left', bbox_to_anchor=(1.01, 1), title='Platforms', fontsize=10, title_fontsize='12', frameon=False)

# Grouped bar chart for growth rates
width = 2
decades_mid = decades[:-1] + np.diff(decades) / 2  # mid points for bars

ax2.bar(decades_mid - width*1.5, growth_email, width, color=colors[0], label='Email')
ax2.bar(decades_mid - width/2, growth_instant_messaging, width, color=colors[1], label='Instant Messaging')
ax2.bar(decades_mid + width/2, growth_social_media, width, color=colors[2], label='Social Media')
ax2.bar(decades_mid + width*1.5, growth_video_conferencing, width, color=colors[3], label='Video Conferencing')
ax2.bar(decades_mid + width*2.5, growth_collaborative_workspaces, width, color=colors[4], label='Collaborative Workspaces')

ax2.set_title('Growth Rate of Usage by Platform\nBetween Decades', fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Decade', fontsize=12)
ax2.set_ylabel('Growth Rate in Usage (%)', fontsize=12)
ax2.set_xticks(decades_mid)
ax2.set_xticklabels([f'{decades[i]}-{decades[i+1]}' for i in range(len(decades) - 1)])

# Enhance layout for readability and avoid occlusion
plt.tight_layout(rect=[0, 0, 0.95, 1])
plt.show()