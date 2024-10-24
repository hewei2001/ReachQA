import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = np.arange(2010, 2026)
adoption_rate = np.array([5, 6.5, 8, 9, 11, 13, 16, 20, 25, 30, 36, 43, 51, 60, 70, 82])
error_margin = np.array([0.5, 0.7, 0.8, 1.0, 1.1, 1.3, 1.5, 2.0, 2.5, 3.0, 3.5, 4.3, 5.1, 6.0, 7.0, 8.2])

# Create the plot
plt.figure(figsize=(12, 7))

# Plot line with error bars
plt.errorbar(years, adoption_rate, yerr=error_margin, fmt='-o', capsize=5, color='teal', ecolor='orange', elinewidth=2, alpha=0.7, label='Adoption Rate')

# Add labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (%)', fontsize=12)
plt.title('Trend of Renewable Energy Adoption\n2010-2025', fontsize=14, fontweight='bold')

# Customize grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=11)

# Annotate specific points
plt.annotate('2020 Milestone: 25%', xy=(2020, 25), xytext=(2017, 35),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=10)
plt.annotate('Projected Peak: 82%', xy=(2025, 82), xytext=(2023, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=10)

# Set limits for better visualization
plt.ylim(0, 90)
plt.xlim(2010, 2025)

# Ensure layout is tidy
plt.tight_layout()

# Show plot
plt.show()