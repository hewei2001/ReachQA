import matplotlib.pyplot as plt
import numpy as np

# Define the months and corresponding AQI values for Metroville
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Hypothetical AQI values for each month
aqi_values = [85, 78, 90, 70, 65, 55, 60, 58, 67, 72, 75, 80]

# Hypothetical average temperature (Celsius) for each month
temperature_values = [6, 7, 10, 15, 20, 24, 26, 25, 22, 16, 10, 7]

# Create subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))

# First subplot: Line chart for AQI values
ax1.plot(months, aqi_values, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8, label='AQI 2023')

events = {
    "February": "Policy impact",
    "April": "Spring rain effect",
    "June": "Purifier installations",
    "August": "Traffic increase"
}

for month, event in events.items():
    month_index = months.index(month)
    ax1.annotate(
        event,
        xy=(month, aqi_values[month_index]),
        xytext=(-10, 10) if aqi_values[month_index] > 70 else (-10, -30),
        textcoords='offset points',
        ha='center',
        arrowprops=dict(arrowstyle='->', color='gray')
    )

ax1.set_xlabel("Months", fontsize=12, fontweight='bold')
ax1.set_ylabel("Average AQI", fontsize=12, fontweight='bold')
ax1.set_title(
    "Urban Air Quality Monitoring\nin Metroville: 2023",
    fontsize=14,
    fontweight='bold'
)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, rotation=45, ha='right')

# Second subplot: Bar chart for average temperature
ax2.bar(months, temperature_values, color='coral', label='Avg Temperature 2023')
ax2.set_xlabel("Months", fontsize=12, fontweight='bold')
ax2.set_ylabel("Temperature (°C)", fontsize=12, fontweight='bold')
ax2.set_title(
    "Monthly Average Temperature\nin Metroville: 2023",
    fontsize=14,
    fontweight='bold'
)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(np.arange(len(months)))
ax2.set_xticklabels(months, rotation=45, ha='right')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()