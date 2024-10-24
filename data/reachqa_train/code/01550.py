import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding communication efficiencies
years = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
efficiency = np.array([62, 65, 68, 70, 74, 78, 76, 79, 82, 85, 89])

# Generate a smooth curve using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)
efficiency_spline = make_interp_spline(years, efficiency, k=3)(years_smooth)

# Plotting
plt.figure(figsize=(12, 6))
plt.scatter(years, efficiency, color='orange', s=100, edgecolors='k', label='Measured Efficiency')
plt.plot(years_smooth, efficiency_spline, 'b-', linewidth=2, label='Smooth Trend')

# Customize the chart
plt.title('Interplanetary Communication Efficiency Over Time\nMars-to-Earth Signals', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Communication Efficiency (%)', fontsize=12)
plt.xticks(years)
plt.yticks(np.arange(60, 100, 5))
plt.grid(True, linestyle='--', alpha=0.7)

# Annotate a key improvement
plt.annotate('Significant Improvement', xy=(2025, 78), xytext=(2022, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.2"), fontsize=10)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()