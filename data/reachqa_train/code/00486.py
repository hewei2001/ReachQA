import matplotlib.pyplot as plt
import numpy as np

# Define the formats and their sales data over a decade
formats = ['Hardcover', 'Paperback', 'E-Book', 'Audiobook']

# Fabricated sales data in thousands
sales_data = [
    [120, 130, 140, 125, 135, 120, 150, 140, 145, 130],  # Hardcover
    [180, 190, 185, 175, 200, 195, 210, 205, 200, 180],  # Paperback
    [50, 60, 70, 90, 100, 120, 130, 140, 150, 160],      # E-Book
    [10, 15, 20, 25, 35, 45, 55, 60, 70, 80]             # Audiobook
]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Horizontal box plot with customized colors and styles
box = ax.boxplot(sales_data, vert=False, patch_artist=True, notch=True, 
                 boxprops=dict(facecolor='#8dc3a7', color='#3c763d'),
                 whiskerprops=dict(color='#3c763d'),
                 capprops=dict(color='#3c763d'),
                 medianprops=dict(color='red'),
                 flierprops=dict(marker='o', color='#a94442', alpha=0.7))

# Customize each box's color individually
colors = ['#f2ae72', '#6e5773', '#9a9eab', '#2a363b']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set the y-ticks and labels
ax.set_yticks(np.arange(1, len(formats) + 1))
ax.set_yticklabels(formats)

# Set x-axis label and chart title with line breaks for better readability
ax.set_xlabel('Sales in Thousands')
ax.set_title('The Evolution of Book Formats:\nA Decade of Changing Preferences (2010-2020)', 
             fontsize=14, fontweight='bold', loc='center')

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()