import matplotlib.pyplot as plt
import numpy as np

# Define the sectors and their corresponding green energy adoption data (in percentage)
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation', 'Agriculture', 'Public Services']
adoption_data = {
    'Residential': [25, 20, 15, 10, 5, 25],  # Solar, Wind, Geothermal, Biomass, Hydroelectric, Other
    'Commercial': [20, 25, 20, 10, 5, 20],
    'Industrial': [10, 15, 30, 15, 10, 20],
    'Transportation': [40, 10, 5, 20, 5, 20],
    'Agriculture': [10, 25, 10, 20, 20, 15],
    'Public Services': [15, 30, 20, 10, 15, 10]
}

# Colors for each type of green energy
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Bottom position tracker for stacked bar
bottom = np.zeros(len(sectors))

# Plot each type of green energy as a stacked bar
for i, color in enumerate(colors):
    data = [adoption_data[sector][i] for sector in sectors]
    ax.bar(sectors, data, bottom=bottom, color=color, width=0.5, edgecolor='white')
    bottom += np.array(data)

# Customize the plot
ax.set_title("2023 Green Energy Adoption by Sector\nAn In-depth Overview", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sectors", fontsize=12)
ax.set_ylabel("Percentage of Green Energy Use (%)", fontsize=12)
ax.set_ylim(0, 100)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.legend(['Solar', 'Wind', 'Geothermal', 'Biomass', 'Hydroelectric', 'Other'], title="Energy Types", loc='upper left', fontsize=10)

# Annotate percentage values on each stack
for i, sector in enumerate(sectors):
    bottom = 0
    for j, color in enumerate(colors):
        height = adoption_data[sector][j]
        if height > 5:  # Annotate only if percentage is significant
            ax.text(i, bottom + height/2, f'{height}%', ha='center', va='center', color='white', fontsize=9, fontweight='bold')
        bottom += height

# Additional plot: a line plot showing the total renewable adoption per sector
total_adoption = [sum(adoption_data[sector]) for sector in sectors]
ax2 = ax.twinx()
ax2.plot(sectors, total_adoption, color='black', marker='o', linestyle='-', linewidth=2, label='Total Adoption (%)')
ax2.set_ylabel("Total Green Energy Adoption (%)", fontsize=12)
ax2.set_ylim(0, 100)
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()