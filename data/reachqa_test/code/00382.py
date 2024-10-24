import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
diameters = np.array([4879, 12104, 12742, 6794, 142984, 116464, 51118, 49528]) / 1000  # Convert to thousands of kilometers
colors = plt.cm.plasma(np.linspace(0, 1, len(planets)))  # Custom color scheme

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the data with a subtle gradient effect
bars = ax.barh(planets, diameters, height=0.8, color=colors)
for i, bar in enumerate(bars):
    ax.barh(planets[i], diameters[i], height=0.8, edgecolor='gray', facecolor=colors[i], linewidth=0.5)

# Highlight Jupiter
ax.barh(planets[4], diameters[4], height=0.8, edgecolor='black', facecolor=colors[4], linewidth=1.5)

# Set title and labels
ax.set_title("Largest Planets in Our Solar System\nby Diameter (Thousands of Kilometers)", fontsize=14)
ax.set_xlabel("Diameter (thousands of kilometers)", fontsize=12)
ax.set_ylabel("Planet", fontsize=12)

# Add value labels on the end of each bar
for i, bar in enumerate(bars):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f"{diameters[i]:.1f}", ha='left', va='center', fontsize=10)

# Adjust y-axis ticks and labels
ax.set_yticks(np.arange(len(planets)))
ax.set_yticklabels(planets, fontsize=10)
ax.tick_params(axis='y', which='major', pad=10)

# Add grid lines and a background color
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.set_facecolor('#F5F5F5')

# Add a note with additional information
ax.annotate("Note: Data from NASA's planetary fact sheets.", xy=(0.05, 0.01), xycoords='figure fraction', fontsize=8)

# Automatically adjust the layout
fig.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()