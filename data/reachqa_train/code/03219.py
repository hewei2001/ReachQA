import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define data for voyages and corresponding sea monster sightings
voyages = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sightings = np.array([5, 7, 6, 10, 13, 15, 12, 18, 20, 22])

# Define labels for the periods of discovery
period_labels = [
    "Ancient", "Early Middle Ages", "Viking Age", "Late Middle Ages",
    "Age of Discovery", "Golden Age of Piracy", "Enlightenment",
    "Industrial Revolution", "Modern Exploration", "Digital Age Mapping"
]

# Scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(voyages, sightings, color='darkblue', edgecolor='black', s=100, label='Sightings per Period')

# Smooth fitting using spline interpolation
x_smooth = np.linspace(voyages.min(), voyages.max(), 300)
spline = make_interp_spline(voyages, sightings, k=3)  # Cubic spline
y_smooth = spline(x_smooth)

# Plot the smooth fitting curve
plt.plot(x_smooth, y_smooth, color='green', linestyle='--', linewidth=2, label='Trend Line (Spline Fit)')

# Annotate periods
for i, label in enumerate(period_labels):
    plt.annotate(label, (voyages[i], sightings[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Title and labels
plt.title("Voyages of Discovery and Sea Monsters\nA Historical Sightings Perspective", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Voyage/Period Index", fontsize=12)
plt.ylabel("Sea Monster Sightings", fontsize=12)

# Legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()