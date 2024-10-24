import matplotlib.pyplot as plt
import numpy as np

# Define sectors and their corresponding energy data
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']
solar = [40, 30, 25, 20]
wind = [25, 20, 15, 10]
hydro = [10, 15, 20, 15]
fossil_fuels = [15, 25, 30, 40]
nuclear = [10, 10, 10, 15]

# Combine energy data into a numpy array
energy_data = np.vstack([solar, wind, hydro, fossil_fuels, nuclear])

# Colors for each energy type with gradient variations
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500', '#8A2BE2']
gradients = [
    ['#FFFACD', '#FFD700', '#FFD700', '#FFD700'],  # Solar
    ['#ADD8E6', '#1E90FF', '#1E90FF', '#1E90FF'],  # Wind
    ['#98FB98', '#32CD32', '#32CD32', '#32CD32'],  # Hydro
    ['#FF7F50', '#FF4500', '#FF4500', '#FF4500'],  # Fossil Fuels
    ['#DDA0DD', '#8A2BE2', '#8A2BE2', '#8A2BE2']   # Nuclear
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width and initialize bottom positions for stacking
bar_width = 0.6
bottoms = np.zeros(len(sectors))

# Stacked bar chart
for idx, (energy, color) in enumerate(zip(energy_data, gradients)):
    bars = ax.bar(sectors, energy, label=['Solar', 'Wind', 'Hydro', 'Fossil Fuels', 'Nuclear'][idx], color=color, width=bar_width, bottom=bottoms)
    bottoms += energy
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2, f'{int(height)}%', ha='center', va='center', color='black', fontsize=10, fontweight='bold')

# Configure the plot aesthetics
ax.set_xlabel('Energy Consumption Sectors', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage Contribution', fontsize=14, fontweight='bold')
ax.set_title('Projected Energy Source Distribution\nin Futuroville for the Year 2050', fontsize=18, fontweight='bold')
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{y}%' for y in np.arange(0, 101, 10)], fontsize=12)

# Add cumulative percentage annotations at the top of each sector
for i, total in enumerate(bottoms):
    ax.text(i, total + 2, f'Total: {int(total)}%', ha='center', va='center', color='black', fontsize=11, fontweight='bold')

# Add legend
ax.legend(loc='upper left', fontsize=12, title='Energy Sources')

# Add subtle grid lines
ax.grid(axis='y', linestyle='--', color='gray', alpha=0.7)

# Enhance plot borders and axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('gray')
ax.spines['bottom'].set_color('gray')

# Automatically adjust subplot parameters for a neat layout
plt.tight_layout()

# Display the plot
plt.show()