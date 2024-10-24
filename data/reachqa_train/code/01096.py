import matplotlib.pyplot as plt
import numpy as np

# Categories to be assessed
categories = ['Speed', 'Intelligence', 'Strength', 'Flexibility', 'Battery Life']
num_vars = len(categories)

# Data for each robot
aero_bot = [85, 70, 60, 90, 80]
terra_tron = [60, 65, 85, 70, 95]
aqua_droid = [75, 80, 65, 75, 70]

# Additional data for overlay (e.g., projected improvements)
improvements = [10, 5, 8, 6, 7]  # Consistent increase in all metrics
avg_performance = np.mean([aero_bot, terra_tron, aqua_droid], axis=0)

# Create radar chart angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Radar chart setup
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Function to plot a single robot on the radar
def plot_radar(data, label, color):
    data += data[:1]  # Complete the loop
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, label=label, color=color, linewidth=2)

# Plot each robot's data
plot_radar(aero_bot, 'AeroBot', 'deepskyblue')
plot_radar(terra_tron, 'TerraTron', 'limegreen')
plot_radar(aqua_droid, 'AquaDroid', 'darkorange')

# Overlay line plot for average performance with improvements
improved_performance = (avg_performance + improvements).tolist()
improved_performance += improved_performance[:1]

ax.plot(angles, improved_performance, 'o-', color='red', linewidth=3, label='Avg + Improvements')
ax.fill(angles, improved_performance, color='red', alpha=0.1)

# Add the category labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Enhancements: Annotations for threshold
for i, angle in enumerate(angles[:-1]):
    ax.text(angle, improved_performance[i] + 5, f'{improved_performance[i]:.0f}', 
            horizontalalignment='center', color='red', size=8)

# Title and legend
plt.title('Tech Haven RoboAthlon 2045\nRobotic Performance Comparison with Projections', 
          fontsize=15, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Automatically adjust the layout for better display
plt.tight_layout()

# Display the chart
plt.show()