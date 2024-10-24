import matplotlib.pyplot as plt
import numpy as np

# Original data
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
temperature_anomalies = np.array([-0.1, 0.05, 0.1, 0.2, 0.35, 0.55, 0.7])
uncertainties = np.array([0.05, 0.04, 0.06, 0.05, 0.03, 0.02, 0.02])

# New related data: number of climate-related events per decade
climate_events = np.array([10, 15, 20, 25, 35, 50, 70])

fig, ax1 = plt.subplots(figsize=(12, 7))

# Primary plot: Temperature Anomalies
ax1.errorbar(decades, temperature_anomalies, yerr=uncertainties, fmt='-o', color='b', 
             ecolor='r', capsize=5, capthick=2, linestyle='-', linewidth=2, 
             markersize=8, markerfacecolor='orange', markeredgecolor='k', label='Temp Anomalies')
ax1.set_title('Global Temperature Anomalies and Climate Events\n(1960-2020)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Temperature Anomaly (°C)', fontsize=12)
ax1.set_ylim(-0.2, 0.8)
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.annotate('Notable Increase in Recent Decades', xy=(2005, 0.6), xytext=(1990, 0.4),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.3"), fontsize=10)

# Secondary plot: Climate Events
ax2 = ax1.twinx()
ax2.bar(decades, climate_events, color='green', alpha=0.5, width=5, label='Climate Events')
ax2.set_ylabel('Number of Climate Events', fontsize=12)
ax2.set_ylim(0, 80)
ax2.legend(loc='upper right', fontsize=10)

# Trendline for Temperature Anomalies
z = np.polyfit(decades, temperature_anomalies, 1)
p = np.poly1d(z)
ax1.plot(decades, p(decades), "r--", linewidth=1.5, label='Trendline')

# Adjust layout
fig.tight_layout()

plt.show()