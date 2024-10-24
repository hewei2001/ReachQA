import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2040, 2051)

# Hypothetical production data (in metric tons) for each synthetic element
elementium_production = [5, 10, 15, 25, 40, 60, 80, 110, 150, 195, 250]
newtrogen_production = [3, 5, 8, 12, 20, 35, 50, 70, 95, 125, 165]
quantumite_production = [1, 3, 5, 10, 18, 30, 45, 65, 90, 120, 155]

# Initialize the plot
plt.figure(figsize=(12, 8))

# Plot each synthetic element's production data
plt.plot(years, elementium_production, label='Elementium', color='blue', 
         linewidth=2, linestyle='-', marker='o', markersize=6)
plt.plot(years, newtrogen_production, label='Newtrogen', color='green', 
         linewidth=2, linestyle='--', marker='s', markersize=6)
plt.plot(years, quantumite_production, label='Quantumite', color='red', 
         linewidth=2, linestyle='-.', marker='^', markersize=6)

# Customize the plot
plt.title('Evolution of Synthetic Element Production\nfrom 2040 to 2050', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Production (Metric Tons)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 301, 50))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend and adjust layout
plt.legend(title='Synthetic Elements', loc='upper left')
plt.tight_layout()

# Display the plot
plt.show()