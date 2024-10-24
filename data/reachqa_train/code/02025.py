import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2022
years = np.arange(2013, 2023)

# Data: Number of residential solar installations (in thousands)
san_francisco = [10, 13, 17, 22, 29, 37, 46, 58, 72, 90]
austin = [8, 12, 16, 21, 26, 33, 41, 52, 66, 83]
munich = [5, 8, 11, 16, 22, 29, 38, 49, 62, 77]
bangalore = [7, 10, 14, 19, 25, 33, 42, 54, 68, 85]
tokyo = [9, 14, 19, 25, 32, 41, 52, 66, 83, 102]

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each city's data
plt.plot(years, san_francisco, marker='o', linestyle='-', linewidth=2, label='San Francisco', color='#1f77b4')
plt.plot(years, austin, marker='s', linestyle='--', linewidth=2, label='Austin', color='#ff7f0e')
plt.plot(years, munich, marker='^', linestyle='-.', linewidth=2, label='Munich', color='#2ca02c')
plt.plot(years, bangalore, marker='d', linestyle=':', linewidth=2, label='Bangalore', color='#d62728')
plt.plot(years, tokyo, marker='p', linestyle='-', linewidth=2, label='Tokyo', color='#9467bd')

# Set the title and labels
plt.title('Growth of Residential Solar Installations\n(2013-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Installations (Thousands)', fontsize=14)

# Customize legend
plt.legend(title='City', fontsize=12, loc='upper left', frameon=True)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust x-ticks and labels to avoid overlap
plt.xticks(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()