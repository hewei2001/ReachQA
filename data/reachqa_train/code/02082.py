import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the extended years and corresponding average travel speeds (in km/h)
years = np.array([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 
                  2020, 2022, 2024, 2026, 2028, 2030, 2032, 2034, 2036, 2038, 2040])
travel_speeds = np.array([800, 820, 840, 860, 880, 1000, 1500, 3000, 4000, 4500, 
                          5000, 7500, 11000, 15000, 20000, 25000, 30000, 40000, 60000, 80000, 100000])

# Add a comparative series for cost of teleportation development (hypothetical units)
costs = np.array([500, 480, 470, 460, 450, 430, 400, 370, 340, 300, 
                  250, 230, 220, 210, 200, 190, 180, 175, 170, 165, 160])

# Smooth curve fitting
years_smooth = np.linspace(years.min(), years.max(), 500)
spl = make_interp_spline(years, travel_speeds, k=3)
travel_speeds_smooth = spl(years_smooth)

plt.figure(figsize=(14, 10))

# Subplot for Travel Speeds
ax1 = plt.subplot(211)
ax1.scatter(years, travel_speeds, color='purple', s=100, alpha=0.7, label='Travel Speed Data')
ax1.plot(years_smooth, travel_speeds_smooth, color='blue', linestyle='-', linewidth=2.5, label='Smooth Fitting Curve')

ax1.set_title("Evolution of Teleportation Technology\nImpact on Travel Speed in Technotopia (2000-2040)", 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Average Travel Speed (km/h)", fontsize=12)
ax1.set_yscale('log')  # Logarithmic scale

milestones = {
    2010: '1st Commercial Teleporter',
    2025: 'Quantum Leap Teleporters',
    2035: 'Instant Transport Network'
}

for year, event in milestones.items():
    idx = (np.abs(years - year)).argmin()  # Find the index of the closest year
    travel_speed = travel_speeds[idx]  # Use the speed at that closest year
    ax1.annotate(event, xy=(years[idx], travel_speed), 
                 xytext=(years[idx] - 3, travel_speed * 1.5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')

ax1.grid(linestyle='--', linewidth=0.7, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)

# Subplot for Costs
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(years, costs, color='green', linestyle='-', linewidth=2.5, label='Cost of Teleportation Development')
ax2.set_title("Costs of Teleportation Development (2000-2040)", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Cost (Hypothetical Units)", fontsize=12)
ax2.set_ylim(0, 600)
ax2.grid(linestyle=':', linewidth=0.5, alpha=0.5)
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()