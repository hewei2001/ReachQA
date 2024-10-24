import matplotlib.pyplot as plt
import numpy as np

# Define the decades and corresponding data for Average SST
decades = np.array([1980, 1990, 2000, 2010, 2020, 2030])
average_sst = np.array([15.5, 15.7, 15.9, 16.0, 16.2, 16.4])  # Average SST in degrees Celsius
uncertainty = np.array([0.1, 0.12, 0.11, 0.13, 0.15, 0.14])  # Measurement uncertainties

# Construct a related dataset for SST anomaly (difference from 1980 baseline)
baseline_sst = 15.5  # Baseline SST in 1980
sst_anomaly = average_sst - baseline_sst

# Initialize a figure with 1 row and 2 columns for subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: Line chart with error bars for Average SST
axs[0].errorbar(decades, average_sst, yerr=uncertainty, fmt='-o', ecolor='skyblue', capsize=5,
                capthick=2, color='darkorange', alpha=0.9, marker='s', markersize=7)
axs[0].grid(True, linestyle='--', alpha=0.7)
axs[0].set_title("Decadal Trends in Global SST\nand Associated Uncertainty (1980-2030)",
                 fontsize=12, fontweight='bold', pad=15)
axs[0].set_xlabel("Decade", fontsize=11)
axs[0].set_ylabel("Average SST (°C)", fontsize=11)
axs[0].set_xlim(1975, 2035)
axs[0].set_ylim(15.0, 17.0)

# Subplot 2: Bar chart for SST Anomaly
axs[1].bar(decades, sst_anomaly, color='teal', width=8)
axs[1].set_title("Sea Surface Temperature Anomaly\nfrom 1980 Baseline (1980-2030)",
                 fontsize=12, fontweight='bold', pad=15)
axs[1].set_xlabel("Decade", fontsize=11)
axs[1].set_ylabel("SST Anomaly (°C)", fontsize=11)
axs[1].axhline(0, color='grey', linewidth=0.8, linestyle='--')  # Baseline for anomaly

# Shared legend at the bottom of the plots
fig.legend(["Average SST with Uncertainty", "SST Anomaly"], loc='lower center', ncol=2, fontsize=11, frameon=False)

# Optimize layout
plt.tight_layout(rect=[0, 0.05, 1, 1])

# Display the plots
plt.show()