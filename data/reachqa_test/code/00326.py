import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.gridspec as gridspec

# Data for the funnel chart: number of beans (in millions) at each stage
stages = ['Harvesting', 'Processing', 'Roasting', 'Packaging', 'Distribution', 'Retail']
beans = [100, 85, 70, 60, 58, 55]

# Colors for each stage
colors = ['#7D3C98', '#2874A6', '#239B56', '#F39C12', '#E67E22', '#D35400']

# Calculate relative widths for the funnel segments
max_beans = max(beans)
widths = np.array(beans) / max_beans

# Initialize the plot
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1])
ax1 = fig.add_subplot(gs[0, :])

# Draw each funnel stage with a trapezoidal shape
bottom = 0
height = 0.7
for i, (stage, color, width) in enumerate(zip(stages, colors, widths)):
    left = (1 - width) / 2
    trap_coords = [(left, bottom), 
                   (left + width, bottom), 
                   (1 - ((1 - width) / 2), bottom + height),
                   (0 + ((1 - width) / 2), bottom + height)]
    trap = patches.Polygon(trap_coords, closed=True, facecolor=color, edgecolor='black', alpha=0.8)
    ax1.add_patch(trap)
    bottom += height + 0.1
    
    # Annotate each stage
    ax1.text(0.5, bottom - height / 2 - 0.05, f'{stage}: {beans[i]}M', ha='center', va='center', 
             color='white', fontsize=12, fontweight='bold')

# Formatting
ax1.set_xlim(0, 1)
ax1.set_ylim(0, bottom)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.invert_yaxis()

# Title
ax1.set_title('Artisanal Coffee Journey\nFrom Bean to Cup', fontsize=16, weight='bold', pad=20)

# Add a 2D pie chart as a new subplot
ax2 = fig.add_subplot(gs[1, 0])
ax2.pie(beans, labels=stages, autopct='%1.1f%%', startangle=140, colors=colors, explode=[0.1]*len(stages))
ax2.set_title('Bean Distribution', fontsize=12, weight='bold')

# Add a subplot with bean count trend line
ax3 = fig.add_subplot(gs[1, 1])
ax3.plot(stages, beans, 'o-', color='#D35400', markersize=8, linewidth=2)
ax3.set_title('Bean Count Trend', fontsize=12, weight='bold')
ax3.set_ylabel('Beans (M)')
ax3.grid(True, which='both', linestyle='--', linewidth=0.5)

# Automatically adjust layout
plt.tight_layout()

# Show the chart
plt.show()