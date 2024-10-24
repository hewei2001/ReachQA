import matplotlib.pyplot as plt
import numpy as np

# Define the sectors and their corresponding green energy adoption data (in percentage)
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']
adoption_data = {
    'Residential': [45, 25, 20, 10],   # Solar, Wind, Geothermal, Other
    'Commercial': [30, 30, 25, 15],    # Solar, Wind, Biomass, Other
    'Industrial': [15, 30, 45, 10],    # Solar, Wind, Hydroelectric, Other
    'Transportation': [40, 35, 15, 10] # Electric, Biofuels, Hydrogen, Other
}

# Colors for each type of green energy
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Bottom position tracker for stacked bar
bottom = np.zeros(len(sectors))

# Plot each type of green energy as a stacked bar
for i, (energy_type, color) in enumerate(zip(adoption_data['Residential'], colors)):
    data = [adoption_data[sector][i] for sector in sectors]
    ax.bar(sectors, data, bottom=bottom, color=color, width=0.5, edgecolor='white')
    bottom += np.array(data)

# Customize the plot
ax.set_title("2023 Green Energy Adoption\nby Sector", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sectors", fontsize=12)
ax.set_ylabel("Percentage of Green Energy Use (%)", fontsize=12)
ax.set_ylim(0, 100)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.legend(['Solar', 'Wind', 'Other Renewables', 'Misc.'], title="Energy Types", loc='upper right', fontsize=10)

# Annotate percentage values on each stack
for i, sector in enumerate(sectors):
    bottom = 0
    for j, color in enumerate(colors):
        height = adoption_data[sector][j]
        ax.text(i, bottom + height/2, f'{height}%', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
        bottom += height

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()