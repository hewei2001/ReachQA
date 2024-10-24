import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.interpolate import make_interp_spline

# Define distances (light-years) and luminosities (solar luminosities)
milky_way_distances = np.array([4.2, 7.5, 10.0, 25.0, 35.0, 50.0, 60.0, 80.0, 100.0, 120.0])
milky_way_luminosities = np.array([1.0, 5.0, 3.2, 7.1, 2.5, 10.0, 15.0, 8.5, 9.0, 6.8])

andromeda_distances = np.array([2.5, 5.0, 15.0, 30.0, 40.0, 55.0, 70.0, 90.0, 110.0, 130.0])
andromeda_luminosities = np.array([0.5, 2.0, 1.5, 6.5, 4.0, 12.0, 11.0, 3.5, 9.5, 5.5])

# New related data: average luminosity of star clusters (arbitrarily defined for illustration)
cluster_names = ['Cluster A', 'Cluster B', 'Cluster C', 'Cluster D']
milky_way_cluster_luminosities = [6.5, 4.0, 8.2, 7.0]  # Example data
andromeda_cluster_luminosities = [5.0, 3.2, 6.0, 5.5]  # Example data

# Create the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Main scatter plot for galaxies
axs[0].scatter(milky_way_distances, milky_way_luminosities, color='blue', label='Milky Way', s=100, alpha=0.7)
axs[0].scatter(andromeda_distances, andromeda_luminosities, color='orange', label='Andromeda', s=100, alpha=0.7)

# Smooth fitting using spline interpolation
x_mw_smooth = np.linspace(min(milky_way_distances), max(milky_way_distances), 300)
spl_mw = make_interp_spline(milky_way_distances, milky_way_luminosities, k=3)
y_mw_smooth = spl_mw(x_mw_smooth)
axs[0].plot(x_mw_smooth, y_mw_smooth, color='blue', linestyle='--', label='Milky Way Fit')

x_a_smooth = np.linspace(min(andromeda_distances), max(andromeda_distances), 300)
spl_a = make_interp_spline(andromeda_distances, andromeda_luminosities, k=3)
y_a_smooth = spl_a(x_a_smooth)
axs[0].plot(x_a_smooth, y_a_smooth, color='orange', linestyle='--', label='Andromeda Fit')

# Customizing the first subplot
axs[0].set_title('Galaxies and their Luminosity\nExploring Star Systems in the Universe', fontsize=16)
axs[0].set_xlabel('Distance from Earth (light-years)', fontsize=12)
axs[0].set_ylabel('Luminosity (solar luminosities)', fontsize=12)
axs[0].legend()
axs[0].grid(True, linestyle='--', alpha=0.7)

# Bar chart for average luminosity of star clusters
bar_width = 0.35
index = np.arange(len(cluster_names))
axs[1].bar(index, milky_way_cluster_luminosities, bar_width, label='Milky Way Clusters', color='blue', alpha=0.7)
axs[1].bar(index + bar_width, andromeda_cluster_luminosities, bar_width, label='Andromeda Clusters', color='orange', alpha=0.7)

# Customizing the second subplot
axs[1].set_title('Average Luminosity of Star Clusters', fontsize=16)
axs[1].set_xlabel('Star Clusters', fontsize=12)
axs[1].set_ylabel('Luminosity (solar luminosities)', fontsize=12)
axs[1].set_xticks(index + bar_width / 2)
axs[1].set_xticklabels(cluster_names)
axs[1].legend()
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()