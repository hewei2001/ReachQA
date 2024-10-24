import matplotlib.pyplot as plt
import numpy as np

# Data: percentage contribution to total energy production
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
contributions = [22, 35, 18, 15, 10]

# Colors for each energy source
colors = ['#FFD700', '#76C7C0', '#6495ED', '#DEB887', '#98FB98']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(energy_sources, contributions, color=colors, edgecolor='grey', height=0.6)

# Add percentage labels to each bar
for bar, percentage in zip(bars, contributions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{percentage}%', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

# Title and labels
ax.set_title("Renewable Energy Contributions\nin GreenLandia for 2023", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Contribution (%)", fontsize=12)
ax.set_ylabel("Energy Sources", fontsize=12)

# Limit x-axis to improve spacing around bars
ax.set_xlim(0, 40)

# Grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust y-ticks
ax.set_yticks(np.arange(len(energy_sources)))
ax.set_yticklabels(energy_sources, fontsize=12, fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()