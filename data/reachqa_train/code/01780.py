import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data for smartphone OS market share
os_labels = ['Android', 'iOS', 'HarmonyOS', 'Others']
market_share = [71, 27, 1, 1]

# Colors for the bars with gradient effect
colors = ['#4CAF50', '#2196F3', '#FFC107', '#9E9E9E']
gradient_colors = ['#66BB6A', '#42A5F5', '#FFD54F', '#BDBDBD']

# Create the plot
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection='3d')

# Add pseudo-3D bars
x_pos = np.arange(len(os_labels))
y_pos = np.zeros(len(os_labels))
z_pos = np.zeros(len(os_labels))
dx = np.full(len(os_labels), 0.6)
dy = np.full(len(os_labels), 0.5)

bars = ax.bar3d(x_pos, y_pos, z_pos, dx, dy, market_share, color=gradient_colors, edgecolor='grey', shade=True)

# Set labels and title
ax.set_xlabel('Operating System', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_zlabel('Height', fontsize=12)
ax.set_title("Global Smartphone Operating System\nMarket Share in 2023", fontsize=14, fontweight='bold')

# Customize the y and z axes
ax.set_yticks([])
ax.set_zticks(np.arange(0, 81, 10))
ax.set_zlim(0, 80)

# Adding percentage values on top of the bars
for i, percentage in enumerate(market_share):
    ax.text(x_pos[i], 0, percentage + 2, f'{percentage}%', ha='center', va='bottom', fontsize=11, fontweight='bold', color=gradient_colors[i])

# Annotations for insight
ax.text(0, 0, 75, "Android dominates with 71%", fontsize=11, color='darkgreen', fontweight='bold', backgroundcolor='w', bbox=dict(facecolor='w', edgecolor='grey', boxstyle='round,pad=0.3'))

# Tight layout adjustment for clarity
plt.tight_layout()

# Display the plot
plt.show()