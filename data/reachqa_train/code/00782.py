import matplotlib.pyplot as plt
import numpy as np

# Define the years for the projections
years = np.arange(2020, 2031)

# Budget projections for each mission type (in Billion USD)
lunar_budget = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5])
mars_budget = np.array([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
asteroid_budget = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0])
deep_space_budget = np.array([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5])

# Budget variability (standard deviation) due to uncertainties
lunar_variability = np.array([0.2] * 11)
mars_variability = np.array([0.25] * 11)
asteroid_variability = np.array([0.15] * 11)
deep_space_variability = np.array([0.3] * 11)

# Plotting the line chart with error bars
plt.figure(figsize=(12, 8))

# Plot each mission type with its error bars
plt.errorbar(years, lunar_budget, yerr=lunar_variability, fmt='-o', label='Lunar Missions',
             capsize=4, color='grey', alpha=0.8)
plt.errorbar(years, mars_budget, yerr=mars_variability, fmt='-s', label='Mars Missions',
             capsize=4, color='tomato', alpha=0.8)
plt.errorbar(years, asteroid_budget, yerr=asteroid_variability, fmt='-^', label='Asteroid Exploration',
             capsize=4, color='skyblue', alpha=0.8)
plt.errorbar(years, deep_space_budget, yerr=deep_space_variability, fmt='-D', label='Deep Space Probes',
             capsize=4, color='forestgreen', alpha=0.8)

# Add titles and labels
plt.title('Space Exploration Budget Over Time:\nProjections and Variability by Mission Type',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Budget (Billion USD)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Add legend and ensure it does not overlap
plt.legend(loc='upper left', fontsize=12, frameon=False)

# Add grid lines for better readability
plt.grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()