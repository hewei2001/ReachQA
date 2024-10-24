import matplotlib.pyplot as plt
import numpy as np

# Define the regions and the number of unique cryptid species
regions = ["Transylvania", "Loch Ness", "Himalayas", "Amazon Rainforest", 
           "Australian Outback", "Pacific Northwest", "Bermuda Triangle"]
cryptid_counts = [15, 8, 12, 10, 7, 20, 5]

# Synthetic data for the overlay plot: Number of cryptid sightings
cryptid_sightings = [30, 50, 25, 40, 15, 45, 10]

# Colors for bars and overlay plot
bar_colors = ['#8B4513', '#1E90FF', '#228B22', '#32CD32', '#FFD700', '#DAA520', '#9400D3']
line_color = '#FF6347'  # Tomato red for the line plot

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the horizontal bar chart
bars = ax1.barh(regions, cryptid_counts, color=bar_colors, edgecolor='black', height=0.6, label='Unique Cryptid Species')

# Add data labels on each bar
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{int(width)}', ha='center', va='center', fontsize=10, color='black')

# Customize the appearance for the bar chart
ax1.set_xlabel('Number of Unique Cryptid Species', fontsize=12, fontweight='bold')
ax1.set_title('Cryptid Diversity:\nTop Regions Cataloging Mythical Creatures', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlim(0, max(cryptid_counts) + 5)
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.set_yticks(np.arange(len(regions)))
ax1.set_yticklabels(regions, fontsize=11, weight='bold')

# Add a secondary axis for the overlay line plot
ax2 = ax1.twiny()
ax2.plot(cryptid_sightings, regions, color=line_color, marker='o', linestyle='-', linewidth=2, label='Cryptid Sightings')

# Customize the overlay plot
ax2.set_xlabel('Number of Cryptid Sightings', fontsize=12, fontweight='bold', color=line_color)
ax2.tick_params(axis='x', labelcolor=line_color)

# Combine legends from both plots
bars_legend = ax1.legend(loc='lower right', frameon=False)
line_legend = ax2.legend(loc='upper left', frameon=False)
ax1.add_artist(bars_legend)

# Tight layout
plt.tight_layout()

# Display the plot
plt.show()