import matplotlib.pyplot as plt
import numpy as np

# Define sectors and programming languages
sectors = ['Web Dev', 'Data Sci', 'Game Dev', 'Mobile Apps']
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Swift']

# Define the percentage distribution of programming languages in each sector
data = np.array([
    [25, 50, 10, 10, 5],    # Web Development
    [60, 10, 10, 10, 10],   # Data Science
    [15, 5, 25, 40, 15],    # Game Development
    [10, 5, 20, 15, 50]     # Mobile Apps
])

# Define bar position and dimensions
num_languages = data.shape[1]
num_sectors = data.shape[0]
x_pos = np.arange(num_languages)
y_pos = np.arange(num_sectors)
x_pos, y_pos = np.meshgrid(x_pos, y_pos)

# Create figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Normalize color mapping
colors = plt.cm.viridis(np.linspace(0, 1, num_sectors))

# Plot each sector's data as 3D bars
for y_index, (sector, color) in enumerate(zip(sectors, colors)):
    ax.bar3d(
        x_pos[y_index], y_pos[y_index], np.zeros(num_languages),
        dx=0.8, dy=0.8, dz=data[y_index],
        color=color, alpha=0.7, label=sector
    )

# Configure axes
ax.set_xlabel('Programming Languages', labelpad=10)
ax.set_ylabel('Sectors', labelpad=10)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_xticks(np.arange(len(languages)))
ax.set_xticklabels(languages, rotation=45, ha='right')
ax.set_yticks(y_pos[:,0])
ax.set_yticklabels(sectors)
ax.set_zlim(0, 100)
ax.view_init(elev=25, azim=135)  # Adjusting view for better visibility

# Add title and legend
ax.set_title('Programming Language Adoption in Tech Sectors\n(Percentage of Companies)', fontsize=14, fontweight='bold', pad=20)
ax.legend(title="Sectors", loc='upper right', bbox_to_anchor=(1.1, 1.0))

# Adjust layout for better spacing
plt.tight_layout()

# Display plot
plt.show()