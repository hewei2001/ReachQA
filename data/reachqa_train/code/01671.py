import matplotlib.pyplot as plt
import numpy as np

# Data for the juice brands in Fruitopia
brands = ['Juicy Joy', 'Citrus Splash', 'Tropical Twist', 'Berry Bliss', 'Green Zing']
units_sold = [1350, 1650, 1280, 1470, 1600]

# Colors for each brand
colors = ['#ffa07a', '#20b2aa', '#ff6347', '#9370db', '#3cb371']

# Indices for bar placement
indices = np.arange(len(brands))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars
bars = ax.bar(indices, units_sold, color=colors, alpha=0.7, width=0.6)

# Annotate bars with units sold
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 20, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the chart
ax.set_title('Fruitopia\'s Top Juice Brands:\nAnnual Sales Performance', fontsize=16, weight='bold', pad=20)
ax.set_xticks(indices)
ax.set_xticklabels(brands, rotation=15, ha='right', fontsize=10)
ax.set_xlabel('Juice Brands', fontsize=12)
ax.set_ylabel('Units Sold', fontsize=12)
ax.set_ylim(0, max(units_sold) + 200)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()