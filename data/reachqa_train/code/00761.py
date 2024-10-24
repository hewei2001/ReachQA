import matplotlib.pyplot as plt
import numpy as np

# Define commodities and their trade volumes
commodities = ['Martian Minerals', 'Earthly Technologies', 
               'Agricultural Products', 'Water Resources', 
               'Medical Supplies']
trade_volumes = [200, 150, 180, 120, 90]  # Trade volumes in thousands of tons

# Define colors for the bars
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#F3FF33']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create a bar chart
bars = ax.bar(np.arange(len(commodities)), trade_volumes, color=colors, edgecolor='black')

# Title and labels
ax.set_title('Intergalactic Trade Commodities:\nEarth to Mars Exchange in 2150', fontsize=16, fontweight='bold')
ax.set_xlabel('Commodities', fontsize=14)
ax.set_ylabel('Trade Volume (in thousands of tons)', fontsize=14)

# Set the x-tick labels and rotate them for better readability
ax.set_xticks(np.arange(len(commodities)))
ax.set_xticklabels(commodities, rotation=45, ha='right')

# Add data labels above bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}k', ha='center', va='bottom', fontsize=12)

# Add a legend with descriptions
ax.legend(bars, ['Rich Martian ore deposits', 'Advanced Earth tech gadgets', 
                 'Essential food supplies', 'Vital water resources', 
                 'Crucial medical kits'],
          title='Commodity Description', loc='upper right')

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()