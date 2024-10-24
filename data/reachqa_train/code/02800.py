import matplotlib.pyplot as plt
import numpy as np

# Define cities and the number of AI-driven food delivery robots deployed in each city for 2030
cities = ['Tokyo', 'New York', 'London', 'Shanghai', 'Berlin', 'Sydney', 'Mumbai']
robots_deployed = [1200, 950, 850, 1100, 700, 600, 750]

# Define bar positions and width
x_positions = np.arange(len(cities))
bar_width = 0.6

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bars with distinct colors for each city
colors = ['#FFB6C1', '#87CEFA', '#FFD700', '#8A2BE2', '#7FFF00', '#FF4500', '#00CED1']
bars = ax.bar(x_positions, robots_deployed, color=colors, width=bar_width)

# Annotate each bar with the number of robots
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 25, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the x-axis
ax.set_xticks(x_positions)
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=11)

# Set the title and labels
ax.set_title("Deployment of AI-driven Food Delivery Robots in 2030\nAcross Major Global Cities", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Number of Robots Deployed", fontsize=12)

# Add grid lines for the y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to fit all elements
plt.tight_layout()

# Show the plot
plt.show()