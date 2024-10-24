import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
species = ['Pigeons', 'Squirrels', 'Sparrows', 'Foxes', 'Bats']
population_change = [45, 20, -15, -5, 35]  # Population change in percentage

# Creating bar chart
fig, ax = plt.subplots(figsize=(10, 6))
x_pos = np.arange(len(species))
colors = ['#3e95cd', '#8e5ea2', '#3cba9f', '#e8c3b9', '#c45850']
bars = ax.bar(x_pos, population_change, color=colors, alpha=0.8, width=0.6)

# Add data annotations
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height + np.sign(height) * 2, 
            f'{height:+.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Set the title and labels
ax.set_title('Urban Wildlife Population Trends in Greenfield\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Species', fontsize=12)
ax.set_ylabel('Population Change (%)', fontsize=12)

# Set x-axis tick positions and labels
ax.set_xticks(x_pos)
ax.set_xticklabels(species, rotation=30, ha='right', fontsize=10)

# Adding a grid only on the y-axis for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Add a baseline
ax.axhline(0, color='black', linewidth=0.8)

# Adjust layout
plt.tight_layout()

# Show the chart
plt.show()