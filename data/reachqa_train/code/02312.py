import matplotlib.pyplot as plt
import numpy as np

# Define time periods and data for multiple space agencies
years = np.arange(1970, 2025, 5)
nasa_launches = np.array([5, 10, 15, 25, 35, 50, 70, 85, 100, 110, 130])
esa_launches = np.array([3, 7, 10, 20, 30, 45, 65, 80, 95, 105, 125])
cnsa_launches = np.array([1, 4, 5, 15, 25, 40, 60, 75, 85, 95, 115])
roscosmos_launches = np.array([8, 12, 20, 30, 40, 55, 75, 85, 100, 115, 135])
isro_launches = np.array([0, 1, 5, 10, 15, 25, 35, 50, 65, 80, 95])

# Set up the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Plot the number of launches
ax1.plot(years, nasa_launches, marker='o', linestyle='-', color='royalblue', linewidth=2, label='NASA')
ax1.plot(years, esa_launches, marker='s', linestyle='--', color='green', linewidth=2, label='ESA')
ax1.plot(years, cnsa_launches, marker='^', linestyle='-.', color='red', linewidth=2, label='CNSA')
ax1.plot(years, roscosmos_launches, marker='D', linestyle='-', color='orange', linewidth=2, label='Roscosmos')
ax1.plot(years, isro_launches, marker='x', linestyle=':', color='purple', linewidth=2, label='ISRO')

# Customize the first subplot
ax1.set_title("Space Exploration: Satellite Launches by Agency (1970-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Satellite Launches", fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 141, 20))
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Space Agencies', loc='upper left', fontsize=10, frameon=True)

# Annotate key points
ax1.annotate('Rise of GPS', xy=(1990, 25), xytext=(1975, 60), arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.8))
ax1.annotate('Commercial Boom', xy=(2010, 45), xytext=(2000, 80), arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.8))

# Stacked area plot for cumulative launches
ax2.stackplot(years, nasa_launches, esa_launches, cnsa_launches, roscosmos_launches, isro_launches,
              labels=['NASA', 'ESA', 'CNSA', 'Roscosmos', 'ISRO'],
              colors=['royalblue', 'green', 'red', 'orange', 'purple'], alpha=0.6)

# Customize the second subplot
ax2.set_title("Cumulative Growth in Satellite Launches (1970-2020)", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Cumulative Launches", fontsize=12)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 401, 50))
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=10, frameon=True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()