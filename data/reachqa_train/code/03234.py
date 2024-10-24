import matplotlib.pyplot as plt
import numpy as np

# Define years and building heights data
years_built = np.array([2005, 2008, 2010, 2012, 2015, 2017, 2019, 2021, 2023, 2025])
building_heights = np.array([120, 135, 150, 170, 190, 210, 230, 250, 270, 300])

# Define architectural styles with color mapping
styles = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
style_colors = {1: 'royalblue', 2: 'darkorange', 3: 'forestgreen', 4: 'crimson', 5: 'purple'}

# Compute average building height per style
avg_heights_per_style = [np.mean(building_heights[styles == style]) for style in np.unique(styles)]

# Create figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Scatter Plot (Original)
for style in np.unique(styles):
    mask = styles == style
    axes[0].scatter(years_built[mask], building_heights[mask], s=100, c=style_colors[style], 
                    label=f'Style {style}', edgecolors='black', linewidth=0.8)

annotations = ['SkyRise', 'Horizon Tower', 'Vertex', 'Zenith', 'Pinnacle', 
               'Eclipse', 'Arcadia', 'Solstice', 'Aurora', 'Lumina']
for i, txt in enumerate(annotations):
    axes[0].annotate(txt, (years_built[i], building_heights[i]), fontsize=9, xytext=(5, 5), textcoords='offset points')

axes[0].set_xlabel('Year Built', fontsize=12)
axes[0].set_ylabel('Building Height (m)', fontsize=12)
axes[0].set_title('Neon City: Evolution of Building Heights\nfrom 2005 to 2025', fontsize=14, fontweight='bold', pad=20)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(title='Architectural Style', title_fontsize='13', fontsize='11', loc='upper left')

# Bar Plot (New)
axes[1].bar([f'Style {style}' for style in np.unique(styles)], avg_heights_per_style, color=style_colors.values())
axes[1].set_xlabel('Architectural Style', fontsize=12)
axes[1].set_ylabel('Average Building Height (m)', fontsize=12)
axes[1].set_title('Average Building Height per Architectural Style', fontsize=14, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()