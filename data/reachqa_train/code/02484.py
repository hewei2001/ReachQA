import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define years and influence scores for each art style with more detail
years = np.arange(1910, 2005, 5)
cubism_influence = np.array([80, 90, 75, 60, 20, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
surrealism_influence = np.array([0, 0, 20, 60, 80, 90, 60, 30, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0])
abstract_influence = np.array([0, 0, 0, 20, 50, 80, 90, 70, 50, 20, 10, 5, 0, 0, 0, 0, 0, 0, 0])
popart_influence = np.array([0, 0, 0, 0, 0, 0, 20, 60, 80, 90, 70, 50, 0, 0, 0, 0, 0, 0, 0])
contemporary_influence = np.array([0, 0, 0, 0, 0, 10, 40, 60, 80, 90, 95, 100, 95, 90, 85, 80, 75, 70, 65])
dadaism_influence = np.array([0, 20, 50, 70, 50, 20, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Function to define a smooth curve (Gaussian fitting example)
def smooth_curve(x, a, b, c):
    return a * np.exp(-0.5 * ((x - b) / c) ** 2)

# Plotting
plt.figure(figsize=(16, 10))

# Scatter plot for each style
plt.scatter(years, cubism_influence, label='Cubism', color='blue', alpha=0.6)
plt.scatter(years, surrealism_influence, label='Surrealism', color='orange', alpha=0.6)
plt.scatter(years, abstract_influence, label='Abstract Art', color='green', alpha=0.6)
plt.scatter(years, popart_influence, label='Pop Art', color='red', alpha=0.6)
plt.scatter(years, contemporary_influence, label='Contemporary Art', color='purple', alpha=0.6)
plt.scatter(years, dadaism_influence, label='Dadaism', color='cyan', alpha=0.6)

# Curve fitting for smooth lines
params_cubism, _ = curve_fit(smooth_curve, years, cubism_influence, p0=[90, 1920, 10])
params_surrealism, _ = curve_fit(smooth_curve, years, surrealism_influence, p0=[90, 1940, 15])
params_abstract, _ = curve_fit(smooth_curve, years, abstract_influence, p0=[90, 1960, 15])
params_popart, _ = curve_fit(smooth_curve, years, popart_influence, p0=[90, 1975, 10])
params_contemporary, _ = curve_fit(smooth_curve, years, contemporary_influence, p0=[100, 1990, 15])
params_dadaism, _ = curve_fit(smooth_curve, years, dadaism_influence, p0=[70, 1930, 15])

# Create smooth lines
years_fine = np.linspace(1900, 2020, 500)
plt.plot(years_fine, smooth_curve(years_fine, *params_cubism), color='blue', linestyle='--', linewidth=1)
plt.plot(years_fine, smooth_curve(years_fine, *params_surrealism), color='orange', linestyle='--', linewidth=1)
plt.plot(years_fine, smooth_curve(years_fine, *params_abstract), color='green', linestyle='--', linewidth=1)
plt.plot(years_fine, smooth_curve(years_fine, *params_popart), color='red', linestyle='--', linewidth=1)
plt.plot(years_fine, smooth_curve(years_fine, *params_contemporary), color='purple', linestyle='--', linewidth=1)
plt.plot(years_fine, smooth_curve(years_fine, *params_dadaism), color='cyan', linestyle='--', linewidth=1)

# Customize plot
plt.title('The Evolution of Art Styles\nand Their Influence Over Time (1910-2000)', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Influence Score', fontsize=14)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Annotate key points
for (year, influence) in zip(years, contemporary_influence):
    if influence == max(contemporary_influence):
        plt.annotate(f'Peak {influence}', xy=(year, influence), xytext=(year+5, influence+10),
                     arrowprops=dict(arrowstyle='->', color='purple'))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()