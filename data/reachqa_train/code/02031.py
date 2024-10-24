import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Patch

# Data for the eco-friendly beverage production
beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]  # Production volumes in millions of liters
market_share = [12, 9, 14, 18, 8]  # Market share percentages

# Use a seaborn color palette for a more sophisticated look
colors = sns.color_palette("pastel")

# Plotting the bar chart with a secondary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create bars for production volumes
bars = ax1.bar(beverages, production_volumes, color=colors, alpha=0.85, edgecolor='black', hatch='/')

# Adding data annotations on each bar with a secondary axis for market share
ax2 = ax1.twinx()
ax2.plot(beverages, market_share, color='gray', marker='o', linewidth=2, label='Market Share (%)')

for bar, volume, share in zip(bars, production_volumes, market_share):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1.5, f'{volume}M', ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 4, f'{share}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='blue')

# Title and labels
ax1.set_title("Eco-Friendly Beverage Production\nand Market Share Overview", fontsize=16, fontweight='bold')
ax1.set_xlabel("Beverage Type", fontsize=14)
ax1.set_ylabel("Production Volume (Million Liters)", fontsize=14)
ax2.set_ylabel("Market Share (%)", fontsize=14)

# Highlighting the most produced beverage with a border
most_produced_index = np.argmax(production_volumes)
for i, bar in enumerate(bars):
    if i == most_produced_index:
        bar.set_edgecolor('red')
        bar.set_linewidth(2)

# Custom legend with patches
legend_elements = [
    Patch(facecolor=colors[most_produced_index], edgecolor='red', label=f"Top Producer: {beverages[most_produced_index]}"),
    Patch(facecolor='none', edgecolor='gray', label='Market Share (%)', linestyle='-')
]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=10, frameon=False)

# Grid and styling
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)
ax2.yaxis.grid(False)
ax1.set_axisbelow(True)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()