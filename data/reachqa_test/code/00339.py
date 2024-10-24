import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patheffects as pe

# Define the fields and corresponding funding percentages
fields = ['Quantum Computing', 'Bioengineering', 'Nanotechnology', 
          'Renewable Energy', 'Artificial Intelligence', 'Space Exploration']
funding = [20, 15, 10, 25, 20, 10]

# Define colors for each segment using a colormap for gradient effects
cmap = plt.get_cmap('viridis')
colors = [cmap(i / float(len(fields))) for i in range(len(fields))]

# Explode specific segments to highlight them
explode = (0.05, 0, 0, 0.1, 0.05, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    funding, colors=colors, labels=fields, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=explode, shadow=True
)

# Enhance wedges with gradient by applying transparency towards the edges
for w in wedges:
    w.set_alpha(0.9)

# Add the inner circle with text
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
ax.text(0, 0, "Total Funding\n100%", horizontalalignment='center', 
        verticalalignment='center', fontsize=14, weight='bold')

# Customizing the legend with icons
plt.legend(wedges, fields, title="Technology Sectors", loc="center left", 
           bbox_to_anchor=(1, 0, 0.5, 1), title_fontsize='13', fontsize='11')

# Customizing text properties for clarity
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=9)

# Set a multi-line title for better readability
ax.set_title("Funding Allocation\nTech Pioneer Program", fontsize=16, fontweight='bold', ha='center', va='center')

# Adjust layout
plt.tight_layout()

# Add subtle 3D effect using z-order adjustments and path effects
for w in wedges:
    w.set_zorder(2)
    w.set_path_effects([pe.withStroke(linewidth=1, foreground='grey')])

# Display the plot
plt.show()