import matplotlib.pyplot as plt
import numpy as np

# Define the regions and the number of unique cryptid species
regions = ["Transylvania", "Loch Ness", "Himalayas", "Amazon Rainforest", 
           "Australian Outback", "Pacific Northwest", "Bermuda Triangle"]
cryptid_counts = [15, 8, 12, 10, 7, 20, 5]

# Color palette for each region
colors = ['#8B4513', '#1E90FF', '#228B22', '#32CD32', '#FFD700', '#DAA520', '#9400D3']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the horizontal bar chart
bars = ax.barh(regions, cryptid_counts, color=colors, edgecolor='black', height=0.6)

# Add data labels on each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{int(width)}', ha='center', va='center', fontsize=10, color='black')

# Customize the appearance
ax.set_xlabel('Number of Unique Cryptid Species', fontsize=12, fontweight='bold')
ax.set_title('Cryptid Diversity:\nTop Regions Cataloging Mythical Creatures', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlim(0, max(cryptid_counts) + 5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set tick labels with appropriate alignment
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions, fontsize=11, weight='bold')

# Adjust layout to prevent any overlap and ensure the chart is visually appealing
plt.tight_layout()

# Display the plot
plt.show()