import matplotlib.pyplot as plt
import numpy as np

# Define the sectors and their corresponding energy types
sectors = ['Solar Farms', 'Fusion Reactors', 'Anti-Matter Generators', 'Quantum Fusion Arrays']
energy_types = ['Photon Capture', 'Fusion Energy', 'Anti-Matter Synthesis', 'Quantum Flux']

# Energy production distribution by type in each sector (percentages)
energy_data = np.array([
    [40, 30, 20, 10],  # Solar Farms
    [10, 50, 30, 10],  # Fusion Reactors
    [20, 10, 50, 20],  # Anti-Matter Generators
    [10, 20, 20, 50]   # Quantum Fusion Arrays
])

# Colors for each energy type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Start plotting sector pie charts
fig, ax = plt.subplots(2, 2, figsize=(14, 14))
plt.subplots_adjust(top=0.85)
fig.suptitle("Galactic Energy Production Distribution\nby Sector (Year 3050)", fontsize=18, fontweight='bold', y=0.98)

# Explode parameter to highlight one section in each pie chart
explode = (0.1, 0, 0, 0)

# Iterate through each sector and plot the respective pie chart
for i, sector in enumerate(sectors):
    ax_row = i // 2
    ax_col = i % 2
    wedges, texts, autotexts = ax[ax_row, ax_col].pie(
        energy_data[i],
        labels=energy_types,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode,
        textprops=dict(color="black", fontsize=10)
    )
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_fontsize(10)
    ax[ax_row, ax_col].set_title(sector, fontsize=14, fontweight='bold')

# Add a legend for the energy types
fig.legend(wedges, energy_types, loc='center right', fontsize=12, title='Energy Types')

# Adjust layout to avoid text clipping
plt.tight_layout(rect=[0, 0, 0.85, 0.95])

# Show plot
plt.show()