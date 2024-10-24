import matplotlib.pyplot as plt
import numpy as np

# Data
airports = [
    'Atlanta Hartsfield-Jackson International Airport', 'Beijing Capital International Airport', 
    'Los Angeles International Airport', 'Tokyo International Airport', 'Dubai International Airport', 
    'Shanghai Pudong International Airport', 'Hong Kong International Airport', 'Seoul Incheon International Airport', 
    'Paris Charles de Gaulle Airport', 'Dallas/Fort Worth International Airport'
]
airport_codes = ['ATL', 'PEK', 'LAX', 'HND', 'DXB', 'PVG', 'HKG', 'ICN', 'CDG', 'DFW']
passenger_traffic = np.array([107.39, 100.11, 88.07, 87.09, 86.39, 84.51, 82.65, 77.47, 76.16, 75.07])

# Calculate total passenger traffic and average traffic
total_traffic = np.sum(passenger_traffic)
average_traffic = np.mean(passenger_traffic)

# Calculate percentage scale based on total traffic
percentage_traffic = (passenger_traffic / total_traffic) * 100

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bars
bars = ax.barh(airports, passenger_traffic, color=plt.cm.coolwarm(np.linspace(0, 1, len(airports))), height=0.5)

# Add value and percentage labels at the end of each bar
for bar, traffic, percentage in zip(bars, passenger_traffic, percentage_traffic):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{traffic:.2f}M ({percentage:.2f}%)',
            ha='left', va='center', color='gray', fontsize=10)

# Set title and labels
title = "Top 10 Busiest Airports in the World by Annual Passenger Traffic\n"
subtitle = "(2020 data, in millions of passengers, source: Airports Council International)"
ax.set_title(title + subtitle, fontsize=14, pad=20)
ax.set_xlabel("Annual Passenger Traffic (millions)", fontsize=12)
ax.set_ylabel("Airport", fontsize=12)

# Add a horizontal line for average traffic
ax.axvline(x=average_traffic, color='k', linestyle='--', linewidth=1, label='Average Traffic')
ax.legend(loc='upper right', fontsize=10)

# Add airport codes to y-axis labels
ax.set_yticklabels([f'{airport}\n({code})' for airport, code in zip(airports, airport_codes)], fontsize=10)

# Adjust layout and ticks
ax.tick_params(axis='y', labelsize=10, length=0)
ax.set_xlim(0, passenger_traffic.max() * 1.1)
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Final layout adjustment
plt.tight_layout()

# Show the plot
plt.show()