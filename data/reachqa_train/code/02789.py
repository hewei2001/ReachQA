import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2030, 2041)
gso_investment = [1.2, 1.8, 2.5, 3.1, 4.0, 5.0, 6.3, 7.2, 8.5, 9.5, 10.2]
pea_investment = [0.8, 1.5, 2.0, 2.6, 3.5, 4.5, 5.1, 6.0, 7.0, 7.8, 8.4]
egc_investment = [0.6, 1.1, 1.8, 2.3, 3.0, 3.7, 4.5, 5.3, 6.5, 7.0, 7.9]

# Plot
plt.figure(figsize=(12, 8))

# Stackplot for cumulative investment
plt.stackplot(years, gso_investment, pea_investment, egc_investment,
              labels=['Global Space Organization', 'Pacific Exploration Alliance', 'Euro-Galactic Coalition'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Titles and Labels
plt.title('Investment in Ocean Worlds Exploration\nand Colonization (2030-2040)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Investment (Billions of Dollars)', fontsize=14)

# Legend and Grid
plt.legend(loc='upper left', title='Space Agencies', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Customize x-axis and y-axis ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 31, 5))

# Ensure the layout fits into the figure area
plt.tight_layout()

# Annotations to highlight key trends
plt.annotate('GSO Leads Investment', xy=(2035, 4.0), xytext=(2036, 8.0),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, backgroundcolor='white')
plt.annotate('PEA Steady Growth', xy=(2038, 6.0), xytext=(2039, 11.0),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=12, backgroundcolor='white')
plt.annotate('EGC Catching Up', xy=(2040, 7.9), xytext=(2040, 15.0),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=12, backgroundcolor='white')

# Show the plot
plt.show()