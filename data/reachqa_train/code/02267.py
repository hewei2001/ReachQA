import matplotlib.pyplot as plt
import numpy as np

# Define building materials and their usage percentage
materials = ["Concrete", "Wood", "Steel", "Brick", "Glass", "Insulation"]
usage_percentages = [30, 25, 15, 10, 12, 8]

# Sort materials by usage percentage for a clearer visualization
sorted_indices = np.argsort(usage_percentages)
materials_sorted = [materials[i] for i in sorted_indices]
usage_percentages_sorted = [usage_percentages[i] for i in sorted_indices]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(materials_sorted, usage_percentages_sorted, color=plt.cm.tab20(np.linspace(0, 1, len(materials_sorted))))

# Add data labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center', fontsize=10, color='black')

# Customize plot appearance
ax.set_xlabel('Percentage of Total Material Usage', fontsize=12, fontweight='bold')
ax.set_ylabel('Building Materials', fontsize=12, fontweight='bold')
ax.set_title('Material Usage in Residential Construction:\nSustainable Practices in 2023', fontsize=14, fontweight='bold')
ax.invert_yaxis()  # Put highest usage at the top
ax.set_xlim(0, 35)  # Set x-axis limits for better spacing and visibility
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()