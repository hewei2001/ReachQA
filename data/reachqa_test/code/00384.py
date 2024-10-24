import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define regions and product categories
regions = ['Northeast', 'Midwest', 'South', 'West Coast']
product_categories = ['Electronics', 'Fashion', 'Home Goods', 'Beauty & Personal Care']

# Define data as percentages (adjusted for consistency)
data = np.array([
    [22, 28, 18, 32],  # Northeast
    [24, 22, 20, 34],  # Midwest
    [20, 26, 22, 32],  # South
    [26, 30, 18, 26]   # West Coast
])

# Create a figure with two subplots
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# Define x and y coordinates
x = np.arange(len(regions))
y = np.arange(len(product_categories))
X, Y = np.meshgrid(x, y)

# Set bar width/depth and colors
width, depth = 0.4, 0.4
colors = ['b', 'g', 'r', 'y']  # Colors for each region

# Plot 3D bars for each region, adjusted for better spacing
for i in range(len(regions)):
    ax1.bar3d(X[:, i] - width/2, Y[:, i] - depth/2, np.zeros(len(product_categories)), width, depth, data[i, :], color=colors[i], alpha=0.8)

# Label x, y, and z axes
ax1.set_xticks(x)
ax1.set_xticklabels(regions, rotation=45, ha='right', fontsize=9)
ax1.set_yticks(y)
ax1.set_yticklabels(product_categories, rotation=5, fontsize=9)
ax1.set_zlim(0, 40)
ax1.set_zlabel('Percentage')
ax1.set_title("Regional Distribution of Online Shopping Preferences\nin the United States", fontsize=12)

# Line chart for total online shopping percentage over time
time_points = np.arange(2018, 2022)
total_shopping_percentages = np.array([
    [24, 27, 30, 33],  # Northeast
    [22, 24, 26, 28],  # Midwest
    [20, 23, 25, 28],  # South
    [27, 29, 31, 33]   # West Coast
])
for i in range(len(regions)):
    ax2.plot(time_points, total_shopping_percentages[i], label=regions[i], marker='o')

# Set title and labels for line chart
ax2.set_title('Total Online Shopping Percentage Over Time', fontsize=12)
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Percentage', fontsize=10)
ax2.legend()

# Adjust layout for clarity
fig.tight_layout()

# Display the plots
plt.show()