import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Data for solar energy usage by sector
sectors = ["Residential", "Commercial", "Industrial", "Public Transportation", "Miscellaneous"]
energy_usage = [30, 25, 15, 20, 10]

# Colors with subtle gradients simulated by slightly different shades
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF66B3']
hatches = ['/', '\\', '|', '-', '+']  # Different patterns for each sector

# Explode the slice for the public transportation sector to emphasize it
explode = (0, 0, 0, 0.1, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    energy_usage, 
    explode=explode, 
    labels=sectors, 
    colors=colors, 
    autopct='%1.1f%%', 
    shadow=True, 
    startangle=90,
    pctdistance=0.85
)

# Apply patterns to each pie wedge
for wedge, hatch in zip(wedges, hatches):
    wedge.set_hatch(hatch)

# Enhance text labels
for text in texts:
    text.set_fontsize(10)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_weight('bold')

# Add a custom legend
patches = [mpatches.Patch(facecolor=color, hatch=hatch, label=sector) 
           for color, hatch, sector in zip(colors, hatches, sectors)]
ax.legend(handles=patches, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, title="Sectors")

# Set the title with multiline and font enhancement
ax.set_title(
    'Solar Energy Usage Distribution\nin Solis, 2050 - Highlighting Public Transportation',
    fontsize=16, fontweight='bold', va='bottom', pad=40
)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()