import matplotlib.pyplot as plt
import numpy as np

# Define the decades and corresponding data
decades = np.array([1980, 1990, 2000, 2010, 2020, 2030])
average_sst = np.array([15.5, 15.7, 15.9, 16.0, 16.2, 16.4])  # Average SST in degrees Celsius
uncertainty = np.array([0.1, 0.12, 0.11, 0.13, 0.15, 0.14])  # Measurement uncertainties

# Initialize the plot
plt.figure(figsize=(10, 6))

# Plot the line chart with error bars
plt.errorbar(decades, average_sst, yerr=uncertainty, fmt='-o', ecolor='skyblue', capsize=5,
             capthick=2, color='darkorange', alpha=0.9, marker='s', markersize=7,
             label='Average SST with Uncertainty')

# Enhance readability with grid
plt.grid(True, linestyle='--', alpha=0.7)

# Set titles and labels
plt.title("Decadal Trends in Global Sea Surface Temperature\nand Associated Uncertainty (1980-2030)", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Average SST (°C)", fontsize=12)

# Define axes limits to ensure all elements are well within the frame
plt.ylim(15.0, 17.0)
plt.xlim(1975, 2035)

# Include a legend to clarify plot elements
plt.legend(loc='upper left', fontsize=11)

# Optimize layout to avoid clipping of text and labels
plt.tight_layout()

# Display the plot
plt.show()