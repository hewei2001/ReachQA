import matplotlib.pyplot as plt
import numpy as np

# Data for the juice brands in Fruitopia
brands = ['Juicy Joy', 'Citrus Splash', 'Tropical Twist', 'Berry Bliss', 'Green Zing']
units_sold = [1350, 1650, 1280, 1470, 1600]

# Colors for each brand
colors = ['#ffa07a', '#20b2aa', '#ff6347', '#9370db', '#3cb371']

# Indices for bar placement
indices = np.arange(len(brands))

# Additional data for a line chart, representing quarterly sales for all brands combined
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
quarterly_sales = [7200, 6700, 7100, 7300]

# Create a figure with 2 subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First subplot: Bar chart of annual sales
bars = ax1.bar(indices, units_sold, color=colors, alpha=0.7, width=0.6)
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 20, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax1.set_title('Fruitopia\'s Top Juice Brands:\nAnnual Sales Performance', fontsize=14, weight='bold', pad=20)
ax1.set_xticks(indices)
ax1.set_xticklabels(brands, rotation=15, ha='right', fontsize=10)
ax1.set_xlabel('Juice Brands', fontsize=12)
ax1.set_ylabel('Units Sold', fontsize=12)
ax1.set_ylim(0, max(units_sold) + 200)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Second subplot: Line chart of quarterly sales
ax2.plot(quarters, quarterly_sales, marker='o', color='#FF4500', linestyle='-', linewidth=2, markersize=8)
ax2.set_title('Quarterly Sales Trend\n(All Brands Combined)', fontsize=14, weight='bold', pad=20)
ax2.set_xlabel('Quarters', fontsize=12)
ax2.set_ylabel('Units Sold', fontsize=12)
ax2.set_ylim(0, max(quarterly_sales) + 500)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

# Overall layout adjustment
plt.tight_layout()

# Display the charts
plt.show()