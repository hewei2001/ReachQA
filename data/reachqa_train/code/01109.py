import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data definition
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020])
brightness_star_a = np.array([20, 22, 23, 21, 24, 22, 25, 26, 24, 25, 24])
brightness_galaxy_b = np.array([15, 16, 18, 20, 19, 22, 21, 23, 24, 22, 25])
brightness_quasar_c = np.array([30, 28, 35, 30, 33, 37, 34, 36, 38, 40, 39])

# Hypothetical energy data (in megajoules)
energy_star_a = np.array([500, 520, 530, 515, 540, 530, 550, 560, 545, 555, 550])
energy_galaxy_b = np.array([400, 410, 430, 445, 435, 470, 460, 485, 495, 470, 490])
energy_quasar_c = np.array([600, 590, 630, 605, 615, 640, 625, 635, 660, 670, 655])

# Smooth curve function
def smooth_curve(x, y):
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)
    return X_, Y_

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot with smooth lines
for brightness, label, color in zip(
    [brightness_star_a, brightness_galaxy_b, brightness_quasar_c],
    ["Star A", "Galaxy B", "Quasar C"],
    ['#FF6347', '#4682B4', '#32CD32']
):
    ax1.scatter(years, brightness, label=f"Brightness {label}", color=color, alpha=0.7, edgecolor='black', s=100)
    x_smooth, y_smooth = smooth_curve(years, brightness)
    ax1.plot(x_smooth, y_smooth, color=color, alpha=0.9, linewidth=2, linestyle='--')

# Secondary Y-axis for energy
ax2 = ax1.twinx()
ax2.set_ylabel('Energy (Megajoules)', fontsize=12, color='#8B008B')

# Bar plot for energy
bar_width = 0.5
for energy, label, hatch, color in zip(
    [energy_star_a, energy_galaxy_b, energy_quasar_c],
    ["Star A", "Galaxy B", "Quasar C"],
    ['/', '\\', '|'],
    ['#FF69B4', '#00CED1', '#8A2BE2']
):
    ax2.bar(years - bar_width/3, energy, bar_width, label=f"Energy {label}", alpha=0.6, hatch=hatch, color=color)

# Titles and labels
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Brightness (Lumens)', fontsize=12)
ax1.set_title('Cosmic Discoveries: Brightness and Energy Variations\nof Celestial Objects (2000-2020)', 
              fontsize=16, fontweight='bold')

# Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.12, 0.85), title="Data Sources", fontsize=10)

# Grid and layout
ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()