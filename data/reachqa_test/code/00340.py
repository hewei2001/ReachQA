import matplotlib.pyplot as plt
import numpy as np

# Define decades and temperature anomalies (in degrees Celsius)
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
temperature_anomalies = np.array([0.0, 0.1, 0.2, 0.35, 0.55, 0.8, 1.05])

# Define CO2 concentration levels (ppm) for the same decades
co2_levels = np.array([315, 325, 340, 355, 370, 390, 415])

# Significant climate milestones
milestones = {
    1990: "First IPCC Report",
    2000: "Kyoto Protocol",
    2015: "Paris Agreement"
}

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot temperature anomalies
ax1.plot(decades, temperature_anomalies, marker='o', color='firebrick', linewidth=2.5, linestyle='--', label='Temperature Anomaly')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Temperature Anomaly (°C)", fontsize=12, color='firebrick')
ax1.tick_params(axis='y', labelcolor='firebrick')

# Annotate temperature anomaly data points
for year, anomaly in zip(decades, temperature_anomalies):
    ax1.annotate(f'{anomaly:.2f}°C', xy=(year, anomaly), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='black')

# Annotate climate milestones
for year, event in milestones.items():
    if year in decades:  # Check if the milestone year is in decades
        ax1.annotate(event, xy=(year, temperature_anomalies[np.where(decades == year)][0]),
                     textcoords="offset points", xytext=(-10, -25), ha='center', fontsize=9, fontweight='bold', color='darkblue',
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='darkblue'))

# Create a second y-axis for CO2 levels
ax2 = ax1.twinx()
ax2.bar(decades, co2_levels, color='skyblue', alpha=0.6, width=7, label='CO2 Levels (ppm)')
ax2.set_ylabel("CO2 Levels (ppm)", fontsize=12, color='skyblue')
ax2.tick_params(axis='y', labelcolor='skyblue')

# Set title with line breaks for readability
ax1.set_title("Global Average Temperature Rise and CO2 Concentration:\nA Six-Decade Overview (1960-2020)", fontsize=14, fontweight='bold')

# Add grid to the plot
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Set axis limits
ax1.set_xlim(1955, 2025)
ax1.set_ylim(-0.1, 1.2)
ax2.set_ylim(310, 430)

# Display legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85), fontsize=10, frameon=False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()