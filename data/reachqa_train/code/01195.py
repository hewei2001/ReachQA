import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2019
years = np.arange(2010, 2020)

# Average monthly consumption in pounds
chocolates = [55, 58, 60, 63, 62, 60, 59, 58, 56, 55]
gummies = [30, 32, 35, 38, 42, 45, 48, 50, 53, 55]
hard_candies = [25, 23, 22, 20, 18, 16, 15, 13, 12, 11]

# Setting up the plot
plt.figure(figsize=(12, 7))

# Define bin edges for the histogram
bin_edges = np.arange(2010, 2020, 1)

# Plot histograms for each candy type
plt.hist([years, years, years], bins=bin_edges, weights=[chocolates, gummies, hard_candies], 
         label=['Chocolates', 'Gummies', 'Hard Candies'], color=['saddlebrown', 'darkorange', 'royalblue'], 
         alpha=0.7, edgecolor='black', histtype='bar')

# Customize the plot
plt.title("The Sweet Symphony of Sugar Consumption:\nA Decade of Candy Cravings in the United States", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Avg Monthly Consumption (Pounds)", fontsize=14)
plt.xticks(years)
plt.yticks(range(0, 81, 10))
plt.legend(title="Candy Type", fontsize=12)

# Enhance the x-axis labels to improve readability
plt.xticks(rotation=45, ha='right')

# Add a grid to the background
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()