import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy output in GWh for each type of turbine
offshore_output = np.array([120, 125, 130, 133, 135, 140, 142, 145, 150, 152, 155])
onshore_output = np.array([80, 83, 85, 90, 92, 95, 98, 101, 105, 108, 110])
hybrid_output = np.array([50, 60, 65, 72, 85, 90, 100, 110, 120, 130, 140])

# Calculate cumulative outputs
cumulative_output = offshore_output + onshore_output + hybrid_output

# Calculate annual growth rates
offshore_growth = np.diff(offshore_output, prepend=offshore_output[0])
onshore_growth = np.diff(onshore_output, prepend=onshore_output[0])
hybrid_growth = np.diff(hybrid_output, prepend=hybrid_output[0])

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot energy outputs
ax1.plot(years, offshore_output, marker='o', label='Offshore Turbine', linestyle='-', linewidth=2, color='b')
ax1.plot(years, onshore_output, marker='s', label='Onshore Turbine', linestyle='--', linewidth=2, color='g')
ax1.plot(years, hybrid_output, marker='^', label='Hybrid Turbine', linestyle='-.', linewidth=2, color='r')

# Fill area under the curve
ax1.fill_between(years, offshore_output, color='b', alpha=0.1)
ax1.fill_between(years, onshore_output, color='g', alpha=0.1)
ax1.fill_between(years, hybrid_output, color='r', alpha=0.1)

# Cumulative output plot
ax2 = ax1.twinx()
ax2.plot(years, cumulative_output, marker='D', linestyle=':', linewidth=2, color='purple', label='Cumulative Output')
ax2.fill_between(years, cumulative_output, color='purple', alpha=0.05)

# Titles and labels
plt.title('Decade of Progress: EcoPower Co. Wind Turbine Performance\n2010-2020', fontsize=14, pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Output (GWh)', fontsize=12, color='black')
ax2.set_ylabel('Cumulative Output (GWh)', fontsize=12, color='purple')

# Ticks and grid
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(50, 161, 10))
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legends
ax1.legend(loc='upper left', fontsize=10, title='Turbine Type', title_fontsize='13')
ax2.legend(loc='upper right', fontsize=10, title='Cumulative', title_fontsize='13')

# Annotations
max_offshore_index = offshore_output.argmax()
ax1.annotate('Max Offshore Output',
             xy=(years[max_offshore_index], offshore_output[max_offshore_index]), 
             xytext=(years[max_offshore_index] - 2, offshore_output[max_offshore_index] + 10),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=10, color='blue')

# Layout adjustment
fig.tight_layout()

# Display the chart
plt.show()