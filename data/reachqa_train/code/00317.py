import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for plotting
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020])
countries_adopting = np.array([5, 8, 12, 15, 20, 28, 35, 45, 55, 70, 90])
renewable_consumption = np.array([2, 4, 5, 7, 10, 15, 22, 30, 40, 60, 85])

# Smooth line setup
x_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, renewable_consumption, k=3)
y_smooth = spl(x_smooth)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter points with color gradient
scatter = ax1.scatter(
    years, renewable_consumption, c=countries_adopting, cmap='viridis',
    s=100, alpha=0.8, edgecolors='black', label='Consumption Data'
)

# Smooth fitting curve
fit_curve = ax1.plot(
    x_smooth, y_smooth, color='darkorange', linestyle='-', linewidth=2.5, 
    label='Consumption Trend'
)

# Secondary Y-axis
ax2 = ax1.twinx()
ax2.plot(years, countries_adopting, color='steelblue', linestyle='--', linewidth=2, marker='o', markersize=7, label='Countries Adopting')

# Annotations
for i, txt in enumerate(countries_adopting):
    ax1.annotate(f"{txt} countries", (years[i], renewable_consumption[i]), textcoords="offset points", xytext=(-5,10), ha='center', fontsize=9)

# Titles and labels
ax1.set_title(
    "The Evolution of Renewable Energy Adoption\n"
    "Impact of Policies on Global Consumption (2000-2020)", 
    fontsize=16, fontweight='bold', color='navy'
)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Renewable Energy Consumption (Exajoules)", fontsize=12, color='darkgreen')
ax2.set_ylabel("Countries Adopting Policies", fontsize=12, color='steelblue')
ax1.set_xlim(years.min() - 1, years.max() + 1)
ax1.set_ylim(0, max(renewable_consumption) + 10)
ax2.set_ylim(0, max(countries_adopting) + 10)

# Background shading
ax1.axvspan(2000, 2010, color='lightgrey', alpha=0.3, label='Early Adoption Phase')
ax1.axvspan(2010, 2020, color='lightyellow', alpha=0.3, label='Rapid Growth Phase')

# Grid and legend
ax1.grid(True, linestyle='--', alpha=0.6)
fig.colorbar(scatter, ax=ax1, label='Number of Countries Adopting Policies')
ax1.legend(loc="upper left", frameon=False, fontsize=11)
ax2.legend(loc="upper right", frameon=False, fontsize=11)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()