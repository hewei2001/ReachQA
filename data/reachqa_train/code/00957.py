import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Define the average sea surface temperatures in degrees Celsius
sst_data = [16.1, 16.3, 16.5, 16.6, 16.8, 17.1, 17.3, 17.6, 17.8, 18.0, 18.3]

# Define a related dataset - temperature anomaly (arbitrary values for illustration)
anomaly_data = [0.1, 0.2, 0.15, 0.1, 0.3, 0.4, 0.35, 0.5, 0.45, 0.55, 0.6]

# Calculate the baseline temperature for each year
baseline = [x - y for x, y in zip(sst_data, anomaly_data)]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the line chart for sea surface temperatures
ax1.plot(years, sst_data, marker='o', linestyle='-', color='navy', linewidth=2, markersize=6, label='Average SST')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Sea Surface Temperature (°C)', fontsize=12, color='navy')
ax1.tick_params(axis='y', labelcolor='navy')

# Add a secondary y-axis for temperature anomalies
ax2 = ax1.twinx()
ax2.bar(years, anomaly_data, color='skyblue', alpha=0.6, label='Temperature Anomaly')
ax2.set_ylabel('Temperature Anomaly (°C)', fontsize=12, color='skyblue')
ax2.tick_params(axis='y', labelcolor='skyblue')

# Add annotations for the sea surface temperatures
for year, sst in zip(years, sst_data):
    ax1.annotate(f'{sst}°C', 
                 xy=(year, sst), 
                 xytext=(0, 10), 
                 textcoords='offset points',
                 fontsize=9,
                 ha='center',
                 arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Add annotations for the anomaly data
for year, anomaly in zip(years, anomaly_data):
    ax2.annotate(f'{anomaly}°C',
                 xy=(year, anomaly),
                 xytext=(0, -12),
                 textcoords='offset points',
                 fontsize=9,
                 ha='center',
                 color='blue')

# Set the title with line breaks for better readability
ax1.set_title('Decadal Sea Surface Temperature Changes and Anomalies\n(2010-2020)', fontsize=14, fontweight='bold', pad=15)

# Add grid lines to the primary axis
ax1.grid(True, linestyle='--', alpha=0.7)

# Add legends for both plots
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()