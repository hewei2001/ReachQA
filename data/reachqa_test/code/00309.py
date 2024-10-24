import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data for civilizations and their technological advancements
civilizations = ['Andromedans', 'Zenithians', 'Aurorans', 'Nebulons', 'Solarians']
sectors = ['Quantum Computing', 'Bioengineering', 'Energy Harnessing', 'Space Travel',
           'Nanotechnology', 'Communication Systems', 'AI']

advancements = [
    [80, 90, 75, 85, 70, 88, 95],  # Andromedans
    [65, 75, 80, 70, 95, 85, 90],  # Zenithians
    [78, 60, 88, 82, 77, 92, 84],  # Aurorans
    [72, 85, 82, 75, 80, 90, 88],  # Nebulons
    [90, 87, 77, 85, 85, 78, 80]   # Solarians
]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(16, 9))

# Bar chart parameters
bar_width = 0.15
index = np.arange(len(sectors))
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(civilizations)))  # Colorblind-friendly palette

# Plot bars for each civilization
for i, civilization in enumerate(civilizations):
    bars = ax.bar(index + i * bar_width, advancements[i], bar_width, label=civilization, color=colors[i])
    
    # Add text labels above the bars for precise values
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, yval, ha='center', va='bottom', fontsize=9)

# Set title and labels
ax.set_title("Galactic Innovations:\nTechnological Advancements Across Alien Civilizations", 
             fontsize=16, fontweight='bold', pad=20, loc='left', color='navy')
ax.set_xlabel('Technological Sectors', fontsize=12, labelpad=10, color='darkgreen')
ax.set_ylabel('Advancement Level', fontsize=12, labelpad=10, color='darkgreen')
ax.set_xticks(index + bar_width * (len(civilizations) - 1) / 2)
ax.set_xticklabels(sectors, rotation=30, ha='right', fontsize=11, color='darkslategray')

# Add legend with custom patches
custom_legend = [mpatches.Patch(color=colors[i], label=civilizations[i]) for i in range(len(civilizations))]
ax.legend(handles=custom_legend, title='Civilizations', title_fontsize='10', fontsize='9', loc='upper left')

# Add grid lines for y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add a subtle space-themed background
ax.set_facecolor('#f0f8ff')

# Ensure tight layout for visual clarity
plt.tight_layout()

# Show plot
plt.show()