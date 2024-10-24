import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data setup
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
funding = np.array([10, 15, 25, 30, 40, 55, 70, 85, 95, 105, 120])
projected_growth = np.array([15, 18, 22, 25, 28, 35, 40, 42, 45, 48, 50])
market_impact = np.array([4, 5, 6, 6.5, 7, 7.5, 8, 8.2, 8.5, 9, 9.5])

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
sc = ax.scatter(years, funding, projected_growth, s=market_impact*100, c=market_impact, cmap='cool', alpha=0.7, edgecolors='w', linewidth=0.5)

# Title and labels
ax.set_title('Futurism and Innovation:\nThe Evolution of Tech Startups', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Funding (Million $)', fontsize=12)
ax.set_zlabel('Projected Growth (%)', fontsize=12)

# Annotate each point
for i in range(len(years)):
    ax.text(years[i], funding[i], projected_growth[i], f'{years[i]}', fontsize=9, color='black', ha='center')

# Adding color bar for market impact
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Market Impact', fontsize=12)

# Customize the viewing angle
ax.view_init(elev=20, azim=130)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()