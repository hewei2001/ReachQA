import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years for which data is collected
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020])

# Brightness data for each celestial object (in lumens)
brightness_star_a = np.array([20, 22, 23, 21, 24, 22, 25, 26, 24, 25, 24])
brightness_galaxy_b = np.array([15, 16, 18, 20, 19, 22, 21, 23, 24, 22, 25])
brightness_quasar_c = np.array([30, 28, 35, 30, 33, 37, 34, 36, 38, 40, 39])

# Function to create a smoother representation for each set of data using interpolation
def smooth_curve(x, y):
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)
    return X_, Y_

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Scatter plot with smooth fitting lines for each celestial object
for brightness, label, color in zip(
    [brightness_star_a, brightness_galaxy_b, brightness_quasar_c],
    ["Star A", "Galaxy B", "Quasar C"],
    ['#FF6347', '#4682B4', '#32CD32']
):
    # Plot the scatter points
    ax.scatter(years, brightness, label=label, color=color, alpha=0.7, edgecolor='black', s=100)

    # Calculate and plot the smooth fitting line
    x_smooth, y_smooth = smooth_curve(years, brightness)
    ax.plot(x_smooth, y_smooth, color=color, alpha=0.9, linewidth=2, linestyle='--')

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Brightness (lumens)', fontsize=12)
ax.set_title('Cosmic Discoveries: Brightness Variations\nof Celestial Objects (2000-2020)', 
             fontsize=14, fontweight='bold')

# Add grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title="Celestial Objects", loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()