import matplotlib.pyplot as plt
import numpy as np

# Define wildlife species and city zones
species = ['Squirrels', 'Pigeons', 'Raccoons', 'Foxes', 'Hawks', 'Deer']
zones = ['Downtown', 'Suburban', 'Parks', 'Industrial', 'Residential', 'Waterfront']

# Create a matrix with activity levels (scale 1 to 10)
activity_levels = np.array([
    [8, 5, 9, 4, 7, 3],  # Squirrels
    [6, 8, 7, 5, 9, 4],  # Pigeons
    [4, 3, 8, 5, 6, 7],  # Raccoons
    [3, 2, 6, 7, 4, 9],  # Foxes
    [2, 7, 5, 6, 8, 5],  # Hawks
    [1, 4, 2, 3, 5, 9]   # Deer
])

# Calculate average activity for each zone
avg_activity_zone = activity_levels.mean(axis=0)

# Create the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Heatmap
cax = ax1.imshow(activity_levels, cmap='YlGnBu', interpolation='nearest', aspect='auto')
ax1.set_xticks(np.arange(len(zones)))
ax1.set_yticks(np.arange(len(species)))
ax1.set_xticklabels(zones, rotation=45, ha='right')
ax1.set_yticklabels(species)
ax1.set_title('Urban Wildlife Activity\nin Greenridge City Zones', fontsize=14, pad=10)
fig.colorbar(cax, ax=ax1, orientation='vertical', label='Activity Level')

# Add text annotations for activity levels
for i in range(len(species)):
    for j in range(len(zones)):
        ax1.text(j, i, activity_levels[i, j], ha='center', va='center', color='black', fontsize=8)

ax1.grid(which='minor', color='grey', linestyle='-', linewidth=0.5)
ax1.set_xticks(np.arange(-0.5, len(zones), 1), minor=True)
ax1.set_yticks(np.arange(-0.5, len(species), 1), minor=True)

# Subplot 2: Bar Chart for Average Activity per Zone
ax2.bar(zones, avg_activity_zone, color='skyblue')
ax2.set_title('Average Wildlife Activity\nby Zone', fontsize=14, pad=10)
ax2.set_xlabel('City Zones', fontsize=10)
ax2.set_ylabel('Average Activity Level', fontsize=10)
ax2.set_ylim(0, 10)
ax2.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()