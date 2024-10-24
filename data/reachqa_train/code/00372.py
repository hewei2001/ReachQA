import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define guilds and their revenue data (in golden crowns)
guilds = ['Blacksmith Guild', 'Weaver Guild', 'Alchemist Guild', 'Mason Guild']

# Manually crafted revenue data
blacksmith_revenue = [250, 270, 260, 280, 300, 310, 305, 290, 275, 285, 295, 305]
weaver_revenue = [200, 210, 205, 215, 220, 230, 225, 215, 210, 215, 220, 230]
alchemist_revenue = [180, 190, 200, 195, 185, 205, 200, 190, 180, 195, 210, 215]
mason_revenue = [300, 320, 310, 305, 315, 325, 310, 300, 295, 315, 320, 330]

# Organize data for the box plot
guild_revenues = [blacksmith_revenue, weaver_revenue, alchemist_revenue, mason_revenue]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a vertical box plot
box = ax.boxplot(guild_revenues, vert=True, patch_artist=True, labels=guilds, notch=True, showfliers=True, whis=1.5)

# Define colors and patterns
colors = ['#FFD700', '#FF8C00', '#ADFF2F', '#4682B4']
patterns = ['/', '\\', '|', '-']

# Customize box plot colors
for patch, color, pattern in zip(box['boxes'], colors, patterns):
    patch.set_facecolor(color)
    patch.set_hatch(pattern)

# Whisker, cap, median settings
for element in ['whiskers', 'caps']:
    plt.setp(box[element], color='#8B4513', linewidth=1.5)
plt.setp(box['medians'], color='#FF6347', linewidth=2)

# Add data labels for mean
means = [np.mean(revenue) for revenue in guild_revenues]
for i, mean in enumerate(means):
    ax.text(i + 1, mean, f'{mean:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Add grid and enhance readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.set_axisbelow(True)

# Title and labels with improved readability
plt.title('Medieval Kingdom Economy:\nAnnual Revenues of Guilds in Galendra (1423)', fontsize=14, fontweight='bold')
plt.ylabel('Revenue (Golden Crowns)', fontsize=12)
plt.xlabel('Guilds', fontsize=12)

# Add legend for box colors
legend_handles = [mpatches.Patch(facecolor=color, edgecolor='black', label=guild, hatch=pattern) for color, guild, pattern in zip(colors, guilds, patterns)]
plt.legend(handles=legend_handles, title="Guilds", loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()