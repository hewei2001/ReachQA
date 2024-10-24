import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define years, cities, and initiatives
years = np.arange(2010, 2021)
cities = ['New York', 'London', 'Tokyo', 'Sydney']
initiatives = ['Smart Grids', 'Intelligent Transport', 'Digital Governance', 'Green Buildings']

# Hypothetical budget allocation data (in million USD) for each city per initiative per year
ny_budgets = [
    [50, 40, 30, 20], [52, 42, 35, 25], [54, 45, 38, 28], [57, 47, 40, 32],
    [60, 50, 43, 35], [63, 53, 46, 38], [65, 55, 50, 40], [68, 58, 52, 42],
    [70, 60, 54, 44], [72, 63, 57, 47], [75, 65, 60, 50]
]
ldn_budgets = [
    [45, 35, 25, 15], [48, 37, 28, 18], [50, 40, 30, 20], [52, 43, 32, 23],
    [55, 45, 35, 25], [57, 48, 38, 27], [60, 50, 40, 30], [63, 53, 42, 32],
    [65, 55, 45, 34], [67, 58, 47, 37], [70, 60, 50, 40]
]
tky_budgets = [
    [40, 30, 20, 10], [42, 32, 22, 13], [45, 34, 25, 15], [47, 37, 28, 18],
    [50, 40, 30, 20], [53, 42, 32, 23], [55, 45, 35, 25], [57, 48, 37, 28],
    [60, 50, 40, 30], [62, 52, 43, 33], [65, 55, 45, 35]
]
syd_budgets = [
    [35, 25, 15, 5], [37, 28, 17, 8], [40, 30, 20, 10], [43, 32, 22, 13],
    [45, 35, 25, 15], [48, 37, 27, 18], [50, 40, 30, 20], [53, 43, 32, 23],
    [55, 45, 35, 25], [57, 48, 37, 28], [60, 50, 40, 30]
]

# Convert the budgets to NumPy arrays for easier slicing
ny_budgets = np.array(ny_budgets)
ldn_budgets = np.array(ldn_budgets)
tky_budgets = np.array(tky_budgets)
syd_budgets = np.array(syd_budgets)

# Collect budgets into a single list
budgets = [ny_budgets, ldn_budgets, tky_budgets, syd_budgets]

# Define colors for initiatives
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Plot setup
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Adjusting the viewing angle for better visibility
ax.view_init(elev=30, azim=120)

# Plotting each city with its budget distribution over the years
for c_idx, city in enumerate(cities):
    y = np.array(years)
    for i_idx, initiative in enumerate(initiatives):
        z = np.zeros_like(years) if i_idx == 0 else np.sum(budgets[c_idx][:, :i_idx], axis=1)
        dz = budgets[c_idx][:, i_idx]
        ax.bar3d(np.array([c_idx]*len(years)), y, z, 0.7, 1, dz, color=colors[i_idx], alpha=0.8, edgecolor='k')

# Title and axis labels
ax.set_title('Budget Allocation for Smart City Initiatives (2010-2020)', fontsize=15, pad=25)
ax.set_xlabel('City', fontsize=12, labelpad=10)
ax.set_ylabel('Year', fontsize=12, labelpad=10)
ax.set_zlabel('Budget (Million USD)', fontsize=12, labelpad=10)

# Customize ticks and labels
ax.set_xticks(np.arange(len(cities)))
ax.set_xticklabels(cities, fontsize=10, rotation=20)
ax.set_yticks(years)
ax.set_yticklabels(years, fontsize=9)

# Create a legend
ax.legend(initiatives, loc='upper left', fontsize=10, title='Initiatives', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Adjust layout for clarity
plt.tight_layout()

# Show plot
plt.show()