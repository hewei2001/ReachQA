import matplotlib.pyplot as plt
import numpy as np

# Define decades and corresponding temperature anomalies (in °C)
decades = np.arange(1880, 2020, 10)  # Corrected to match temperature_anomalies length
regions = ['N. America', 'S. America', 'Europe', 'Africa', 'Asia', 'Australia', 'Antarctica']

# Construct synthetic data representing the temperature anomaly for each region over each decade
temperature_anomalies = np.array([
    [-0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.0],  # 1880s
    [-0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.1],   # 1890s
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.2],    # 1900s
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.3],    # 1910s
    [0.0, 0.0, 0.2, 0.2, 0.4, 0.6, 0.3],    # 1920s
    [0.1, 0.2, 0.3, 0.2, 0.3, 0.4, 0.3],    # 1930s
    [0.2, 0.3, 0.4, 0.3, 0.4, 0.5, 0.4],    # 1940s
    [0.3, 0.4, 0.5, 0.4, 0.3, 0.6, 0.5],    # 1950s
    [0.4, 0.5, 0.6, 0.5, 0.6, 0.7, 0.6],    # 1960s
    [0.5, 0.6, 0.7, 0.6, 0.7, 0.8, 0.7],    # 1970s
    [0.6, 0.7, 0.8, 0.7, 0.8, 0.9, 0.8],    # 1980s
    [0.7, 0.8, 0.9, 0.8, 0.9, 1.0, 0.9],    # 1990s
    [0.8, 0.9, 1.0, 0.9, 1.0, 1.1, 1.0],    # 2000s
    [0.9, 1.0, 1.1, 1.0, 1.1, 1.2, 1.1]     # 2010s
])

# Plotting the heat map
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.imshow(temperature_anomalies, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Adding color bar
cbar = fig.colorbar(cax, ax=ax, orientation='vertical', shrink=0.8)
cbar.set_label('Temperature Anomaly (°C)', rotation=270, labelpad=15)

# Set the labels for x and y axes
ax.set_xticks(np.arange(len(regions)))
ax.set_yticks(np.arange(len(decades)))
ax.set_xticklabels(regions, rotation=45, ha='right')
ax.set_yticklabels(decades)
ax.set_title('Average Global Temperature Anomalies\n(1880 - 2010)', fontsize=16, fontweight='bold')

# Annotating the heat map
for i in range(len(decades)):
    for j in range(len(regions)):
        ax.text(j, i, f"{temperature_anomalies[i, j]:.1f}", ha='center', va='center', color='black')

plt.xlabel('Region', fontsize=12)
plt.ylabel('Decade', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()
plt.show()