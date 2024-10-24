import matplotlib.pyplot as plt
import numpy as np

# Define the structure types and cities
structure_types = ['Vertical Gardens', 'Smart Skyscrapers', 'Transport Hubs', 
                   'Energy Towers', 'Floating Neighborhoods']
cities = ['Tokyo', 'New York', 'Shanghai', 'London', 'Dubai']

# Investment data in millions USD
investment_data = np.array([
    [250, 400, 300, 200, 180],  # Tokyo
    [300, 500, 250, 220, 170],  # New York
    [320, 450, 310, 230, 190],  # Shanghai
    [280, 420, 270, 210, 160],  # London
    [350, 480, 330, 240, 200]   # Dubai
])

# Create a 3D bar chart
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Define the position and dimensions of each bar
x_pos, y_pos = np.meshgrid(np.arange(investment_data.shape[1]), np.arange(investment_data.shape[0]))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

dx = dy = 0.6  # Width and depth of the bars
dz = investment_data.flatten()

# Bar colors for different structures
colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728', '#9467bd']

# Plot the bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % len(structure_types)] for i in x_pos], alpha=0.7)

# Customize axes
ax.set_xlabel('Structure Type')
ax.set_ylabel('City')
ax.set_zlabel('Investment (Millions USD)')

# Set ticks and labels with rotation for better readability
ax.set_xticks(np.arange(len(structure_types)))
ax.set_xticklabels(structure_types, rotation=45, ha='right')
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities)

# Adjust view angle for better perspective
ax.view_init(elev=25, azim=135)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Title with line breaks to fit
plt.title("Investment Projections in Futuristic Urban Structures\nAcross Major Cities", 
          pad=20, fontsize=14, weight='bold')

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()