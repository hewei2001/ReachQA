import matplotlib.pyplot as plt
import numpy as np

# Data for the original bar chart
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
contributions = [22, 35, 18, 15, 10]

# Data for the overlay line plot (projected growth in contributions)
years = np.array([2023, 2024, 2025, 2026, 2027])
projected_contributions = {
    'Solar': [22, 24, 27, 30, 32],
    'Wind': [35, 37, 40, 42, 43],
    'Hydroelectric': [18, 17, 16, 15, 14],
    'Geothermal': [15, 16, 17, 18, 19],
    'Biomass': [10, 11, 11.5, 12, 12.5]
}

# Colors for each energy source
colors = ['#FFD700', '#76C7C0', '#6495ED', '#DEB887', '#98FB98']
line_styles = ['-', '--', '-.', ':', '-']

# Create a horizontal bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Bar plot
bars = ax1.barh(energy_sources, contributions, color=colors, edgecolor='grey', height=0.6)

# Adding percentage labels to each bar
for bar, percentage in zip(bars, contributions):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{percentage}%', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

# Add a second y-axis for the line plot
ax2 = ax1.twinx()

# Line plot for projected contributions
for idx, (source, projected) in enumerate(projected_contributions.items()):
    ax2.plot(projected, years, label=f'Projected {source}', color=colors[idx], linestyle=line_styles[idx], marker='o')

# Title and labels
ax1.set_title("Renewable Energy Contributions and Projections\nin GreenLandia (2023-2027)", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Contribution (%)", fontsize=12)
ax1.set_ylabel("Energy Sources", fontsize=12)
ax2.set_ylabel("Year", fontsize=12)

# Limit x-axis and y-axis
ax1.set_xlim(0, 45)
ax2.set_ylim(2022.5, 2027.5)

# Add grid lines for clarity
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust y-ticks for the energy sources
ax1.set_yticks(np.arange(len(energy_sources)))
ax1.set_yticklabels(energy_sources, fontsize=12, fontweight='bold')

# Add legend
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()