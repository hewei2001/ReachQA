import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Solar energy production data in gigawatts (GW) for five cities
san_francisco = np.array([1.0, 1.2, 1.5, 1.9, 2.3, 3.0, 3.7, 4.5, 5.5, 6.8, 7.5])
berlin = np.array([0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.1, 3.8, 4.2, 4.9, 5.3])
tokyo = np.array([2.5, 2.8, 3.2, 3.6, 4.0, 4.5, 5.0, 5.7, 6.3, 7.0, 7.8])
sydney = np.array([0.9, 1.1, 1.3, 1.6, 2.1, 2.7, 3.4, 4.0, 4.7, 5.4, 6.0])
cape_town = np.array([0.5, 0.6, 0.8, 1.0, 1.3, 1.6, 2.0, 2.5, 3.0, 3.6, 4.2])

# Initialize the plot
plt.figure(figsize=(14, 7))

# Plotting each city's data with distinct styles
plt.plot(years, san_francisco, label='San Francisco', marker='o', linestyle='-', linewidth=2, color='b')
plt.plot(years, berlin, label='Berlin', marker='s', linestyle='--', linewidth=2, color='g')
plt.plot(years, tokyo, label='Tokyo', marker='^', linestyle='-.', linewidth=2, color='r')
plt.plot(years, sydney, label='Sydney', marker='D', linestyle=':', linewidth=2, color='c')
plt.plot(years, cape_town, label='Cape Town', marker='x', linestyle='-', linewidth=2, color='m')

# Title and labels
plt.title('Decadal Growth in Solar Energy Production\nAcross Major Cities', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Solar Energy Production (GW)', fontsize=12)
plt.xticks(years, rotation=45)

# Adding a legend
plt.legend(title="Cities", loc='upper left', fontsize=10)

# Adding a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()