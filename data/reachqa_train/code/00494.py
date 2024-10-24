import matplotlib.pyplot as plt
import numpy as np

# Define the data
months = ['January', 'February', 'March', 'April']
central_perk = [5000, 5200, 5100, 5300]  # Monthly coffee sales (in cups)
the_beanery = [4800, 4700, 4900, 5000]
cafe_haven = [4500, 4600, 4400, 4700]
espresso_express = [5200, 5300, 5400, 5500]
java_junction = [4900, 5000, 4950, 5050]

# Position of bars on x-axis
x = np.arange(len(months))

# Width of a bar
width = 0.15

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bars1 = ax.bar(x - 2*width, central_perk, width, label='Central Perk', color='lightcoral')
bars2 = ax.bar(x - width, the_beanery, width, label='The Beanery', color='lightskyblue')
bars3 = ax.bar(x, cafe_haven, width, label='Café Haven', color='lightgreen')
bars4 = ax.bar(x + width, espresso_express, width, label='Espresso Express', color='lightgoldenrodyellow')
bars5 = ax.bar(x + 2*width, java_junction, width, label='Java Junction', color='plum')

# Customizing the plot
ax.set_title('Monthly Coffee Consumption by City Cafés\nin Brewville - 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Coffee Sales (Cups)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(months)

# Add grid lines for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adding legend
ax.legend(loc='upper left', title='Cafés', fontsize=10)

# Annotate with sales numbers on each bar
def add_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 50, int(yval), va='bottom', ha='center', fontsize=10)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)
add_labels(bars4)
add_labels(bars5)

# Automatically adjust layout to prevent text overlap and enhance clarity
plt.tight_layout()

# Show the plot
plt.show()