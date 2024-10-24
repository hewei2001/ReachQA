import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2000, 2026)
solar = np.array([10, 12, 15, 18, 22, 28, 35, 45, 60, 80, 105, 135, 180, 240, 320, 420, 550, 700, 880, 1090, 1300, 1550, 1850, 2200, 2600, 3000])
wind = np.array([30, 40, 55, 70, 90, 120, 155, 200, 260, 340, 450, 590, 770, 1000, 1300, 1600, 1950, 2350, 2800, 3300, 3850, 4500, 5200, 6000, 7000, 8100])
hydro = np.array([800, 810, 825, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280])
biomass = np.array([50, 55, 65, 75, 90, 110, 135, 165, 200, 240, 290, 350, 420, 500, 600, 720, 860, 1010, 1180, 1370, 1590, 1840, 2130, 2460, 2840, 3300])

# Creating the main plot
fig, ax = plt.subplots(figsize=(16, 9))

# Enhanced stacked area plot
ax.stackplot(years, solar, wind, hydro, biomass,
             labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
             colors=['#FDB813', '#0077B6', '#0A9396', '#EE9B00'],
             alpha=0.85)

# Adding annotations for key changes
ax.annotate('Solar & Wind Rapid Growth', xy=(2010, 1050), xytext=(2005, 5000),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, color='grey')

# Trend lines
for i, source in enumerate([solar, wind, hydro, biomass]):
    z = np.polyfit(years, source, 3)
    p = np.poly1d(z)
    ax.plot(years, p(years), linestyle='--', linewidth=1.5)

# Titles and labels
ax.set_title('Evolution of Renewable Energy Sources\nfrom 2000 to 2025', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Adjusted ticks for clarity
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 16001, 2000))

# Dynamic legend
ax.legend(loc='upper left', fontsize=10)

# Grid and formatting enhancements
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(2000, 2025)
ax.set_ylim(0, 16000)

# Adding a secondary inset for detailed view
inset_ax = fig.add_axes([0.15, 0.55, 0.3, 0.3])  # Position: x, y, width, height
inset_ax.stackplot(years[-5:], solar[-5:], wind[-5:], hydro[-5:], biomass[-5:], colors=['#FDB813', '#0077B6', '#0A9396', '#EE9B00'], alpha=0.85)
inset_ax.set_title('Detailed View: 2020-2025', fontsize=10)
inset_ax.set_xticks(years[-5:])
inset_ax.set_yticks(np.arange(0, 16001, 4000))
inset_ax.grid(True, linestyle='--', alpha=0.5)

# Layout adjustment
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Show plot
plt.show()