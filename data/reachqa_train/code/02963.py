import matplotlib.pyplot as plt
import numpy as np

# List of fashion materials
materials = [
    "Cotton",
    "Wool",
    "Polyester",
    "Silk",
    "Nylon",
    "Acrylic",
    "Linen",
    "Leather",
    "Viscose",
    "Hemp"
]

# CO2 emissions data (kg CO2 per meter of material)
emissions = [
    2.2,  # Cotton
    7.3,  # Wool
    5.5,  # Polyester
    10.1, # Silk
    4.8,  # Nylon
    6.5,  # Acrylic
    1.8,  # Linen
    33.4, # Leather
    3.7,  # Viscose
    1.1   # Hemp
]

# Define colors for each material, using a colormap for diversity
colors = plt.cm.tab10(np.linspace(0, 1, len(materials)))

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(materials, emissions, color=colors, edgecolor='black')

# Add labels and title
ax.set_xlabel('CO2 Emissions (kg/m)', fontsize=12)
ax.set_ylabel('Fashion Materials', fontsize=12)
ax.set_title('CO2 Emissions in Fashion: \nA Material Perspective', fontsize=16, fontweight='bold', pad=20)

# Annotate each bar with its CO2 emission value
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.3, bar.get_y() + bar.get_height()/2, f'{width:.1f}', 
            va='center', ha='left', fontsize=10, color='black')

# Set y-tick parameters for better alignment
ax.set_yticks(range(len(materials)))
ax.set_yticklabels(materials, ha='right', fontsize=11)
ax.yaxis.set_tick_params(pad=5)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()