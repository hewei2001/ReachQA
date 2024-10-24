import matplotlib.pyplot as plt
import numpy as np

# Define the decades
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Average global temperature anomalies in Celsius
temperature_anomalies = np.array([-0.05, 0.01, 0.12, 0.32, 0.45, 0.63, 0.80])

# Uncertainties in the measurements (standard deviation)
uncertainties = np.array([0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the line chart with error bars
ax.errorbar(decades, temperature_anomalies, yerr=uncertainties, fmt='-o', color='tab:red', ecolor='tab:blue', 
            elinewidth=2, capsize=4, alpha=0.8, label='Temperature Anomalies')

# Annotate each point with its value
for i, (decade, anomaly) in enumerate(zip(decades, temperature_anomalies)):
    ax.annotate(f'{anomaly:+.2f}°C', xy=(decade, anomaly), xytext=(0, 10),
                textcoords='offset points', ha='center', fontsize=10, color='black')

# Set titles and labels
ax.set_title('Climate Science Research:\nTemperature Anomalies Over Decades (1960-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=12)

# Add grid lines for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Set y-ticks to be dynamically scaled
ax.set_yticks(np.arange(-0.2, 1.0, 0.1))

# Add a legend to indicate what the line represents
ax.legend(loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()