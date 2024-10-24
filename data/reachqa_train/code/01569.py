import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2012 to 2022
years = np.arange(2012, 2023)

# Interest index data for different regions (Hypothetical data showing trends)
north_america = np.array([10, 15, 18, 22, 30, 40, 50, 65, 78, 85, 95])
europe = np.array([8, 12, 15, 20, 25, 35, 45, 55, 67, 74, 80])
asia_pacific = np.array([5, 8, 12, 18, 27, 35, 48, 60, 72, 82, 90])

# Create the plot
plt.figure(figsize=(12, 6))

# Plotting data for each region
plt.plot(years, north_america, label='North America', marker='o', linestyle='-', linewidth=2.5, color='blue')
plt.plot(years, europe, label='Europe', marker='s', linestyle='--', linewidth=2.5, color='green')
plt.plot(years, asia_pacific, label='Asia-Pacific', marker='^', linestyle='-.', linewidth=2.5, color='red')

# Title and labels
plt.title('Rising Curiosity: Quantum Computing in Academia\n(2012-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Interest Index', fontsize=12)
plt.xticks(years, rotation=45)  # Rotate to prevent overlap

# Adding a legend
plt.legend(title="Regions", loc='upper left', fontsize=10)

# Adding a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()