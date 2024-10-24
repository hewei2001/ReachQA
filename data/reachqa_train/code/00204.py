import matplotlib.pyplot as plt
import numpy as np

# Define the countries and renewable energy sources
countries = ['Germany', 'China', 'USA', 'India', 'Brazil']
sources = ['Solar', 'Wind', 'Hydro']

# Percentage contribution data for each source in each country
data = np.array([
    [20, 30, 15],  # Germany
    [15, 25, 20],  # China
    [10, 25, 10],  # USA
    [25, 15, 10],  # India
    [5, 10, 45]    # Brazil
])

# Create a figure and a 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the x and y positions for the bars
xpos = np.arange(len(countries))
ypos = np.arange(len(sources))
xposM, yposM = np.meshgrid(xpos, ypos, indexing="ij")

# Flatten the position arrays
xposM = xposM.flatten()
yposM = yposM.flatten()
zpos = np.zeros_like(xposM)

# Set the dimensions of the bars
dx = dy = 0.6
dz = data.flatten()

# Define colors for each renewable source
colors = ['#FFD700', '#1E90FF', '#32CD32']  # Solar (Gold), Wind (Dodger Blue), Hydro (Lime Green)

# Create the bars
ax.bar3d(xposM, yposM, zpos, dx, dy, dz, color=np.repeat(colors, len(countries)), alpha=0.7)

# Labeling the axes
ax.set_xlabel('Countries', fontsize=10)
ax.set_ylabel('Energy Source', fontsize=10)
ax.set_zlabel('Percentage (%)', fontsize=10)
ax.set_zlim(0, 50)

# Set ticks and labels for countries and sources
ax.set_xticks(xpos + dx / 2)
ax.set_xticklabels(countries, rotation=45, ha='right', fontsize=9)
ax.set_yticks(ypos + dy / 2)
ax.set_yticklabels(sources, fontsize=9)

# Adjust view angle for better visualization
ax.view_init(elev=20., azim=120)

# Add a title with line breaks for better visibility
ax.set_title('Renewable Energy Adoption\nAcross Leading Countries', fontsize=14, weight='bold', pad=30)

# Create a legend
legend_patches = [
    plt.Line2D([0], [0], color=colors[0], lw=4, label='Solar'),
    plt.Line2D([0], [0], color=colors[1], lw=4, label='Wind'),
    plt.Line2D([0], [0], color=colors[2], lw=4, label='Hydro')
]
ax.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1.05, 1), title='Energy Sources')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()