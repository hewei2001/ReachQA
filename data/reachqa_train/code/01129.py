import matplotlib.pyplot as plt
import numpy as np

# Artificial data representing daily sales transaction values (in USD)
east_coast_sales = np.array([120, 135, 150, 142, 155, 160, 165, 170, 178, 185, 192, 200, 205, 210, 195, 190])
midwest_sales = np.array([90, 95, 105, 100, 110, 115, 118, 122, 128, 135, 140, 142, 145, 138, 130, 125])
west_coast_sales = np.array([160, 170, 175, 180, 185, 190, 195, 200, 210, 215, 220, 230, 235, 240, 225, 220])

# Store regions and sales data
regions = ['East Coast', 'Midwest', 'West Coast']
data = [east_coast_sales, midwest_sales, west_coast_sales]

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Violin plot with box plot overlay
vparts = ax.violinplot(data, showmedians=False, showmeans=False, showextrema=False, widths=0.7)
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.3, labels=regions)

# Set color scheme
colors = ['#FFA07A', '#98FB98', '#ADD8E6']

# Customize violin plot appearance
for i, pc in enumerate(vparts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.3)

# Customize box plot appearance
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.setp(box['medians'], color='red', linewidth=2)
plt.setp(box['whiskers'], color='blue', linewidth=1.5, linestyle='--')
plt.setp(box['caps'], color='black', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='gray', alpha=0.5)

# Annotate median values
for i, (dataset, region) in enumerate(zip(data, regions), start=1):
    median = np.median(dataset)
    ax.text(i, median + 2, f'{median:.0f}', horizontalalignment='center', fontsize=10, color='red', weight='bold')

# Add title and labels
ax.set_title('Distribution of Daily Sales Transactions\nAcross TechGadgets Stores in 2023', fontsize=16, weight='bold', pad=20)
ax.set_ylabel('Transaction Value (USD)', fontsize=12)
ax.set_xlabel('Region', fontsize=12)

# Grid and layout adjustments
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Legend customization
handles = [plt.Line2D([0], [0], color=color, lw=4, label=region) for color, region in zip(colors, regions)]
ax.legend(handles=handles, title='Regions', loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()