import matplotlib.pyplot as plt
import numpy as np

# Expanded data with more categories and subcategories
energy_sources = [
    'Solar Energy', 'Onshore Wind', 'Offshore Wind', 
    'Geothermal', 'Hydroelectric', 
    'Nuclear', 'Biomass', 'Tidal Power', 'Fossil Fuels'
]
percentages = [20, 12, 10, 8, 18, 5, 10, 7, 10]  # Hypothetical complex dataset

# Corresponding colors
colors = ['#FFD700', '#00BFFF', '#1E90FF', '#DAA520', '#4682B4', 
          '#C0C0C0', '#A52A2A', '#4B0082', '#8B0000']

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Stacked bar chart representation
cumulative = np.zeros(len(percentages))
subcategories = [2, 1, 1, 1, 1, 1, 1, 1, 1]  # Correct length of subcategories
pos = 0
for i, (energy, percent, color) in enumerate(zip(energy_sources, percentages, colors)):
    if subcategories[i] > 1:
        for j in range(subcategories[i]):
            label = f"{energy} - Part {j+1}"
            part_percent = percent / subcategories[i]
            ax1.barh(pos, part_percent, color=color, left=cumulative[i] + j * part_percent, label=label)
    else:
        ax1.barh(pos, percent, color=color, left=cumulative[i], label=energy)
    cumulative[i] += percent
    pos += 1

# Add data labels
for bar in ax1.patches:
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height() / 2, 
             f'{bar.get_width():.1f}%', ha='center', va='center', 
             fontsize=10, fontweight='bold', color='black')

# Customize the plot
ax1.set_title('Energy Source Distribution and Breakdown\nin Electra City - Year 2075', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Percentage Contribution', fontsize=12)
ax1.set_xlim(0, 60)  # Adjust x-limits for readability
ax1.set_yticks(np.arange(len(energy_sources)))  # Set y-ticks
ax1.set_yticklabels(energy_sources)  # Correct y-tick labels to match categories
ax1.xaxis.grid(True, linestyle='--', alpha=0.5)
ax1.set_axisbelow(True)

# Legend and layout
ax1.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.15, 1.0))
plt.tight_layout()

# Display the plot
plt.show()