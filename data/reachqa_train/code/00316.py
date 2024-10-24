import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years of observation (2000 - 2020)
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020])

# Number of countries adopting renewable energy policies in corresponding years
countries_adopting = np.array([5, 8, 12, 15, 20, 28, 35, 45, 55, 70, 90])

# Corresponding increase in global renewable energy consumption (in exajoules)
renewable_consumption = np.array([2, 4, 5, 7, 10, 15, 22, 30, 40, 60, 85])

# Create a smooth line for fitting the scatter data
x_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, renewable_consumption, k=3)
y_smooth = spl(x_smooth)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot scatter points
scatter = ax.scatter(years, renewable_consumption, color='forestgreen', s=100, alpha=0.7, edgecolors='black', label='Observed Data')

# Plot smooth fitting curve
fit_curve = ax.plot(x_smooth, y_smooth, color='darkorange', linestyle='-', linewidth=2.5, label='Trend Line')

# Add annotations
for i, txt in enumerate(countries_adopting):
    ax.annotate(f"{txt} countries", (years[i], renewable_consumption[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Titles and labels
ax.set_title("The Evolution of Renewable Energy Adoption\nImpact of Policies on Global Consumption (2000-2020)", fontsize=16, fontweight='bold', color='navy')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Renewable Energy Consumption (Exajoules)", fontsize=12)
ax.set_xlim(years.min() - 1, years.max() + 1)
ax.set_ylim(0, max(renewable_consumption) + 10)
ax.grid(True, linestyle='--', alpha=0.6)

# Legend
ax.legend(loc="upper left", frameon=False, fontsize=11)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()