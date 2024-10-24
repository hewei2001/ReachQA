import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2023
years = np.arange(2015, 2024)

# Define conservation efforts as percentage of total
reforestation = np.array([20, 25, 30, 35, 33, 31, 30, 28, 26])
wildlife_protection = np.array([15, 18, 20, 22, 25, 27, 29, 31, 30])
anti_deforestation_laws = np.array([65, 57, 50, 43, 42, 42, 41, 41, 44])

# Define colors for each strategy
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Plot the area chart
plt.figure(figsize=(12, 7))
plt.stackplot(years, reforestation, wildlife_protection, anti_deforestation_laws,
              labels=['Reforestation', 'Wildlife Protection', 'Anti-Deforestation Laws'],
              colors=colors, alpha=0.8)

# Customize the plot
plt.title("Trends in Forest Conservation Strategies (2015-2023)\nGlobal Forest Conservation Initiative", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Conservation Effort (%)", fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.legend(loc='upper right', fontsize=10)

# Add grid lines for better readability
plt.grid(True, which='both', axis='y', linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()