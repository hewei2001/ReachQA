import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2025
years = np.arange(2000, 2026)

# Hypothetical data for renewable energy production in TWh
solar = np.array([10, 12, 15, 18, 22, 28, 35, 45, 60, 80, 105, 135, 180, 240, 320, 420, 550, 700, 880, 1090, 1300, 1550, 1850, 2200, 2600, 3000])
wind = np.array([30, 40, 55, 70, 90, 120, 155, 200, 260, 340, 450, 590, 770, 1000, 1300, 1600, 1950, 2350, 2800, 3300, 3850, 4500, 5200, 6000, 7000, 8100])
hydro = np.array([800, 810, 825, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280])
biomass = np.array([50, 55, 65, 75, 90, 110, 135, 165, 200, 240, 290, 350, 420, 500, 600, 720, 860, 1010, 1180, 1370, 1590, 1840, 2130, 2460, 2840, 3300])

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Create a stacked area plot
ax.stackplot(years, solar, wind, hydro, biomass, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=['#ffcc00', '#66c2ff', '#33cc33', '#996633'], alpha=0.8)

# Titles and labels
ax.set_title('Evolution of Renewable Energy Sources\nfrom 2000 to 2025', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Customize the x-axis ticks for better readability
plt.xticks(years[::2], rotation=45)

# Add legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(2000, 2025)
ax.set_ylim(0, 16000)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show plot
plt.show()