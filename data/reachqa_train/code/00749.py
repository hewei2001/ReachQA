import matplotlib.pyplot as plt
import numpy as np

# Decades and corresponding temperature anomalies (in °C) with uncertainties
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
temperature_anomalies = np.array([-0.1, 0.05, 0.1, 0.2, 0.35, 0.55, 0.7])
uncertainties = np.array([0.05, 0.04, 0.06, 0.05, 0.03, 0.02, 0.02])

# Setting up the plot
plt.figure(figsize=(10, 6))
plt.errorbar(decades, temperature_anomalies, yerr=uncertainties, fmt='-o', ecolor='r', capsize=5, capthick=2, 
             color='b', linestyle='-', linewidth=2, markersize=8, markerfacecolor='orange', markeredgecolor='k')

# Customization for better presentation
plt.title('Global Temperature Anomalies Over Decades\n(1960-2020)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.ylim(-0.2, 0.8)

# Adding a grid for ease of reading
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Annotation highlighting the significant trend in recent years
plt.annotate('Notable Increase in Recent Decades', xy=(2005, 0.6), xytext=(1990, 0.4),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.3"), fontsize=10)

# Legend to describe the plot elements
plt.legend(['Temperature Anomalies'], loc='upper left', fontsize=10)

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()

# Displaying the plot
plt.show()