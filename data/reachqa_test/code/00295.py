import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap

# Define the regions and their renewable energy adoption percentages
regions = ['North America', 'Europe', 'Asia', 'Africa']
renewable_percentages = [45, 55, 30, 20]

# Enhanced color map for gradient effect
cmap = cm.get_cmap('Greens', 256)
gradient_colors = cmap(np.linspace(0.4, 0.9, len(regions)))

# Create a figure with two subplots: main chart and pie chart for context
fig, (ax, ax_pie) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 1]})

# Plot horizontal bars with gradient colors
bars = ax.barh(regions, renewable_percentages, color=gradient_colors, edgecolor='black', linewidth=1.2)

# Add percentage data labels with enhanced style
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{int(width)}%', va='center', ha='left', fontsize=11, color='black', bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

# Title and labels with multi-line title
ax.set_title('Renewable Energy Adoption Rates\nAcross Global Regions', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Percentage of Energy from Renewable Sources (%)', fontsize=12)
ax.set_xlim(0, 100)

# Add custom ticks
ax.set_xticks(range(0, 101, 20))

# Grid lines for readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.grid(False)

# Bold y-axis labels
ax.set_yticklabels(regions, fontsize=11, weight='bold')

# Legend configuration, integrating it into the plot
for rect, label in zip(bars, regions):
    height = rect.get_height()
    ax.text(rect.get_x() - 1.5, rect.get_y() + height / 2, label, va='center', ha='right', fontsize=10, color='gray')

# Add pie chart as context to show proportional adoption
pie_values = [sum(renewable_percentages) / len(renewable_percentages), 100 - sum(renewable_percentages) / len(renewable_percentages)]
pie_labels = ['Renewable', 'Non-Renewable']
ax_pie.pie(pie_values, labels=pie_labels, autopct='%1.1f%%', colors=['#76c7c0', '#d3d3d3'],
           startangle=90, wedgeprops={'edgecolor': 'black'})
ax_pie.set_title('Global Energy\nComposition', fontsize=12, fontweight='bold')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()