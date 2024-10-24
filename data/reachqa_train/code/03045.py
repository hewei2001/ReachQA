import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Define years and ocean regions
years = np.arange(2010, 2021)
ocean_regions = ["North Atlantic", "South Atlantic", "North Pacific", "South Pacific", "Indian Ocean"]

# Temperature anomalies data (°C)
temperature_anomalies = np.array([
    [0.12, 0.15, 0.16, 0.18, 0.21, 0.24, 0.28, 0.30, 0.33, 0.35, 0.37],
    [0.08, 0.10, 0.11, 0.13, 0.16, 0.18, 0.20, 0.23, 0.25, 0.28, 0.30],
    [0.14, 0.16, 0.18, 0.21, 0.23, 0.26, 0.29, 0.31, 0.34, 0.36, 0.39],
    [0.10, 0.12, 0.13, 0.15, 0.18, 0.20, 0.22, 0.25, 0.27, 0.29, 0.32],
    [0.09, 0.11, 0.12, 0.14, 0.17, 0.19, 0.21, 0.24, 0.26, 0.28, 0.31]
])

# Additional data: Average global anomalies for comparison
global_anomalies = np.mean(temperature_anomalies, axis=0)

# Create a figure with subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Main heatmap plot
heatmap = axs[0].imshow(temperature_anomalies, cmap='RdYlBu_r', aspect='auto', interpolation='nearest')

# Color bar configuration
cbar = fig.colorbar(heatmap, ax=axs[0], orientation='vertical', pad=0.02)
cbar.set_label('Temperature Anomaly (°C)', rotation=270, labelpad=20)

# Add titles and labels
axs[0].set_title('Global Ocean Temperature Anomalies:\nA Decade of Climate Observation (2010-2020)', fontsize=16, weight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Ocean Region', fontsize=12)

# Set ticks
axs[0].set_xticks(np.arange(len(years)))
axs[0].set_xticklabels(years, rotation=45, ha='right')
axs[0].set_yticks(np.arange(len(ocean_regions)))
axs[0].set_yticklabels(ocean_regions)

# Annotations for the heatmap
for i in range(len(ocean_regions)):
    for j in range(len(years)):
        text_color = 'white' if heatmap.get_cmap()(heatmap.norm(temperature_anomalies[i, j]))[0] < 0.5 else 'black'
        axs[0].text(j, i, f'{temperature_anomalies[i, j]:.2f}', ha='center', va='center', color=text_color, fontsize=9)

# Additional subplot for global anomalies
axs[1].plot(years, global_anomalies, marker='o', color='tab:blue')
axs[1].set_title('Average Global Temperature Anomalies Over Time', fontsize=14, weight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Average Anomaly (°C)', fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Add grid lines to the heatmap for clarity
axs[0].grid(visible=True, color='grey', linestyle='-', linewidth=0.5, alpha=0.2)

# Tight layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()