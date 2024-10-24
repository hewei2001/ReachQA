import matplotlib.pyplot as plt
import numpy as np

# Artificial data representing daily sales transaction values (in USD)
east_coast_sales = np.array([120, 135, 150, 142, 155, 160, 165, 170, 178, 185, 192, 200, 205, 210, 195, 190])
midwest_sales = np.array([90, 95, 105, 100, 110, 115, 118, 122, 128, 135, 140, 142, 145, 138, 130, 125])
west_coast_sales = np.array([160, 170, 175, 180, 185, 190, 195, 200, 210, 215, 220, 230, 235, 240, 225, 220])

# Combine data into a list
data = [east_coast_sales, midwest_sales, west_coast_sales]

# Store regions for labeling
regions = ['East Coast', 'Midwest', 'West Coast']

# Plotting the vertical box chart
fig, ax = plt.subplots(figsize=(12, 8))

# Creating the boxplot
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, labels=regions, widths=0.6)

# Customizing boxplot colors and appearance
colors = ['#FFA07A', '#98FB98', '#ADD8E6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customizing medians, whiskers, caps, etc.
plt.setp(box['medians'], color='red', linewidth=2)
plt.setp(box['whiskers'], color='blue', linewidth=1.5, linestyle='--')
plt.setp(box['caps'], color='black', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='gray', alpha=0.5)

# Add title and labels
ax.set_title('Distribution of Daily Sales Transactions\nAcross TechGadgets Stores in 2023', fontsize=16, weight='bold', pad=20)
ax.set_ylabel('Transaction Value (USD)', fontsize=12)
ax.set_xlabel('Region', fontsize=12)

# Additional grid and display adjustments
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Adding a legend for the box colors
for region, color in zip(regions, colors):
    plt.plot([], [], color=color, label=region, linewidth=10)
plt.legend(title='Regions', loc='upper right')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()