import matplotlib.pyplot as plt
import numpy as np

# Define the sectors and their corresponding energy types
sectors = [
    'Solar Farms', 'Fusion Reactors', 
    'Anti-Matter Generators', 'Quantum Fusion Arrays', 
    'Dark Matter Facilities', 'Hydrogen Harvesters'
]

energy_types = [
    'Photon Capture', 'Fusion Energy', 
    'Anti-Matter Synthesis', 'Quantum Flux', 
    'Dark Energy Extraction', 'Hydrogen Efficiency'
]

# Energy production distribution by type in each sector (percentages)
energy_data = np.array([
    [35, 25, 15, 10, 10, 5],  # Solar Farms
    [8, 45, 25, 12, 5, 5],    # Fusion Reactors
    [10, 8, 60, 12, 5, 5],    # Anti-Matter Generators
    [5, 10, 15, 60, 5, 5],    # Quantum Fusion Arrays
    [7, 7, 15, 10, 54, 7],    # Dark Matter Facilities
    [10, 10, 10, 10, 10, 50]  # Hydrogen Harvesters
])

# Colors for each energy type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Start plotting sector pie charts
fig, ax = plt.subplots(2, 3, figsize=(18, 12))
plt.subplots_adjust(top=0.9)
fig.suptitle("Galactic Energy Production Distribution\nby Sector (Year 3050)", fontsize=16, fontweight='bold', y=0.98)

# Explode parameter to highlight one section in each pie chart
explode = (0.1, 0, 0, 0, 0, 0)

# Iterate through each sector and plot the respective pie chart
for i, sector in enumerate(sectors):
    ax_row = i // 3
    ax_col = i % 3
    wedges, texts, autotexts = ax[ax_row, ax_col].pie(
        energy_data[i],
        labels=energy_types,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode,
        textprops=dict(color="black", fontsize=9)
    )
    # Adjust font sizes to improve readability
    for text in texts:
        text.set_fontsize(9)
    for autotext in autotexts:
        autotext.set_fontsize(9)
    ax[ax_row, ax_col].set_title(sector, fontsize=12, fontweight='bold')

# Add a legend for the energy types
fig.legend(wedges, energy_types, loc='center right', fontsize=10, title='Energy Types')

# Adjust layout to avoid text clipping
plt.tight_layout(rect=[0, 0, 0.85, 0.93])

# Show plot
plt.show()