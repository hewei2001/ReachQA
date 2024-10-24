import matplotlib.pyplot as plt
import numpy as np

# Define the data for the charts
platforms = ['Social Media', 'Email', 'Messaging Apps', 'Professional Networks', 'Video Calls']
usage_percentages = [35, 25, 20, 10, 10]
average_daily_hours = [2.5, 1.8, 1.5, 1.0, 1.2]

# Define distinct colors for each segment
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#FF8C42', '#008080']

# Create the figure and set up two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# --- First Plot: Donut Chart ---

# Create the pie chart with specified wedge properties to form a ring
wedges, texts, autotexts = ax1.pie(
    usage_percentages,
    labels=platforms,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2)
)

# Draw a center circle to enhance the ring effect
centre_circle = plt.Circle((0, 0), 0.60, fc='white', linewidth=1.5, edgecolor='black')
ax1.add_artist(centre_circle)

# Customize the autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a central title inside the ring
ax1.text(0, 0, 'Global\nUsage 2023', horizontalalignment='center', verticalalignment='center',
         fontsize=14, fontweight='bold', color='black')

# Set a multi-line title for the pie chart
ax1.set_title('Digital Communication Platforms\nUser Engagement Overview 2023', fontsize=16, fontweight='bold', pad=20)

# Ensure the pie chart is circular
ax1.axis('equal')

# --- Second Plot: Bar Chart ---

# Create a bar chart showing average daily hours spent on platforms
ax2.bar(platforms, average_daily_hours, color=colors, edgecolor='black', linewidth=1.5)

# Add labels and title
ax2.set_ylabel('Average Daily Hours', fontsize=12, fontweight='bold')
ax2.set_xlabel('Platforms', fontsize=12, fontweight='bold')
ax2.set_title('Average Daily Usage\nin Hours per Platform', fontsize=16, fontweight='bold', pad=20)

# Annotate the bar chart with the exact values
for i, (platform, hours) in enumerate(zip(platforms, average_daily_hours)):
    ax2.text(i, hours + 0.05, f'{hours} hrs', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Enhance x-tick label visibility
ax2.set_xticklabels(platforms, rotation=45, ha='right', fontsize=10, fontweight='bold')

# Improve layout to prevent any overlap
plt.tight_layout()

# Display the plot
plt.show()