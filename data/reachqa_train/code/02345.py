import numpy as np
import matplotlib.pyplot as plt

# Define the decades for the x-axis
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Fictional data representing the area of green spaces in square kilometers
parks = np.array([150, 180, 210, 250, 300])
urban_forests = np.array([70, 80, 95, 120, 150])
green_roofs = np.array([0, 5, 15, 30, 50])
community_gardens = np.array([5, 10, 20, 40, 70])

# Stack the data
green_space_areas = np.vstack([parks, urban_forests, green_roofs, community_gardens])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(decades, green_space_areas, labels=['Parks', 'Urban Forests', 'Green Roofs', 'Community Gardens'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'], alpha=0.8)

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Area of Green Spaces (sq km)', fontsize=12)
ax.set_title('Evolution of Urban Green Spaces\nAcross Decades', fontsize=16, fontweight='bold', y=1.03)
ax.legend(loc='upper left', fontsize=10, title="Types of Green Spaces", title_fontsize=11)

# Annotate key developments
ax.annotate('Introduction of Green Roofs', xy=(2000, 225), xytext=(1985, 350),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Community Gardens Boom', xy=(2010, 440), xytext=(2015, 550),
            arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='darkgreen')

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels to avoid overlap
plt.xticks(decades, rotation=45)

# Adjust layout for better visibility
plt.tight_layout()

# Show the plot
plt.show()