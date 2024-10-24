import matplotlib.pyplot as plt
import numpy as np

# Define the art movements and years
art_movements = ['Impressionism', 'Abstract Art', 'Digital Art']
years = np.array([1990, 2000, 2010, 2020])

# Percentage interest data for each art movement and year
interest_data = np.array([
    [30, 25, 20, 15],  # Impressionism
    [20, 30, 35, 25],  # Abstract Art
    [10, 15, 30, 40],  # Digital Art
])

# Prepare the positions for the bars
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar width and colors for each art movement
width = 0.8
colors = ['#FF9999', '#66B3FF', '#99FF99']  # Using distinct colors for clarity

# Plot each art movement's data separately to avoid overlap
for i, movement in enumerate(art_movements):
    xpos = np.arange(len(years))
    ypos = np.full_like(years, i)
    zpos = np.zeros_like(years)
    ax.bar3d(xpos, ypos, zpos, width, width, interest_data[i], color=colors[i], alpha=0.8, label=movement)

# Set axis labels and chart title
ax.set_xlabel('Year')
ax.set_ylabel('Art Movement')
ax.set_zlabel('Interest (%)')
ax.set_title('Evolution of Art Movement Popularity Among University Students\n(1990-2020)', pad=20)

# Customize X-axis and Y-axis labels
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(len(art_movements)))
ax.set_yticklabels(art_movements)

# Normalize Z-axis to a 0-100 scale to reflect percentage values accurately
ax.set_zlim(0, 100)

# Adjust layout to ensure everything fits well
plt.tight_layout()

# Set an optimal viewing angle
ax.view_init(elev=20, azim=60)

# Add a legend to identify the art movements
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1))

plt.show()