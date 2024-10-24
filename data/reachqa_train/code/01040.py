import matplotlib.pyplot as plt
import numpy as np

# Initiatives and their corresponding funding in millions of dollars
initiatives = [
    "Coral Reef Restoration",
    "Marine Protected Areas",
    "Pollution Clean-up",
    "Sustainable Fisheries",
    "Public Education & Awareness",
    "Marine Research & Innovation"
]
funding = [25, 30, 15, 20, 10, 18]  # Funding in millions

# Define a color palette using a colormap
cmap = plt.get_cmap('cool')
colors = cmap(np.linspace(0.15, 0.85, len(initiatives)))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the horizontal bar chart
bars = ax.barh(initiatives, funding, color=colors, edgecolor='black', height=0.6)

# Annotate the funding values on the bars
for bar in bars:
    ax.text(
        bar.get_width() + 0.5, 
        bar.get_y() + bar.get_height() / 2,
        f'{bar.get_width()}M', 
        va='center', 
        ha='left', 
        fontsize=10,
        color='black'
    )

# Add title and labels
ax.set_title(
    'Funding Distribution\nfor Ocean Conservation Initiatives', 
    fontsize=14, 
    fontweight='bold', 
    pad=20
)
ax.set_xlabel('Funding in Millions ($M)', fontsize=12)
ax.set_ylabel('Initiatives', fontsize=12)

# Style adjustments
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Add vertical gridlines
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

# Customize y-tick labels
ax.set_yticks(np.arange(len(initiatives)))
ax.set_yticklabels(initiatives, fontsize=11)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()