import matplotlib.pyplot as plt
import numpy as np

# Data setup
cities = ['New York', 'Berlin', 'Tokyo', 'Amsterdam', 'San Francisco']
e_bikes = np.array([350, 250, 400, 180, 300])  # E-bikes in thousands
public_transport = np.array([800, 600, 900, 500, 700])  # Public transport riders in thousands

# Calculate total mobility and percentages
total_mobility = e_bikes + public_transport
e_bike_percentage = (e_bikes / total_mobility) * 100
public_transport_percentage = (public_transport / total_mobility) * 100

# Define bar positions
x = np.arange(len(cities))
width = 0.35  # width of the bars

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Create bars for E-Bikes and Public Transport
bars1 = ax1.bar(x - width / 2, e_bikes, width, label='E-Bikes', color='#4CAF50')
bars2 = ax1.bar(x + width / 2, public_transport, width, label='Public Transport', color='#2196F3')

# Annotate bars with data values
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 15, f'{height:,}', ha='center', va='bottom', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 15, f'{height:,}', ha='center', va='bottom', fontsize=10)

# Set title and labels
ax1.set_title('The Shift in Urban Mobility:\nE-Bikes vs. Public Transport\nand Their Share of Total Mobility (2023)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Cities', fontsize=14)
ax1.set_ylabel('Number of Riders (in thousands)', fontsize=14)
ax1.set_xticks(x)
ax1.set_xticklabels(cities, rotation=15, fontsize=12)

# Create a secondary axis for the percentage line plot
ax2 = ax1.twinx()
ax2.plot(x, e_bike_percentage, marker='o', color='orange', label='E-Bike Share (%)', linestyle='--', linewidth=2)
ax2.plot(x, public_transport_percentage, marker='o', color='red', label='Public Transport Share (%)', linestyle='--', linewidth=2)

# Set secondary axis limits and labels
ax2.set_ylim(0, 100)
ax2.set_ylabel('Percentage of Total Mobility (%)', fontsize=14)

# Add legends
ax1.legend(fontsize=12, loc='upper left')
ax2.legend(fontsize=12, loc='upper right')

# Enable grid lines for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()