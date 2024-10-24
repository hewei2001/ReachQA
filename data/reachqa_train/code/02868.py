import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Original data for exoplanets
oxygen_levels = np.array([20, 15, 25, 5, 10, 18, 22, 8, 14, 30])  # Atmospheric Oxygen (%)
surface_temperatures = np.array([15, -50, 22, 45, 10, 0, 38, -75, 5, 28])  # Surface Temperature (°C)
water_presence = np.array([7, 1, 8, 3, 2, 5, 6, 1.5, 3, 8.5])  # Water Presence (arbitrary units)
habitability_index = np.array([0.8, 0.2, 0.85, 0.3, 0.5, 0.6, 0.75, 0.15, 0.35, 0.9])  # Habitability Index

# New data for overlay plot
# Calculating Potential Habitability Score as a derived metric
potential_habitability_score = (oxygen_levels * 0.4 + surface_temperatures * 0.3 + water_presence * 0.3) / 100

# Create meshgrid for surface plot
X, Y = np.meshgrid(np.linspace(min(oxygen_levels), max(oxygen_levels), 30),
                   np.linspace(min(surface_temperatures), max(surface_temperatures), 30))
Z = (X * 0.4 + Y * 0.3 + np.mean(water_presence) * 0.3) / 100  # Use average water presence for simplicity

# Color palette
colors = plt.cm.viridis(habitability_index)

# Create 3D figure
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the exoplanets as a 3D scatter plot
scatter = ax.scatter(
    oxygen_levels, 
    surface_temperatures, 
    water_presence, 
    s=habitability_index * 300, 
    c=colors, 
    cmap='viridis', 
    alpha=0.8, 
    edgecolors='w', 
    marker='o'
)

# Overlay the surface plot
ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.5, edgecolor='none')

# Customize the view
ax.view_init(elev=25, azim=135)

# Titles and labels
ax.set_title("Astrobiological Survey\nExoplanet Habitability Factors with Potential Score Overlay",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Atmospheric Oxygen (%)", fontsize=12, labelpad=15)
ax.set_ylabel("Surface Temperature (°C)", fontsize=12, labelpad=15)
ax.set_zlabel("Water Presence (units)", fontsize=12, labelpad=15)

# Add color bar for the scatter plot
cbar = fig.colorbar(scatter, ax=ax, pad=0.1, shrink=0.6)
cbar.set_label('Habitability Index', fontsize=12)

# Highlighting the most habitable exoplanet
max_habitability_idx = np.argmax(habitability_index)
ax.text(
    oxygen_levels[max_habitability_idx], 
    surface_temperatures[max_habitability_idx], 
    water_presence[max_habitability_idx], 
    'Most Habitable', 
    color='black', 
    fontsize=10, 
    weight='bold'
)

# Improve layout
plt.tight_layout()

# Show plot
plt.show()