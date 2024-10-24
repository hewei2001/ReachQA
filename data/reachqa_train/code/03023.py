import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2010, 2020)

# Construct the artificial data for wheat yield (in tons per hectare)
wheat_yield = np.array([3.2, 3.4, 3.5, 3.8, 3.7, 4.0, 4.1, 4.2, 3.9, 4.3])  # Yield
error = np.array([0.2, 0.25, 0.15, 0.3, 0.25, 0.3, 0.2, 0.3, 0.35, 0.3])    # Variability as error bars

# Create the plot
plt.figure(figsize=(12, 6))

# Plot the wheat yield data with error bars
plt.errorbar(years, wheat_yield, yerr=error, fmt='-o', color='forestgreen', 
             ecolor='lightcoral', elinewidth=3, capsize=4, label='Wheat Yield')

# Customize the plot
plt.title('Wheat Yield Trends and Variability\n(2010-2019)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Yield (tons/ha)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(3.0, 4.5, 0.2))
plt.grid(linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)

# Add a narrative text for context
plt.text(2010.5, 4.25, "Yield variability due to climatic and biological factors", 
         fontsize=10, color='darkblue', bbox=dict(facecolor='lightgrey', alpha=0.5))

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()