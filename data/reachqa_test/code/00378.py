import numpy as np
import matplotlib.pyplot as plt

# Define cities and months
cities = ['New York', 'London', 'Tokyo', 'Beijing', 'Mumbai', 'São Paulo', 'Mexico City', 'Cairo', 'Sydney', 'Paris']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Air pollution data (PM2.5 in μg/m³)
data = np.array([
    [30, 28, 25, 23, 20, 18, 20, 22, 24, 27, 30, 32],  # New York
    [20, 18, 16, 15, 13, 12, 14, 15, 17, 18, 20, 22],  # London
    [45, 42, 40, 38, 35, 33, 35, 38, 40, 42, 45, 48],  # Tokyo
    [55, 52, 50, 48, 45, 43, 45, 48, 50, 52, 55, 58],  # Beijing
    [35, 33, 30, 28, 25, 23, 25, 28, 30, 32, 35, 38],  # Mumbai
    [28, 26, 24, 23, 20, 18, 20, 22, 24, 25, 28, 30],  # São Paulo
    [38, 35, 33, 30, 28, 26, 28, 30, 33, 35, 38, 40],  # Mexico City
    [25, 23, 20, 18, 15, 13, 15, 18, 20, 22, 25, 28],  # Cairo
    [18, 16, 15, 13, 10, 8, 10, 12, 15, 16, 18, 20],   # Sydney
    [22, 20, 18, 16, 14, 12, 14, 16, 18, 20, 22, 25]   # Paris
])

# Create figure and axis objects
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

# Heatmap
im = ax1.imshow(data, cmap='RdYlGn_r', aspect='auto')
ax1.set_title("Global Air Pollution Levels (PM2.5, μg/m³)", fontsize=16)
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, rotation=90, fontsize=10)
ax1.set_yticks(np.arange(len(cities)))
ax1.set_yticklabels(cities, fontsize=10)
fig.colorbar(im, ax=ax1, label='PM2.5 (μg/m³)', fraction=0.046, pad=0.04)

# Mean pollution levels across cities
ax2.plot(months, np.mean(data, axis=0), marker='o', color='b')
ax2.set_title('Mean Monthly PM2.5 Across Cities')
ax2.set_xlabel('Months')
ax2.set_ylabel('Mean PM2.5 (μg/m³)')
ax2.set_ylim([15, 40])
ax2.grid(True)

# Layout adjustments and display
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()
