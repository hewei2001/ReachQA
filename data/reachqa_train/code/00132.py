import numpy as np
import matplotlib.pyplot as plt

# Define the data for the 3D bar chart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
coffee_varieties = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']

# Sales data in units sold (rows: months, columns: coffee varieties)
sales_data = np.array([
    [150, 200, 250, 180, 220],  # January
    [180, 230, 260, 190, 210],  # February
    [200, 250, 270, 220, 230],  # March
    [210, 240, 300, 230, 250],  # April
    [220, 260, 320, 250, 270],  # May
    [240, 270, 330, 270, 290]   # June
])

# Prepare the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define colors for each coffee variety
colors = ['#8B4513', '#DEB887', '#D2691E', '#A0522D', '#CD853F']

# Dimensions of the bars
dx = dy = 0.5

# Plot each coffee variety's sales data
for y, color in enumerate(colors):
    xs = np.arange(len(months))
    ys = sales_data[:, y]
    ax.bar3d(xs, y, np.zeros_like(xs), dx, dy, ys, color=color, alpha=0.8, label=coffee_varieties[y])

# Set axis labels and ticks
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months)
ax.set_yticks(np.arange(len(coffee_varieties)))
ax.set_yticklabels(coffee_varieties)
ax.set_xlabel('Months', labelpad=10)
ax.set_ylabel('Coffee Varieties', labelpad=10)
ax.set_zlabel('Units Sold', labelpad=10)

# Set a viewing angle for better visibility
ax.view_init(elev=20, azim=135)

# Add title and legend
ax.set_title('Monthly Sales Performance\nof Coffee Varieties in a Café', fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=10)

# Improve layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()