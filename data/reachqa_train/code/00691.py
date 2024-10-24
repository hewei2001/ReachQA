import matplotlib.pyplot as plt
import squarify  # Used for creating tree maps
from matplotlib import cm
import matplotlib.patches as mpatches

# Define the data: energy sources and their market share
energy_sources = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']
market_share = [35, 25, 20, 10, 10]  # Market share in percentage

# Define colors using a colormap for a more appealing gradient effect
colors = cm.viridis([0.1, 0.3, 0.5, 0.7, 0.9])

# Prepare labels with icons for each energy source
icons = ['☀️', '🌬️', '💧', '🌋', '🌿']
labels = [f'{icon} {source}\n{share}%' for icon, source, share in zip(icons, energy_sources, market_share)]

# Create the plot
plt.figure(figsize=(14, 10))

# Plot shadow effect by drawing slightly larger squares behind the main plot
# Calculate normalized areas for shadow effect
normed_market_share = [val * 1.05 for val in market_share]  # Slightly increase for shadow effect
squarify.plot(sizes=normed_market_share, color=[cm.viridis(x) for x in [0.15, 0.35, 0.55, 0.75, 0.95]], alpha=0.3, 
              label=['' for _ in energy_sources])

# Main plot
squarify.plot(sizes=market_share, label=labels, color=colors, alpha=0.85, text_kwargs={'fontsize': 14, 'weight': 'bold'})

# Add title with multiple lines for better clarity
plt.title('The Transition to Renewable Energy\nMarket Share of Various Sources in 2023', 
          fontsize=20, fontweight='bold', pad=30, loc='center', color='#333')

# Adding a legend with patch for better understanding
legend_patches = [mpatches.Patch(color=colors[i], label=f'{icons[i]} {energy_sources[i]}') for i in range(len(energy_sources))]
plt.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.15, 1), title='Energy Sources', fontsize=12)

# Customize axes
plt.axis('off')  # Disable axes for clarity

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()