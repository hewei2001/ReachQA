import matplotlib.pyplot as plt
import numpy as np

# Decades and average global surface temperatures (in °C)
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
avg_temps = np.array([13.6, 14.0, 14.2, 14.4, 14.6, 14.8, 15.1])
# Variability in temperature as standard deviation
temp_variability = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4])

# Temperature anomalies (°C from baseline)
temp_anomalies = np.array([-0.2, 0.0, 0.1, 0.15, 0.3, 0.5, 0.6])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plotting line chart with error bars for average temperatures
ax1.errorbar(
    decades, avg_temps, yerr=temp_variability, fmt='o-', color='darkorange',
    ecolor='gray', elinewidth=2, capsize=5, alpha=0.8, label='Avg Temp ± Variability'
)

# Customize axis for average temperatures
ax1.set_title('Average Global Surface Temperatures & Anomalies (1960-2020)\nWith Variability Indicated', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Avg Temperature (°C)', fontsize=12, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')

# Add a secondary y-axis for temperature anomalies
ax2 = ax1.twinx()
ax2.bar(decades, temp_anomalies, width=8, color='lightblue', alpha=0.6, label='Temperature Anomalies')
ax2.set_ylabel('Temperature Anomalies (°C)', fontsize=12, color='lightblue')
ax2.tick_params(axis='y', labelcolor='lightblue')

# Add annotations for each average temperature point
for i in range(len(decades)):
    ax1.annotate(
        f'{avg_temps[i]:.1f}°C ± {temp_variability[i]:.1f}',
        (decades[i], avg_temps[i]),
        textcoords="offset points",
        xytext=(-10, 10),
        ha='center',
        fontsize=9,
        arrowprops=dict(arrowstyle='->', color='gray', lw=1)
    )

# Legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Grid settings
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.set_xticks(decades)

# Automatically adjust layout to fit elements
plt.tight_layout()

# Show the plot
plt.show()