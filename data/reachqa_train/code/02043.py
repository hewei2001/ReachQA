import matplotlib.pyplot as plt
import numpy as np

# Data for years
years = np.arange(2010, 2021)

# Adoption rates in percentages for each sector
residential_rates = np.array([10, 15, 18, 25, 28, 34, 38, 45, 50, 57, 60])
commercial_rates = np.array([8, 12, 15, 20, 23, 27, 32, 36, 41, 47, 52])
industrial_rates = np.array([5, 7, 10, 13, 17, 21, 26, 30, 34, 39, 44])

# Error margins for each sector
residential_errors = np.array([2, 1.5, 2, 1.8, 2.5, 2.8, 3, 2.5, 3, 3.5, 4])
commercial_errors = np.array([1.5, 1.2, 1.8, 2, 2.2, 2.5, 2.7, 3, 2.5, 3, 3.2])
industrial_errors = np.array([1, 1, 1.5, 1.5, 2, 2.2, 2.5, 2.8, 3, 3.3, 3.5])

# Create the plot
plt.figure(figsize=(12, 7))

# Plotting each sector with error bars
plt.errorbar(years, residential_rates, yerr=residential_errors, fmt='-o', capsize=5, label='Residential', color='green', alpha=0.8)
plt.errorbar(years, commercial_rates, yerr=commercial_errors, fmt='-s', capsize=5, label='Commercial', color='blue', alpha=0.8)
plt.errorbar(years, industrial_rates, yerr=industrial_errors, fmt='-d', capsize=5, label='Industrial', color='orange', alpha=0.8)

# Adding title and labels
plt.title("Decade of Green Transition:\nRenewable Energy Adoption in Key Sectors (2010-2020)", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Adoption Rate (%)", fontsize=12)

# Adding grid for better readability
plt.grid(visible=True, linestyle='--', alpha=0.6)

# Adding legend
plt.legend(title="Sectors", loc='upper left')

# Optimizing layout
plt.tight_layout()

# Show the plot
plt.show()