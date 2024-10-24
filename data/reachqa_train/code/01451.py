import matplotlib.pyplot as plt
import numpy as np

# Retreat locations
retreats = ['Mars Valley', 'Jupiter Halo', 'Venus Outpost', 'Saturn Rings', 'Neptune Seas']

# Data: intellectual diversity (X-axis), environmental diversity (Y-axis), creative output (Z-axis), number of attendees (bubble size)
intellectual_diversity = np.array([80, 60, 70, 85, 55])  # Measured in diverse intellectual elements
environmental_diversity = np.array([75, 50, 90, 65, 80]) # Measured in varied environmental factors
creative_output = np.array([88, 65, 92, 78, 70])         # Creative output index
attendees = np.array([120, 90, 150, 110, 95])            # Number of attendees for each retreat

# Normalize bubble size for better visualization
bubble_size = attendees / np.max(attendees) * 500

# Create a 3D scatter plot (bubble chart)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the data
scatter = ax.scatter(intellectual_diversity, environmental_diversity, creative_output, 
                     s=bubble_size, c=creative_output, cmap='viridis', alpha=0.8, edgecolors='w')

# Adding labels and titles
ax.set_title('Galactic Writers\' Retreats:\nNavigating the Universe of Creativity', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Intellectual Diversity', fontsize=12, labelpad=10)
ax.set_ylabel('Environmental Diversity', fontsize=12, labelpad=10)
ax.set_zlabel('Creative Output', fontsize=12, labelpad=10)

# Add a color bar to reflect creative output intensity
color_bar = plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.6, aspect=15)
color_bar.set_label('Creative Output Intensity', fontsize=12)

# Annotate each retreat with its name
for i, retreat in enumerate(retreats):
    ax.text(intellectual_diversity[i], environmental_diversity[i], creative_output[i],
            retreat, fontsize=10, ha='right')

# Enhance visual style
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
ax.view_init(elev=30, azim=45)  # Adjust view angle for better visualization

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()