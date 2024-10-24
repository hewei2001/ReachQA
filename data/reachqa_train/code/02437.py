import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap

# Define categories and data
categories = ['Cost', 'Speed', 'Convenience', 'Env. Impact', 'Safety']
modes = ['Buses', 'Trains', 'Bicycles', 'Cars', 'Walking']

# Data for each transportation mode
data = {
    'Buses': [8, 6, 7, 5, 7],
    'Trains': [7, 9, 8, 8, 8],
    'Bicycles': [9, 5, 6, 9, 6],
    'Cars': [5, 8, 9, 4, 6],
    'Walking': [10, 3, 5, 10, 7]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Define the colormap
cmap = get_cmap('viridis', len(modes))

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Customize the radar chart background
ax.set_facecolor('whitesmoke')

for i, (mode, values) in enumerate(data.items()):
    values += values[:1]
    color = cmap(i)

    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2.5, label=mode, marker='o')

# Adjust gridlines
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax.xaxis.grid(True, linestyle='-', color='lightgray')

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, weight='bold')

# Annotate one key value from each mode for demonstration
for i, (mode, values) in enumerate(data.items()):
    max_value = max(values[:-1])
    index_max = values.index(max_value)
    ax.annotate(f'{max_value}', 
                xy=(angles[index_max], max_value), 
                xytext=(angles[index_max], max_value + 0.5),
                ha='center', color=cmap(i), fontsize=9, fontweight='bold')

# Title and legend adjustments
plt.title('Performance of Urban Transportation Systems in Metroville\nBy Various Parameters', 
          size=16, color='darkblue', weight='bold', pad=25)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.1), title="Modes", fontsize=10)

ax.set_yticklabels([])  # Remove radial labels
plt.tight_layout()  # Adjust layout to prevent overlaps

# Display the plot
plt.show()