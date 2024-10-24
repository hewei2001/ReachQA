import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define years from 2013 to 2022
years = np.arange(2013, 2023)

# Migration distances for each species in kilometers
arctic_tern_migration = [15000, 16000, 15800, 16200, 16700, 17000, 17500, 17200, 17800, 18000]
monarch_butterfly_migration = [3800, 3600, 3900, 3700, 4000, 4100, 4200, 4150, 4300, 4400]
swallow_migration = [8000, 8200, 8100, 8300, 8500, 8600, 8800, 8700, 8900, 9100]

# Fit polynomial trend lines (second-degree polynomial)
def poly_fit(x, a, b, c):
    return a * x**2 + b * x + c

tern_params, _ = curve_fit(poly_fit, years, arctic_tern_migration)
monarch_params, _ = curve_fit(poly_fit, years, monarch_butterfly_migration)
swallow_params, _ = curve_fit(poly_fit, years, swallow_migration)

# Create a denser range for smoother trend line
dense_years = np.linspace(2013, 2022, 300)

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each species' migration with unique styles
ax.plot(years, arctic_tern_migration, label='Arctic Tern', color='navy', linewidth=2, marker='o', linestyle='-')
ax.plot(years, monarch_butterfly_migration, label='Monarch Butterfly', color='orange', linewidth=2, marker='s', linestyle='--')
ax.plot(years, swallow_migration, label='Swallow', color='green', linewidth=2, marker='^', linestyle='-.')

# Plot trend lines
ax.plot(dense_years, poly_fit(dense_years, *tern_params), color='navy', linestyle='-', linewidth=1, alpha=0.5)
ax.plot(dense_years, poly_fit(dense_years, *monarch_params), color='orange', linestyle='--', linewidth=1, alpha=0.5)
ax.plot(dense_years, poly_fit(dense_years, *swallow_params), color='green', linestyle='-.', linewidth=1, alpha=0.5)

# Customize the chart
ax.set_title('Migration Patterns of Selected Species Over a Decade\n(2013-2022)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Migration Distance (km)', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(title='Species', fontsize=12, title_fontsize='13', loc='upper left')
ax.set_xlim([2013, 2022])
ax.set_ylim([3000, 19000])
ax.tick_params(axis='x', rotation=45)

# Annotate significant points
ax.annotate('Longest Distance', xy=(2022, 18000), xytext=(2018, 18500),
            arrowprops=dict(arrowstyle='->', color='navy'), fontsize=12, color='navy', ha='center')
ax.annotate('Steady Increase', xy=(2022, 4400), xytext=(2015, 5000),
            arrowprops=dict(arrowstyle='->', color='orange'), fontsize=12, color='orange', ha='center')
ax.annotate('Consistent Growth', xy=(2022, 9100), xytext=(2016, 9500),
            arrowprops=dict(arrowstyle='->', color='green'), fontsize=12, color='green', ha='center')

# Enhance interaction with mplcursors (requires mplcursors library)
try:
    import mplcursors
    mplcursors.cursor(ax, hover=True)
except ImportError:
    pass  # Only enable interactive cursor if mplcursors is available

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()