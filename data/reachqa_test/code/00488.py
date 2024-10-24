import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# E-commerce spending data in dollars for ten categories across two years (2020-2021)
categories = ['Electronics', 'Fashion', 'Home & Garden', 'Health & Beauty', 
              'Sports & Outdoors', 'Toys', 'Groceries', 'Books', 
              'Automotive', 'Travel']

# Spending data in dollars (simulated for each category over 24 months)
data = {
    'Electronics': [200, 250, 270, 230, 300, 290, 260, 280, 310, 350, 240, 290, 260, 310, 280, 340, 360, 290, 320, 310, 300, 350, 370, 390],
    'Fashion': [150, 180, 200, 220, 190, 210, 230, 250, 240, 260, 270, 280, 300, 290, 260, 250, 240, 270, 290, 310, 320, 330, 340, 360],
    'Home & Garden': [100, 120, 130, 110, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 250, 240, 220, 210, 230, 240, 260],
    'Health & Beauty': [80, 90, 100, 110, 95, 105, 115, 125, 135, 145, 155, 165, 160, 170, 180, 185, 200, 190, 195, 205, 210, 220, 225, 230],
    'Sports & Outdoors': [150, 160, 170, 180, 165, 175, 185, 195, 205, 215, 220, 230, 240, 250, 260, 270, 280, 290, 285, 295, 300, 310, 320, 330],
    'Toys': [120, 130, 140, 150, 145, 155, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
    'Groceries': [300, 310, 290, 320, 310, 330, 340, 360, 350, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510],
    'Books': [70, 80, 90, 100, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285],
    'Automotive': [250, 260, 270, 280, 275, 285, 290, 295, 300, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460],
    'Travel': [400, 420, 430, 450, 440, 460, 480, 500, 490, 510, 520, 540, 530, 550, 560, 570, 580, 600, 610, 620, 630, 640, 650, 660],
}

# Convert the data into a suitable format for the horizontal box chart
spending_data = [data[category] for category in categories]
totals = [sum(data[category]) for category in categories]

# Create a figure with two subplots using GridSpec
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 1, height_ratios=[2, 1])

# First subplot: horizontal box chart (Consumer Spending Trends)
ax1 = fig.add_subplot(gs[0])
box = ax1.boxplot(spending_data, vert=False, patch_artist=True, labels=categories, notch=True, whis=1.5)

# Customizing box colors using the same colormap
colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding median markers
for median in box['medians']:
    ax1.plot(median.get_xdata(), median.get_ydata(), color='black', marker='o', markersize=8)

# Title and labels for the first plot
ax1.set_title('Consumer Spending Trends in E-commerce (2020-2021)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Spending Amount (USD)', fontsize=14)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Second subplot: total spending by category
ax2 = fig.add_subplot(gs[1])
bars = ax2.barh(categories, totals, color=colors)

# Adding data labels to the bars
for bar in bars:
    ax2.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():,.0f}', va='center', ha='left', fontsize=10)

# Title and labels for the second plot
ax2.set_title('Total Consumer Spending by Category (2020-2021)', fontsize=18, fontweight='bold', pad=20)
ax2.set_xlabel('Total Spending Amount (USD)', fontsize=14)
ax2.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout for better spacing
plt.tight_layout()

# Show the combined plots
plt.show()


plt.savefig("../images/00488.jpg", dpi=200)