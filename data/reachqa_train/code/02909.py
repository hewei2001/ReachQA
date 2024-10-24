import matplotlib.pyplot as plt
import numpy as np

# Energy sources and their respective percentage shares
energy_sources = ['Solar Fusion Reactors', 'Quantum Singularity Batteries', 
                  'Dark Matter Conversion', 'Antimatter Engines', 
                  'Hydrogen Fuel Cells', 'Organic Biomass Reactors']
percentages = [40, 25, 15, 10, 5, 5]

# Colors for each energy source
colors = ['#ffdd57', '#9b59b6', '#34495e', '#e74c3c', '#3498db', '#27ae60']

# Explode the 'Solar Fusion Reactors' slice to emphasize its prominence
explode = (0.1, 0, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Draw pie chart with hole in the center for donut effect
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=energy_sources, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='black'),
    explode=explode,
    shadow=True
)

# Customize the font and color of the percentage labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    
# Set chart title with line breaks for better readability
ax.set_title("Galactic Energy Sources of the Future:\nInterstellar Power Distribution in 2150", 
             fontsize=14, fontweight='bold', pad=20)

# Create a legend outside the chart
ax.legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()