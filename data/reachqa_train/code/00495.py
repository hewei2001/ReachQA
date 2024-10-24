import matplotlib.pyplot as plt
import numpy as np

# Define the data
months = ['January', 'February', 'March', 'April']
central_perk = [5000, 5200, 5100, 5300]  # Monthly coffee sales (in cups)
the_beanery = [4800, 4700, 4900, 5000]
cafe_haven = [4500, 4600, 4400, 4700]
espresso_express = [5200, 5300, 5400, 5500]
java_junction = [4900, 5000, 4950, 5050]

# Additional data for the line plot: Historical average sales
historical_avg_sales = [4700, 4900, 5000, 5200]  # Example average sales over previous years

# Position of bars on x-axis
x = np.arange(len(months))

# Width of a bar
width = 0.15

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Bar chart (first subplot)
ax1.bar(x - 2*width, central_perk, width, label='Central Perk', color='lightcoral')
ax1.bar(x - width, the_beanery, width, label='The Beanery', color='lightskyblue')
ax1.bar(x, cafe_haven, width, label='Café Haven', color='lightgreen')
ax1.bar(x + width, espresso_express, width, label='Espresso Express', color='lightgoldenrodyellow')
ax1.bar(x + 2*width, java_junction, width, label='Java Junction', color='plum')

# Bar chart customization
ax1.set_title('Monthly Coffee Consumption by City Cafés\nin Brewville - 2023', fontsize=14, fontweight='bold')
ax1.set_xlabel('Month', fontsize=10)
ax1.set_ylabel('Coffee Sales (Cups)', fontsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(months)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', title='Cafés', fontsize=9)

# Annotate with sales numbers on each bar
def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 50, int(yval), va='bottom', ha='center', fontsize=8)

# Add labels to all bars
add_labels(ax1, ax1.patches)

# Line plot (second subplot)
ax2.plot(months, historical_avg_sales, marker='o', color='darkorange', label='Historical Avg Sales')

# Line plot customization
ax2.set_title('Historical Average Coffee Sales\n(2018-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Month', fontsize=10)
ax2.set_ylabel('Average Coffee Sales (Cups)', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()