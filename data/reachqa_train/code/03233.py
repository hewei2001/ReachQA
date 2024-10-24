import matplotlib.pyplot as plt
import numpy as np

# Define years and building heights data
years_built = np.array([2005, 2008, 2010, 2012, 2015, 2017, 2019, 2021, 2023, 2025])
building_heights = np.array([120, 135, 150, 170, 190, 210, 230, 250, 270, 300])

# Define architectural styles with color mapping
styles = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
style_colors = {1: 'royalblue', 2: 'darkorange', 3: 'forestgreen', 4: 'crimson', 5: 'purple'}

# Create the scatter plot
plt.figure(figsize=(12, 8))
for style in np.unique(styles):
    mask = styles == style
    plt.scatter(years_built[mask], building_heights[mask], 
                s=100, c=style_colors[style], label=f'Style {style}', edgecolors='black', linewidth=0.8)

# Annotate specific buildings
annotations = ['SkyRise', 'Horizon Tower', 'Vertex', 'Zenith', 'Pinnacle', 'Eclipse', 'Arcadia', 'Solstice', 'Aurora', 'Lumina']
for i, txt in enumerate(annotations):
    plt.annotate(txt, (years_built[i], building_heights[i]), fontsize=9, xytext=(5,5), textcoords='offset points')

# Add labels and title
plt.xlabel('Year Built', fontsize=12)
plt.ylabel('Building Height (m)', fontsize=12)
plt.title('Neon City: Evolution of Building Heights\nfrom 2005 to 2025', fontsize=16, fontweight='bold', pad=20)

# Add legend
plt.legend(title='Architectural Style', title_fontsize='13', fontsize='11', loc='upper left', bbox_to_anchor=(1, 1))

# Enhance grid for readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()