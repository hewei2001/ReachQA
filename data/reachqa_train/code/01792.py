import matplotlib.pyplot as plt

# Data representing the attendance numbers at concerts throughout the year
genres = ['Pop', 'Rock', 'Jazz', 'Classical', 'Electronic']
attendance_data = {
    'Pop': [450, 560, 480, 620, 570, 540, 690, 660, 610, 590, 620, 670],
    'Rock': [510, 600, 580, 710, 750, 680, 720, 800, 770, 810, 760, 840],
    'Jazz': [320, 340, 310, 300, 280, 290, 330, 350, 370, 360, 340, 355],
    'Classical': [270, 290, 250, 260, 240, 230, 275, 285, 295, 305, 280, 290],
    'Electronic': [550, 530, 620, 610, 600, 570, 640, 690, 680, 720, 700, 710]
}

# Organize data into a list of lists
data = [attendance_data[genre] for genre in genres]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the box plot
box = ax.boxplot(data, patch_artist=True, notch=False, vert=True,
                 boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                 whiskerprops=dict(color='darkgreen'),
                 capprops=dict(color='darkgreen'),
                 medianprops=dict(color='red'),
                 flierprops=dict(markerfacecolor='gold', marker='o', markersize=6, alpha=0.6))

# Title and labels
ax.set_title('Concert Attendance Trends by Genre\nin Soundville', fontsize=14, fontweight='bold')
ax.set_xlabel('Music Genre', fontsize=12)
ax.set_ylabel('Number of Attendees', fontsize=12)
ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres, fontsize=11)

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Adding a legend
handles = [plt.Line2D([0], [0], color='red', lw=2, label='Median'),
           plt.Line2D([0], [0], marker='o', color='w', label='Outliers',
                      markerfacecolor='gold', markersize=6, alpha=0.6)]
ax.legend(handles=handles, loc='upper left', fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()