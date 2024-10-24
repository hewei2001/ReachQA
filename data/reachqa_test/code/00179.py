import matplotlib.pyplot as plt
import numpy as np

# Data for monthly downloads of digital art styles in 2023
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Fictional download data for three digital art styles
abstract_downloads = np.array([150, 170, 180, 195, 160, 175, 200, 220, 240, 230, 215, 205])
realism_downloads = np.array([180, 190, 210, 250, 240, 260, 280, 300, 320, 310, 295, 290])
impressionism_downloads = np.array([130, 145, 150, 160, 180, 190, 205, 220, 230, 225, 215, 210])

# Calculate cumulative downloads for the overlay plot
cumulative_downloads = abstract_downloads + realism_downloads + impressionism_downloads

# Initialize the plot with two y-axes
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()  # Create a secondary y-axis

# Plot line charts for the art styles
ax1.plot(months, abstract_downloads, marker='o', linestyle='-', color='b', linewidth=2, label='Abstract')
ax1.plot(months, realism_downloads, marker='s', linestyle='--', color='g', linewidth=2, label='Realism')
ax1.plot(months, impressionism_downloads, marker='^', linestyle=':', color='r', linewidth=2, label='Impressionism')

# Add a bar plot for cumulative downloads as an overlay
ax2.bar(months, cumulative_downloads, alpha=0.3, color='gray', label='Cumulative Downloads')

# Annotate key points in the line plots
ax1.annotate('Peak in April', xy=('Apr', 250), xytext=('Feb', 270),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Summer High', xy=('Aug', 300), xytext=('Jun', 320),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Winter Decline', xy=('Dec', 210), xytext=('Oct', 230),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Annotate cumulative bar heights with values
for i, month in enumerate(months):
    ax2.text(month, cumulative_downloads[i] + 10, f'{cumulative_downloads[i]}', fontsize=8, ha='center', color='black')

# Add labels and titles
ax1.set_title('Digital Artwork Trends in 2023\nMonthly Downloads and Cumulative Counts', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Number of Downloads (Individual Styles)', fontsize=12)
ax2.set_ylabel('Cumulative Downloads', fontsize=12, color='gray')

# Customize grids and ticks
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, fontsize=11)
ax1.set_yticks(np.arange(100, 351, 25))
ax2.set_yticks(np.arange(500, 1101, 100))

# Add legends
ax1.legend(loc='upper left', title='Art Style', fontsize=11)
ax2.legend(loc='upper right', fontsize=11)

# Adjust layout to prevent overlap
fig.tight_layout()

# Show the plot
plt.show()