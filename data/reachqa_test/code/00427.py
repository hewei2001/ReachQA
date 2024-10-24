import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Define regions and age groups
regions = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']

# Updated literacy rates as percentages
literacy_rates = np.array([
    [55, 85, 98, 92, 70],  # 0-14
    [65, 88, 96, 94, 75],  # 15-24
    [75, 90, 99, 96, 85],  # 25-54
    [60, 82, 94, 89, 78],  # 55-64
    [40, 75, 88, 82, 58],  # 65+
])

# Calculate average literacy rates by age group
average_literacy_by_age = literacy_rates.mean(axis=1)

# Create figure with subplots
fig, (ax_heatmap, ax_line) = plt.subplots(2, 1, figsize=(10, 12), gridspec_kw={'height_ratios': [3, 1]})

# Heatmap
cmap = mcolors.LinearSegmentedColormap.from_list('custom_viridis', ['#440154', '#3B528B', '#21908C', '#5DC863', '#FDE725'])
cax = ax_heatmap.imshow(literacy_rates, cmap=cmap, aspect='auto')
ax_heatmap.grid(visible=True, color='grey', linewidth=0.5, linestyle='--', alpha=0.3)

# Color bar
cbar = fig.colorbar(cax, ax=ax_heatmap, orientation='vertical', shrink=0.8)
cbar.set_label('Literacy Rate (%)')

# Axis labels
ax_heatmap.set_xticks(np.arange(len(regions)))
ax_heatmap.set_yticks(np.arange(len(age_groups)))
ax_heatmap.set_xticklabels(regions, rotation=45, ha='right')
ax_heatmap.set_yticklabels(age_groups)
ax_heatmap.set_xlabel('Regions')
ax_heatmap.set_ylabel('Age Groups')
ax_heatmap.set_title('Global Literacy Rates Across Age Groups in 2023\n(Expressed as Percentage)', fontsize=14)

# Annotate cells with literacy rates
for i in range(len(age_groups)):
    for j in range(len(regions)):
        value = literacy_rates[i, j]
        ax_heatmap.text(j, i, f"{value}%", ha="center", va="center",
                        color="white" if value > 65 else "black")

# Line graph for average literacy by age group
ax_line.plot(age_groups, average_literacy_by_age, marker='o', linestyle='-', color='dodgerblue')
ax_line.set_title('Average Literacy Rate by Age Group', fontsize=12)
ax_line.set_ylabel('Literacy Rate (%)')
ax_line.set_xlabel('Age Groups')
ax_line.grid(visible=True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()
