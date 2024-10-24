import matplotlib.pyplot as plt
import numpy as np

# Years of the biennales
years = np.array([2021, 2023, 2025])

# Attendance data (in thousands) for each continent
continents = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Australia']
attendance_data = {
    'Europe': np.array([420, 450, 480]),
    'Asia': np.array([390, 420, 460]),
    'North America': np.array([350, 370, 390]),
    'South America': np.array([280, 300, 320]),
    'Africa': np.array([210, 230, 250]),
    'Australia': np.array([150, 170, 190])
}

# Define color scheme for each continent
colors = {
    'Europe': 'royalblue',
    'Asia': 'seagreen',
    'North America': 'darkorange',
    'South America': 'firebrick',
    'Africa': 'purple',
    'Australia': 'gold'
}

# Initialize the figure and the 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Bar width and depth
bar_width = 0.2
bar_depth = 0.5

# Adjust Y and X positions for the bars
y_pos = np.arange(len(continents))
x_pos = np.arange(len(years))

# Loop through each continent and plot its data
for idx, (continent, attendance) in enumerate(attendance_data.items()):
    ax.bar3d(x_pos - bar_width/2, y_pos[idx] - bar_depth/2, np.zeros_like(attendance), 
             bar_width, bar_depth, attendance, color=colors[continent], alpha=0.8, 
             zsort='average', label=continent)

# Set the labels and title
ax.set_xlabel('Years', fontsize=12, labelpad=10)
ax.set_ylabel('Continents', fontsize=12, labelpad=10)
ax.set_zlabel('Attendance (Thousands)', fontsize=12, labelpad=10)
ax.set_title("Art Biennale Attendance Across Continents\n(2021-2025)", fontsize=16, pad=20)

# Set ticks and tick labels
ax.set_xticks(x_pos)
ax.set_xticklabels(years)
ax.set_yticks(y_pos)
ax.set_yticklabels(continents)

# Rotate y-tick labels to improve readability
plt.xticks(rotation=45)
plt.yticks(rotation=30)

# Add legend
ax.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.15, 1.0))

# Adjust the view angle for better visualization
ax.view_init(elev=30, azim=30)

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Show the plot
plt.show()