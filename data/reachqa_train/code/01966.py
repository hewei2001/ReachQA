import matplotlib.pyplot as plt
import numpy as np

# Define the data for the bar chart
years = np.array([2020, 2021, 2022, 2023])
video_conferencing = np.array([50, 65, 75, 80])
cloud_storage = np.array([30, 45, 55, 70])
cybersecurity = np.array([20, 35, 50, 60])
collaboration_tools = np.array([15, 25, 40, 55])

# Define the bar width and position offsets
bar_width = 0.2
positions = np.arange(len(years))

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each technology's data
ax.bar(positions, video_conferencing, width=bar_width, color='dodgerblue', edgecolor='grey', label='Video Conferencing')
ax.bar(positions + bar_width, cloud_storage, width=bar_width, color='forestgreen', edgecolor='grey', label='Cloud Storage')
ax.bar(positions + 2 * bar_width, cybersecurity, width=bar_width, color='crimson', edgecolor='grey', label='Cybersecurity')
ax.bar(positions + 3 * bar_width, collaboration_tools, width=bar_width, color='darkorange', edgecolor='grey', label='Collaboration Tools')

# Add data labels on top of each bar
for i in range(len(years)):
    ax.text(i, video_conferencing[i] + 2, f'{video_conferencing[i]}%', ha='center', va='bottom', color='black', fontsize=10)
    ax.text(i + bar_width, cloud_storage[i] + 2, f'{cloud_storage[i]}%', ha='center', va='bottom', color='black', fontsize=10)
    ax.text(i + 2 * bar_width, cybersecurity[i] + 2, f'{cybersecurity[i]}%', ha='center', va='bottom', color='black', fontsize=10)
    ax.text(i + 3 * bar_width, collaboration_tools[i] + 2, f'{collaboration_tools[i]}%', ha='center', va='bottom', color='black', fontsize=10)

# Set labels and title
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Usage Increase (%)', fontsize=12, fontweight='bold')
ax.set_title('Growth of Remote Work Technologies\nPost-2020', fontsize=16, fontweight='bold', pad=20)

# Set x-ticks to display the years
ax.set_xticks(positions + 1.5 * bar_width)
ax.set_xticklabels(years)

# Add a legend to differentiate between technologies
ax.legend(loc='upper left', fontsize=10, title='Technology Type')

# Add grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()