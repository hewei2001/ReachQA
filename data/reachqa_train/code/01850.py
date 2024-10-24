import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Centuries and construction methods
centuries = ['15th Century', '18th Century', '20th Century']
methods = ['Stone Masonry', 'Brickwork', 'Wood Framing', 'Steel Framing']

# Prevalence of construction methods (%) in each century
data = np.array([
    [60, 30, 10, 0],   # 15th Century
    [20, 50, 30, 0],   # 18th Century
    [10, 20, 30, 40]   # 20th Century
])

# Number of methods and centuries
num_centuries = len(centuries)
num_methods = len(methods)

# Positions for bars
x_pos = np.arange(num_centuries)
y_pos = np.arange(num_methods)

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Customize bar colors
colors = ['#7B9F35', '#D95F02', '#7570B3', '#E7298A']

# Plot each construction method as a separate set of bars
for i, (color, method) in enumerate(zip(colors, methods)):
    ax.bar3d(x_pos, i * np.ones(num_centuries), np.zeros(num_centuries), 0.4, 0.4, data[:, i],
             color=color, alpha=0.8, label=method)

# Setting labels and title
ax.set_xlabel('Centuries', labelpad=15)
ax.set_ylabel('Construction Methods', labelpad=15)
ax.set_zlabel('Prevalence (%)', labelpad=10)
ax.set_title('Evolution of Construction Methods\nAcross Centuries', fontsize=16, pad=30)

# Set ticks for centuries and methods
ax.set_xticks(x_pos + 0.2)
ax.set_xticklabels(centuries, fontsize=10, rotation=25, ha='right')
ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=10)

# Add a legend to describe each construction method
ax.legend(title='Methods', loc='upper left', bbox_to_anchor=(0.9, 1.0), fontsize=9)

# Enhance the view by rotating the angle
ax.view_init(elev=25, azim=-50)

# Automatically adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()