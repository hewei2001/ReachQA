import matplotlib.pyplot as plt
import numpy as np

# Original data for the bar chart
years = np.array([2020, 2021, 2022, 2023])
video_conferencing = np.array([50, 65, 75, 80])
cloud_storage = np.array([30, 45, 55, 70])
cybersecurity = np.array([20, 35, 50, 60])
collaboration_tools = np.array([15, 25, 40, 55])

# Calculate year-over-year growth rates
video_conferencing_growth = np.diff(video_conferencing, prepend=video_conferencing[0]) / video_conferencing * 100
cloud_storage_growth = np.diff(cloud_storage, prepend=cloud_storage[0]) / cloud_storage * 100
cybersecurity_growth = np.diff(cybersecurity, prepend=cybersecurity[0]) / cybersecurity * 100
collaboration_tools_growth = np.diff(collaboration_tools, prepend=collaboration_tools[0]) / collaboration_tools * 100

# Define the bar width and position offsets for the bar chart
bar_width = 0.2
positions = np.arange(len(years))

# Create figure and multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot - Bar chart
ax1.bar(positions, video_conferencing, width=bar_width, color='dodgerblue', edgecolor='grey', label='Video Conferencing')
ax1.bar(positions + bar_width, cloud_storage, width=bar_width, color='forestgreen', edgecolor='grey', label='Cloud Storage')
ax1.bar(positions + 2 * bar_width, cybersecurity, width=bar_width, color='crimson', edgecolor='grey', label='Cybersecurity')
ax1.bar(positions + 3 * bar_width, collaboration_tools, width=bar_width, color='darkorange', edgecolor='grey', label='Collaboration Tools')

# Data labels
for i in range(len(years)):
    ax1.text(i, video_conferencing[i] + 2, f'{video_conferencing[i]}%', ha='center', va='bottom', color='black', fontsize=10)
    ax1.text(i + bar_width, cloud_storage[i] + 2, f'{cloud_storage[i]}%', ha='center', va='bottom', color='black', fontsize=10)
    ax1.text(i + 2 * bar_width, cybersecurity[i] + 2, f'{cybersecurity[i]}%', ha='center', va='bottom', color='black', fontsize=10)
    ax1.text(i + 3 * bar_width, collaboration_tools[i] + 2, f'{collaboration_tools[i]}%', ha='center', va='bottom', color='black', fontsize=10)

# First subplot settings
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Usage Increase (%)', fontsize=12, fontweight='bold')
ax1.set_title('Growth of Remote Work Technologies\nPost-2020', fontsize=16, fontweight='bold', pad=10)
ax1.set_xticks(positions + 1.5 * bar_width)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=10, title='Technology Type')
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Second subplot - Line chart
ax2.plot(years, video_conferencing_growth, marker='o', color='dodgerblue', label='Video Conferencing')
ax2.plot(years, cloud_storage_growth, marker='o', color='forestgreen', label='Cloud Storage')
ax2.plot(years, cybersecurity_growth, marker='o', color='crimson', label='Cybersecurity')
ax2.plot(years, collaboration_tools_growth, marker='o', color='darkorange', label='Collaboration Tools')

# Data points annotation
for i, txt in enumerate(video_conferencing_growth):
    ax2.annotate(f'{txt:.1f}%', (years[i], video_conferencing_growth[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(cloud_storage_growth):
    ax2.annotate(f'{txt:.1f}%', (years[i], cloud_storage_growth[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(cybersecurity_growth):
    ax2.annotate(f'{txt:.1f}%', (years[i], cybersecurity_growth[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(collaboration_tools_growth):
    ax2.annotate(f'{txt:.1f}%', (years[i], collaboration_tools_growth[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Second subplot settings
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')
ax2.set_title('Annual Growth Rate of Remote Work Technologies', fontsize=16, fontweight='bold', pad=10)
ax2.legend(loc='upper left', fontsize=10, title='Technology Type')
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()