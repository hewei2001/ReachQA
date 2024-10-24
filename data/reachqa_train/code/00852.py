import matplotlib.pyplot as plt
import numpy as np

# Define the regions and years
regions = ["Latin America", "Africa", "Asia", "Oceania"]
years = ["2019", "2020", "2021", "2022", "2023"]

# Original yield data in tons per hectare
yield_data = {
    "Latin America": [
        [1.8, 2.0, 1.9, 2.2, 1.7],
        [2.1, 2.3, 2.0, 2.5, 2.0],
        [2.0, 2.2, 1.8, 2.6, 2.1],
        [2.3, 2.5, 2.2, 2.8, 2.4],
        [2.4, 2.6, 2.5, 3.0, 2.5]
    ],
    "Africa": [
        [1.5, 1.6, 1.7, 1.5, 1.4],
        [1.6, 1.7, 1.8, 1.7, 1.5],
        [1.7, 1.8, 1.9, 1.8, 1.6],
        [1.8, 2.0, 1.9, 2.0, 1.7],
        [2.0, 2.1, 2.0, 2.2, 1.8]
    ],
    "Asia": [
        [2.0, 2.1, 2.2, 2.0, 1.9],
        [2.1, 2.3, 2.4, 2.1, 2.0],
        [2.2, 2.4, 2.5, 2.3, 2.1],
        [2.5, 2.7, 2.6, 2.5, 2.3],
        [2.6, 2.8, 2.7, 2.6, 2.4]
    ],
    "Oceania": [
        [1.9, 2.0, 1.8, 1.7, 1.8],
        [2.0, 2.1, 2.0, 1.9, 1.9],
        [2.2, 2.3, 2.1, 2.0, 2.0],
        [2.4, 2.5, 2.3, 2.2, 2.1],
        [2.5, 2.6, 2.4, 2.3, 2.2]
    ]
}

# Compute mean yields for line plot
mean_yields = {region: [np.mean(yields) for yields in yield_data[region]] for region in regions}

# Prepare data for box plot
box_data = [yield_data[region][year_idx] for year_idx in range(len(years)) for region in regions]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Box plot
ax1.boxplot(box_data, vert=True, notch=True, patch_artist=True,
            positions=np.arange(1, len(box_data) + 1),
            boxprops=dict(facecolor='lightblue', color='blue', alpha=0.6),
            whiskerprops=dict(color='blue', linewidth=1.5),
            capprops=dict(color='blue', linewidth=1.5),
            medianprops=dict(color='darkblue', linewidth=2))
ax1.set_title("Coffee Bean Yield Variability\nAcross Regions (2019-2023)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year and Region", fontsize=12)
ax1.set_ylabel("Yield (Tons per Hectare)", fontsize=12)
xtick_labels = [f"{year} - {region}" for year in years for region in regions]
ax1.set_xticks(range(1, len(xtick_labels) + 1))
ax1.set_xticklabels(xtick_labels, rotation=45, ha='right', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Line plot
for region in regions:
    ax2.plot(years, mean_yields[region], marker='o', label=region)
ax2.set_title("Average Yield Trends Across Regions (2019-2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Average Yield (Tons per Hectare)", fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', color='grey', alpha=0.7)

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()