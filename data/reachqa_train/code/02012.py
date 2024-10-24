import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data for the chart
species = ['Pigeons', 'Squirrels', 'Sparrows', 'Foxes', 'Bats']
population_change = [45, 20, -15, -5, 35]  # Population change in percentage

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))
x_pos = np.arange(len(species))

# Color map for dynamic colors
cmap = plt.cm.get_cmap('RdYlGn')
colors = [cmap((1 + (change / 100)) / 2) for change in population_change]

# Creating bars with gradient and pattern overlay
bars = ax.bar(x_pos, population_change, color=colors, width=0.6)

# Add data annotations with arrows
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:+.1f}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, np.sign(height) * 5),
                textcoords='offset points',
                ha='center', va='bottom', fontsize=10,
                arrowprops=dict(facecolor='black', arrowstyle='->'))

# Set title and labels
ax.set_title('Urban Wildlife Population Trends in Greenfield\nFrom 2010 to 2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Species', fontsize=12)
ax.set_ylabel('Population Change (%)', fontsize=12)

# Customize x-axis
ax.set_xticks(x_pos)
ax.set_xticklabels(species, rotation=30, ha='right', fontsize=10)

# Add grid, baseline, and adjust layout
ax.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
ax.axhline(0, color='black', linewidth=0.8)

# Adding a legend to explain color gradient
gradient_patch = mpatches.Patch(color=cmap(0.75), label='Positive Change')
negative_patch = mpatches.Patch(color=cmap(0.25), label='Negative Change')
ax.legend(handles=[gradient_patch, negative_patch], title='Population Trend', loc='upper left')

# Add a background pattern or gradient
ax.set_facecolor('#f5f5f5')

# Tight layout adjustment
plt.tight_layout()

# Show the chart
plt.show()