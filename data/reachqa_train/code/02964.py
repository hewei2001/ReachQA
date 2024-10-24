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

# Hypothetical industry average CO2 emissions (kg CO2 per meter of material)
industry_averages = [
    3.0,  # Cotton
    6.5,  # Wool
    6.0,  # Polyester
    9.0,  # Silk
    5.0,  # Nylon
    6.0,  # Acrylic
    2.0,  # Linen
    30.0, # Leather
    4.0,  # Viscose
    1.5   # Hemp
]

# Define colors for each material, using a colormap for diversity
colors = plt.cm.tab10(np.linspace(0, 1, len(materials)))

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(materials, emissions, color=colors, edgecolor='black', label='Actual CO2 Emissions')

# Overlay a line plot for industry averages
ax.plot(industry_averages, materials, linestyle='--', marker='o', color='darkblue', linewidth=2, label='Industry Avg CO2 Emissions')

# Add labels and title
ax.set_xlabel('CO2 Emissions (kg/m)', fontsize=12)
ax.set_title('CO2 Emissions in Fashion Materials: \nActual vs Industry Averages', fontsize=16, fontweight='bold', pad=20)

# Annotate each bar with its CO2 emission value
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.3, bar.get_y() + bar.get_height()/2, f'{width:.1f}', 
            va='center', ha='left', fontsize=10, color='black')

# Add a legend
ax.legend(loc='upper right', fontsize=11)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()