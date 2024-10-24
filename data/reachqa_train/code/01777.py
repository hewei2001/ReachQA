import numpy as np
import matplotlib.pyplot as plt

# Define continents and candy types
continents = ['North America', 'South America', 'Europe', 'Asia', 'Africa']
candy_types = ['Chocolate', 'Gummies', 'Lollipops', 'Caramel']

# Candy consumption data in tons
candy_data = np.array([
    [500, 300, 200, 150],  # North America
    [200, 250, 100, 50],   # South America
    [450, 350, 300, 200],  # Europe
    [300, 400, 250, 100],  # Asia
    [150, 200, 100, 50]    # Africa
])

# Normalize candy consumption data for percentage
total_consumption = np.sum(candy_data, axis=1)
normalized_data = (candy_data.T / total_consumption).T * 100

# Create a figure and add subplots
fig = plt.figure(figsize=(14, 7))

# Subplot 1: 3D Bar Chart
ax1 = fig.add_subplot(121, projection='3d')

# Positions and dimensions
x_positions = np.arange(len(continents))
y_positions = np.arange(len(candy_types))
x, y = np.meshgrid(x_positions, y_positions, indexing="ij")
x_flat = x.flatten()
y_flat = y.flatten()
dx = dy = 0.3

# Colors for candy types
colors = ['#8B4513', '#FF4500', '#FFD700', '#DAA520']

# Plot 3D bars
z_offset = np.zeros(len(continents))
for i in range(len(candy_types)):
    z_values = candy_data[:, i]
    ax1.bar3d(x_positions, y_flat[y_flat == i], z_offset, dx, dy, z_values, color=colors[i], alpha=0.8)
    z_offset += z_values

# Titles and labels
ax1.set_title("World's Sweet Tooth:\nCandy Consumption Across Continents", fontsize=14, fontweight='bold', pad=30)
ax1.set_xlabel('Continents', fontsize=10)
ax1.set_ylabel('Candy Types', fontsize=10)
ax1.set_zlabel('Consumption (Tons)', fontsize=10)

# Ticks and legends
ax1.set_xticks(x_positions + dx / 2)
ax1.set_xticklabels(continents, rotation=25, ha='right', fontsize=8)
ax1.set_yticks(y_positions + dy / 2)
ax1.set_yticklabels(candy_types, fontsize=8)
proxy_artists = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
ax1.legend(proxy_artists, candy_types, title="Candy Types", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=8)
ax1.view_init(elev=30, azim=120)

# Subplot 2: Radar Chart
def radar_factory(num_vars, frame='circle'):
    """ Create a radar chart with `num_vars` axes. """
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    return fig, ax, angles

_, ax2, angles = radar_factory(len(continents))

# Radar Chart Data
for i, candy in enumerate(candy_types):
    values = normalized_data[:, i].tolist()
    values += values[:1]  # Repeat first value to close the radar chart
    ax2.plot(angles, values, label=candy, color=colors[i])
    ax2.fill(angles, values, alpha=0.25, color=colors[i])

# Radar Chart customization
ax2.set_title("Proportional Candy Consumption by Continent", fontsize=14, fontweight='bold', pad=20)
ax2.set_yticklabels([])
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(continents, fontsize=10)
ax2.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=8)

# Adjust layout and display
plt.tight_layout()
plt.show()