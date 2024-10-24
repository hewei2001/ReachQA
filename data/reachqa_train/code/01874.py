import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(1990, 2021)

# Global ice cream sales data (billion USD)
ice_cream_sales = np.array([
    10, 10.5, 11, 11.2, 11.8, 12.3, 13, 13.5, 14, 14.2, 
    15, 15.5, 16, 16.8, 17.3, 18, 18.5, 19, 19.7, 20, 
    20.5, 21, 21.5, 22, 22.3, 22.8, 23.5, 24, 24.5, 25, 
    25.5
])

# Hypothetical global temperature anomalies (degrees Celsius)
temperature_anomalies = np.array([
    0.20, 0.25, 0.22, 0.30, 0.35, 0.40, 0.38, 0.42, 0.45, 0.48, 
    0.50, 0.55, 0.60, 0.62, 0.68, 0.70, 0.72, 0.78, 0.80, 0.85, 
    0.90, 0.95, 1.00, 1.05, 1.10, 1.12, 1.15, 1.18, 1.20, 1.22, 
    1.25
])

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('Impact of Climate Change on Ice Cream Sales and Temperature Anomalies\n(1990-2020)', fontsize=16)

# First subplot - Ice Cream Sales
axs[0].plot(years, ice_cream_sales, color='orange', marker='o', linestyle='-', linewidth=2, markersize=6, label='Ice Cream Sales (Billion USD)')
axs[0].set_title('Global Ice Cream Sales', fontsize=14)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Sales (Billion USD)', fontsize=12)
axs[0].set_xticks(years[::2])
axs[0].set_xticklabels(years[::2], rotation=45)
axs[0].set_yticks(np.arange(10, 26, 2))
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(loc='upper left', fontsize=10)

highlight_indices = [0, 10, 20, 30]
for i in highlight_indices:
    axs[0].annotate(
        f'{ice_cream_sales[i]:.1f} B USD',
        (years[i], ice_cream_sales[i]),
        textcoords="offset points",
        xytext=(-5, 10),
        ha='center',
        fontsize=10,
        color='blue',
        bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightgray', alpha=0.5)
    )

# Second subplot - Temperature Anomalies
axs[1].bar(years, temperature_anomalies, color='cyan', edgecolor='black')
axs[1].set_title('Global Temperature Anomalies', fontsize=14)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Temperature Anomaly (°C)', fontsize=12)
axs[1].set_xticks(years[::2])
axs[1].set_xticklabels(years[::2], rotation=45)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plots
plt.show()