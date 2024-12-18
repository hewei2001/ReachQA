import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the years from 2020 to 2050
years = np.arange(2020, 2051)

# Hypothetical efficiency data for each energy source (in percentage)
fusion_efficiency = np.array([40, 42, 45, 48, 52, 56, 60, 63, 66, 70, 73, 76, 78, 80, 82, 84, 86, 88, 89, 90, 91, 92, 93, 94, 94, 95, 96, 96, 97, 97, 98])
solar_efficiency = np.array([20, 21, 23, 26, 30, 34, 39, 44, 50, 55, 60, 65, 68, 71, 74, 76, 78, 80, 82, 84, 85, 86, 87, 88, 89, 89, 90, 90, 91, 91, 92])
wind_efficiency = np.array([30, 32, 34, 36, 39, 42, 45, 48, 50, 53, 56, 59, 61, 63, 65, 67, 68, 69, 70, 71, 72, 72, 73, 73, 74, 74, 75, 75, 76, 76, 77])
geothermal_efficiency = np.array([25, 26, 28, 30, 32, 34, 37, 40, 43, 45, 47, 49, 51, 53, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 66, 67, 67, 68, 68, 69])

# Define the polynomial fitting function
def poly_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33F0']
energy_sources = ['Fusion', 'Solar', 'Wind', 'Geothermal']
efficiencies = [fusion_efficiency, solar_efficiency, wind_efficiency, geothermal_efficiency]

for i, (color, source, efficiency) in enumerate(zip(colors, energy_sources, efficiencies)):
    ax.scatter(years, efficiency, color=color, label=f'{source} Efficiency', alpha=0.6)
    params, _ = curve_fit(poly_fit, years, efficiency)
    fitted_efficiency = poly_fit(years, *params)
    ax.plot(years, fitted_efficiency, color=color, linestyle='--', linewidth=2)

    # Add annotations for key years
    for year, eff in zip([2025, 2035, 2045], efficiency[[5, 15, 25]]):
        ax.annotate(f'{eff}%', xy=(year, eff), xytext=(year, eff+5),
                    arrowprops=dict(facecolor=color, shrink=0.05), fontsize=10)

# Titles and labels
ax.set_title("Projected Efficiency of Future Energy Sources (2020-2050)\nFusion, Solar, Wind, and Geothermal", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Efficiency (%)", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)

# Set limits
ax.set_xlim(2020, 2050)
ax.set_ylim(15, 100)

# Add a legend
ax.legend(loc='upper left', fontsize=12)

# Highlight specific periods
ax.axvspan(2030, 2040, color='gray', alpha=0.1, label='Decade of Focus')

# Add a text box with summary insights
ax.text(2048, 30, "Key Insights:\nEfficiency growth noticeable\nSignificant changes around 2040",
        fontsize=10, va='center', ha='right', bbox=dict(facecolor='white', alpha=0.6))

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()