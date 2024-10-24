import matplotlib.pyplot as plt
import numpy as np

# Define the farming techniques
farming_techniques = ['Traditional', 'Organic', 'Precision Farming']

# Create synthetic data representing crop yields (in tons per hectare) over a decade for each technique
# These numbers are adjusted to reflect realistic variations
traditional_yields = [3.1, 3.3, 3.4, 3.6, 3.7, 3.8, 4.0, 4.2, 4.3, 4.4]
organic_yields = [2.4, 2.6, 2.8, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
precision_yields = [4.6, 4.8, 5.0, 5.2, 5.3, 5.5, 5.7, 5.8, 6.0, 6.1]

# Compile these into a single list
yield_data = [traditional_yields, organic_yields, precision_yields]

# Horizontal box plot to visualize yield distribution across different farming techniques
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(yield_data, vert=False, patch_artist=True, showmeans=True, meanline=True,
                 notch=True, whis=1.5,
                 boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                 whiskerprops=dict(color='green', linewidth=1.5),
                 capprops=dict(color='darkgreen', linewidth=1.5),
                 medianprops=dict(color='red', linewidth=2),
                 meanprops=dict(color='orange', linewidth=2, linestyle='--'))

# Set y-ticks to display the farming techniques
ax.set_yticks([1, 2, 3])
ax.set_yticklabels(farming_techniques)

# Add titles and labels
plt.title("A Decade of Crop Yield Distribution:\nInsights into Farming Techniques (2013-2022)", 
          fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Crop Yield (Tons per Hectare)", fontsize=14)
plt.ylabel("Farming Techniques", fontsize=14)

# Adding grid to enhance readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding different colors for each box for better distinction
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add a legend explaining the components of the boxplot
handles = [plt.Line2D([0], [0], color='red', lw=2, label='Median'),
           plt.Line2D([0], [0], color='orange', lw=2, linestyle='--', label='Mean')]
plt.legend(handles=handles, loc='upper right', fontsize=10, title='Boxplot Elements', title_fontsize='12')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()