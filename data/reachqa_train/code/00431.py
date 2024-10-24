import matplotlib.pyplot as plt
import numpy as np

# Define decades and corresponding data for each mode of transportation
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
walking = [35, 30, 25, 20, 15]
bicycling = [10, 12, 15, 17, 20]
public_transport = [20, 22, 25, 27, 30]
cars = [30, 32, 28, 30, 25]
air_travel = [5, 4, 7, 6, 10]

# Stack data into a numpy array
data = np.array([walking, bicycling, public_transport, cars, air_travel])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(decades, data, labels=['Walking', 'Bicycling', 'Public Transport', 'Cars', 'Air Travel'],
             colors=['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3'], alpha=0.8)

# Configure title, labels, and legend
ax.set_title('Evolution of Transportation Modes\nOver the Decades', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage Usage (%)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Improve grid visibility
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()