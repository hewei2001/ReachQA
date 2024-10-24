import matplotlib.pyplot as plt
import numpy as np

# Define the expanded regions and seasons
regions = ["Downtown", "Suburbs", "Industrial", "Residential", "Commercial", "Urban", "Rural", "TechPark"]
seasons = ["Winter", "Spring", "Summer", "Fall", "Monsoon", "Dry Season"]

# Construct IAQI and Health Impact data for each region and season
iaq_data = np.array([
    [65, 75, 55, 60, 70, 68, 62, 65],  # Winter
    [75, 85, 60, 68, 76, 73, 66, 72],  # Spring
    [55, 70, 45, 82, 62, 66, 58, 63],  # Summer
    [60, 78, 52, 75, 64, 70, 60, 68],  # Fall
    [67, 77, 50, 70, 72, 74, 65, 69],  # Monsoon
    [62, 80, 48, 73, 68, 71, 62, 70]   # Dry Season
])

health_impact_data = np.array([
    [15, 25, 10, 12, 18, 17, 14, 15],
    [18, 28, 12, 15, 20, 19, 15, 17],
    [12, 20, 8, 22, 15, 16, 12, 14],
    [14, 26, 9, 19, 16, 18, 13, 16],
    [16, 23, 7, 17, 18, 20, 14, 16],
    [13, 27, 8, 18, 17, 18, 15, 17]
])

# Rotate the data for alignment
iaq_data = np.rot90(iaq_data)
health_impact_data = np.rot90(health_impact_data)

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# First plot: Heatmap for IAQI
cax1 = axs[0].imshow(iaq_data, cmap='coolwarm', aspect='auto', interpolation='nearest')
fig.colorbar(cax1, ax=axs[0], label='Indoor Air Quality Index (IAQI)')

axs[0].set_yticks(np.arange(len(regions)))
axs[0].set_xticks(np.arange(len(seasons)))
axs[0].set_yticklabels(regions)
axs[0].set_xticklabels(seasons)
axs[0].set_title('Comprehensive Air Quality Assessment\nAcross Diverse Urban Settings', fontsize=16, fontweight='bold', pad=10)
plt.setp(axs[0].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add text annotations with average calculation
for i in range(len(regions)):
    for j in range(len(seasons)):
        average_value = (iaq_data[i, j] + health_impact_data[i, j]) / 2
        axs[0].text(j, i, f"{iaq_data[i, j]}\n({average_value:.1f})", ha='center', va='center', color='black', fontsize=8)

# Second plot: Health Impact Bar Chart
for i, region in enumerate(regions):
    axs[1].bar(np.arange(len(seasons)) + i / len(regions), health_impact_data[i], width=0.1, label=f'{region}', alpha=0.8)

axs[1].set_xticks(np.arange(len(seasons)))
axs[1].set_xticklabels(seasons)
axs[1].set_title('Health Impact Index Distribution by Season', fontsize=14, fontweight='bold')
axs[1].legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.setp(axs[1].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

plt.tight_layout()
plt.show()