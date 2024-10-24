import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Increased data for voyages and corresponding sea monster sightings
voyages = np.arange(1, 21)  # 20 voyages for increased complexity
sightings = np.array([5, 7, 6, 10, 13, 15, 12, 18, 20, 22,
                      25, 29, 32, 30, 35, 37, 36, 40, 45, 50])

# Additional group representing a different type of sea monster
sightings_type2 = np.array([3, 5, 7, 9, 14, 11, 17, 19, 21, 23,
                            26, 28, 30, 34, 32, 36, 39, 42, 48, 53])

# Labels for the periods of discovery, aligned with the new data
period_labels = [
    "Ancient", "Early Middle Ages", "Viking Age", "Late Middle Ages",
    "Age of Discovery", "Golden Age of Piracy", "Enlightenment",
    "Industrial Revolution", "Modern Exploration", "Digital Age Mapping",
    "Artificial Intelligence", "Space Age", "Genetic Era", "Quantum Leap",
    "Robotic Expansion", "Asteroid Mining", "Digital Singularity",
    "Universal Peace", "Interstellar Travel", "Galactic Federation"
]

# Create figure and axis
plt.figure(figsize=(14, 10))

# Scatter plot for the first group
plt.scatter(voyages, sightings, color='darkblue', edgecolor='black', s=100, label='Type 1 Sightings')

# Scatter plot for the second group
plt.scatter(voyages, sightings_type2, color='red', edgecolor='black', s=100, label='Type 2 Sightings', alpha=0.6)

# Smooth fitting using spline interpolation for both groups
x_smooth = np.linspace(voyages.min(), voyages.max(), 300)
spline1 = make_interp_spline(voyages, sightings, k=3)  # Cubic spline
y_smooth1 = spline1(x_smooth)
spline2 = make_interp_spline(voyages, sightings_type2, k=3)
y_smooth2 = spline2(x_smooth)

# Plot the smooth fitting curve for both groups
plt.plot(x_smooth, y_smooth1, color='green', linestyle='--', linewidth=2, label='Trend Line Type 1')
plt.plot(x_smooth, y_smooth2, color='orange', linestyle='-', linewidth=2, label='Trend Line Type 2')

# Annotate periods, carefully handling overlap
for i, label in enumerate(period_labels):
    plt.annotate(label, (voyages[i], sightings[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, rotation=45)

# Title and labels
plt.title("Voyages of Discovery and Sea Monsters\nA Comprehensive Historical Perspective", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Voyage/Period Index", fontsize=12)
plt.ylabel("Sea Monster Sightings", fontsize=12)

# Legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()