import matplotlib.pyplot as plt
import numpy as np

# Updated Data for better variability
genres = ['Rock', 'Pop', 'Hip-Hop', 'Electronic', 'Classical']
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
data = np.array([
    [1200, 850, 600, 450, 250],  # Rock
    [1550, 1100, 750, 550, 400],  # Pop
    [1050, 750, 620, 500, 300],  # Hip-Hop
    [850, 620, 470, 280, 120],   # Electronic
    [420, 270, 180, 70, 30]      # Classical
])

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data with better spacing and color clarity
x_values = np.arange(len(age_groups))
y_values = np.arange(len(genres))
width, depth = 0.4, 0.4  # Narrower bars to reduce occlusion
for i in y_values:
    ax.bar3d(x_values, [i]*len(x_values), np.zeros(len(x_values)), width, depth, data[i], 
             color=plt.cm.get_cmap('tab10')(i / len(genres)), alpha=0.7, edgecolor='black', linewidth=0.5)

# Set axis labels and title
ax.set_xlabel('Age Groups', labelpad=10)
ax.set_ylabel('Music Genres', labelpad=10)
ax.set_zlabel('Number of Attendees', labelpad=10)
ax.set_title("Music Festival Attendance by Genre and Age Group\n"
             "Note: Height of bars represents number of attendees", pad=20)

# Adjust the viewing angle to minimize occlusion
ax.view_init(elev=30, azim=60)

# Set specific names for x and y axes
ax.set_xticks(x_values)
ax.set_xticklabels(age_groups)
ax.set_yticks(y_values)
ax.set_yticklabels(genres)

# Add grid lines with low intensity for better aesthetics
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend for genres
for i, genre in enumerate(genres):
    ax.scatter([], [], [], c=[plt.cm.get_cmap('tab10')(i / len(genres))], label=genre)
ax.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper left', bbox_to_anchor=(1.05, 1))

# Automatically adjust layout to avoid overlaps
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Show plot
plt.show()