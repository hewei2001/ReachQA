import matplotlib.pyplot as plt
import numpy as np

# Decades for the x-axis
decades = ['1980s', '2000s', '2020s']

# Data: Trips per 1000 residents for each transport mode by decade
data = np.array([
    [300, 150, 80],   # Walking
    [50, 120, 180],   # Cycling
    [350, 300, 250],  # Public Transport
    [250, 400, 350],  # Private Cars
    [0, 30, 140]      # Ride-Sharing
])

# Colors for each transportation mode
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Initialize the plot
plt.figure(figsize=(12, 8))

# Stack the bars
bottom_data = np.zeros(len(decades))  # Initial bottom of each bar

# Create bars for each transport mode
for i, (transport_mode, color) in enumerate(zip(data, colors)):
    plt.bar(decades, transport_mode, color=color, bottom=bottom_data, label=['Walking', 'Cycling', 'Public Transport', 'Private Cars', 'Ride-Sharing'][i], edgecolor='black')
    bottom_data += transport_mode  # Update bottom position for next bar stack

# Add axis labels and title
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Trips per 1000 Residents', fontsize=12)
plt.title('The Evolution of Urban Transportation Modes\nin Metropolis Over Decades', fontsize=16, fontweight='bold', pad=20)

# Add a legend with a title and ensure it doesn't overlap with the chart
plt.legend(title='Transport Modes', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate each bar segment with its value
for i in range(len(decades)):
    y_offset = 0
    for j in range(len(data)):
        y = data[j, i] / 2 + y_offset
        y_offset += data[j, i]
        plt.text(i, y, str(data[j, i]), ha='center', va='center', color='black', fontsize=9, fontweight='bold')

# Enhance layout to prevent element overlap and improve appearance
plt.tight_layout()

# Display the plot
plt.show()