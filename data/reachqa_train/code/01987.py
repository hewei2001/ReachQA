import numpy as np
import matplotlib.pyplot as plt

# Define sectors and energy types
sectors = ['Residential', 'Industrial', 'Commercial']
energy_types = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']

# Contribution percentages for each energy type within each sector for 2025
energy_data_2025 = {
    'Residential': [45, 35, 8, 6, 6],
    'Industrial': [12, 20, 38, 25, 5],
    'Commercial': [28, 22, 10, 8, 32]
}

# Projected contribution percentages for 2030
energy_data_2030 = {
    'Residential': [50, 30, 5, 10, 5],
    'Industrial': [15, 25, 40, 15, 5],
    'Commercial': [30, 20, 15, 10, 25]
}

# Colors for energy types
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513', '#FF6347']  # Gold, Dodger Blue, Lime Green, Saddle Brown, Tomato

# Create a figure
fig = plt.figure(figsize=(18, 8))

# Define the polar plot (Rose chart)
ax_polar = plt.subplot(1, 2, 1, polar=True)
num_sectors = len(sectors)
angles = np.linspace(0, 2 * np.pi, num_sectors, endpoint=False).tolist()
for i, energy in enumerate(energy_types):
    heights = [energy_data_2025[sector][i] for sector in sectors]
    angles_bar = np.repeat(angles, 2)
    angles_bar[1::2] += 2 * np.pi / num_sectors
    ax_polar.bar(angles_bar, np.repeat(heights, 2), width=2 * np.pi / num_sectors / len(energy_types),
                 color=colors[i], edgecolor='white', linewidth=1, label=energy, alpha=0.7)

ax_polar.set_theta_offset(np.pi / 2)
ax_polar.set_theta_direction(-1)
ax_polar.set_xticks(angles)
ax_polar.set_xticklabels(sectors, fontsize=12, fontweight='bold')
ax_polar.set_yticklabels([])
ax_polar.set_title("Greentopia: Renewable Energy Sources\nDistribution Across Sectors (2025)", fontsize=14, fontweight='bold', pad=20)
ax_polar.legend(title='Energy Types', loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10)

# Define the stacked bar chart for projected data 2030
ax_bar = plt.subplot(1, 2, 2)
bar_width = 0.3
x = np.arange(len(sectors))

for i, energy in enumerate(energy_types):
    bottom = np.zeros(len(sectors)) if i == 0 else np.sum([[energy_data_2030[sector][j] for sector in sectors] for j in range(i)], axis=0)
    heights = [energy_data_2030[sector][i] for sector in sectors]
    ax_bar.bar(x + i * bar_width, heights, bar_width, color=colors[i], label=energy, bottom=bottom, alpha=0.8)

ax_bar.set_xticks(x + bar_width * (len(energy_types) - 1) / 2)
ax_bar.set_xticklabels(sectors, fontsize=12, fontweight='bold')
ax_bar.set_ylabel("Percentage Contribution", fontsize=12)
ax_bar.set_title("Projected Energy Distribution Across Sectors (2030)", fontsize=14, fontweight='bold')
ax_bar.legend(title='Energy Types', fontsize=10)

plt.tight_layout()
plt.show()