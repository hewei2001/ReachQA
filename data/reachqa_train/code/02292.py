import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import make_interp_spline

# Define the fictional dataset
distances = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                      120, 140, 160, 180, 200, 220, 240, 260, 280, 300])

# Hypothetical apparent brightness values
brightness = 10000 / distances**2
brightness += np.array([200, 150, -100, 50, -150, 100, -50, 150, 0, -100,
                        200, -150, 100, -200, 50, 150, -100, 200, -50, 100])

# Define the model function for fitting
def model_func(d, a):
    return a / d**2

# Fit the model to the data
popt, _ = curve_fit(model_func, distances, brightness)

# Create smooth curve data
x_smooth = np.linspace(min(distances), max(distances), 300)
y_smooth = make_interp_spline(distances, brightness, k=3)(x_smooth)

# Plotting
plt.figure(figsize=(14, 8))

# Scatter plot for data points
plt.scatter(distances, brightness, color='dodgerblue', label='Observed Brightness', edgecolors='black', s=100, alpha=0.7)

# Smooth fitting curve
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2, linestyle='--', label='Smooth Fitting Curve')

# Set title and labels
plt.title('Brightness vs. Distance:\nInsights from Two Decades of Astronomical Observations (2000-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Distance from Earth (Light-years)', fontsize=14)
plt.ylabel('Apparent Brightness (arbitrary units)', fontsize=14)

# Adjust plot details
plt.grid(True, which='major', linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=12)

# Highlight specific observations
highlight_distances = [50, 150, 250]
highlight_labels = ['Betelgeuse', 'Sirius', 'Andromeda']
for d, label in zip(highlight_distances, highlight_labels):
    if d in distances:
        index = np.where(distances == d)[0][0]
        plt.annotate(label, (d, brightness[index]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10,
                     arrowprops=dict(arrowstyle='->', color='gray'))

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()