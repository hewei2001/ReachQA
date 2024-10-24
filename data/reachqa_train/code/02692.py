import matplotlib.pyplot as plt
import numpy as np

# Data setup
produce_types = ['Galactic Grains', 'Cosmic Fruits', 'Stellar Vegetables']
xylot_output = [120, 100, 80]
zarnon_output = [90, 130, 100]
kryla_output = [110, 80, 120]

# Define positions for bars
bar_positions = np.arange(len(produce_types))

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))

ax.bar(bar_positions, xylot_output, label='Xylot', color='#4db8ff', edgecolor='white')
ax.bar(bar_positions, zarnon_output, bottom=xylot_output, label='Zarnon', color='#ffcc66', edgecolor='white')
ax.bar(bar_positions, kryla_output, bottom=np.array(xylot_output) + np.array(zarnon_output), label='Kryla', color='#66cc99', edgecolor='white')

# Customize the chart
ax.set_title('Intergalactic Agricultural Produce Distribution\nAcross Andromeda\'s Planets', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Type of Produce', fontsize=12)
ax.set_ylabel('Total Production (Units)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(produce_types, fontsize=10, rotation=15)

# Add a legend
ax.legend(title='Planet', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate totals on top of the bars
for i, (x, z, k) in enumerate(zip(xylot_output, zarnon_output, kryla_output)):
    total = x + z + k
    ax.text(i, total + 5, str(total), ha='center', fontsize=10, fontweight='bold')

# Display the grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()