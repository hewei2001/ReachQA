import matplotlib.pyplot as plt
import numpy as np

# Contextual Data Inputs
years = np.arange(2000, 2021)

# Original Data: Temperature Anomalies
# Extend temperature_anomalies to match the length of years
temperature_anomalies = np.array([0.5, 0.7, 0.5, 0.9, 1.2, 1.1, 1.3, 1.5, 1.6, 1.8, 1.9, 2.1, 2.0, 2.2, 2.3, 2.4, 2.3, 2.4, 2.5, 2.55, 2.6]) # Adding 2.55 and 2.6 for 2019 and 2020
uncertainty = np.random.normal(0, 0.2, temperature_anomalies.shape)

# Make sure the uncertainty values are non-negative for errorbar
uncertainty = np.abs(uncertainty)

# New Data: Ice Extent (Millions of Square Kilometers)
# Extend ice_extent to match the length of years
ice_extent = np.array([12.5, 11.7, 11.8, 11.3, 10.8, 10.6, 10.5, 9.7, 9.5, 9.3, 9.2, 8.8, 8.9, 8.5, 8.4, 8.2, 8.1, 7.8, 7.7, 7.6, 7.5]) # Adding 7.6 and 7.5 for 2019 and 2020

# Plot setup
plt.figure(figsize=(16, 7))

# Subplot for temperature anomalies
plt.subplot(1, 2, 1)
plt.title('Evolution of Temperature Trends in the Arctic Region\n(2000-2020)', fontsize=14)
plt.plot(years, temperature_anomalies, color='tab:blue', linewidth=2, marker='o', label='Average Temperature Anomalies')
plt.errorbar(years, temperature_anomalies, yerr=uncertainty, fmt='none', ecolor='lightgray', capsize=5, alpha=0.6)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.legend(framealpha=0.9)

# Highlight significant years with annotations for temperature anomalies
for i, temp in enumerate(temperature_anomalies):
    if i in [0, 5, 10, 15, len(temperature_anomalies)-1]:
        plt.text(years[i], temp + 0.1, f'{temp:.1f}°C', color='red', ha='center')

# Subplot for ice extent
plt.subplot(1, 2, 2)
plt.title('Arctic Ice Extent over Time\n(2000-2020)', fontsize=14)
plt.plot(years, ice_extent, color='tab:green', linewidth=2, marker='o', label='Ice Extent')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Extent (Million km²)', fontsize=12)
plt.legend(framealpha=0.9)

# Adjust the layout to avoid label overlaps
plt.tight_layout()

# Display the plot
plt.show()