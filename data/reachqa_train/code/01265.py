import numpy as np
import matplotlib.pyplot as plt

# Months over a year (January to December)
months = np.arange(1, 13)

# Growth data in centimeters (cm) for each environment
desert_growth = np.array([5, 8, 12, 15, 17, 18, 19, 19, 20, 21, 22, 23])
temperate_growth = np.array([10, 15, 20, 30, 40, 50, 55, 60, 65, 70, 72, 75])
rainforest_growth = np.array([15, 25, 35, 50, 70, 90, 100, 105, 110, 115, 118, 120])

# Construct related data for leaf count
desert_leaves = np.array([3, 5, 7, 9, 10, 10, 11, 11, 12, 12, 13, 14])
temperate_leaves = np.array([5, 7, 10, 15, 20, 25, 27, 30, 32, 33, 34, 35])
rainforest_leaves = np.array([8, 12, 17, 25, 35, 45, 50, 52, 55, 57, 58, 60])

# Initialize the plot with subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Line plot of growth data
axes[0].plot(months, desert_growth, label='Desert', color='#FFA500', marker='o', linestyle='--', linewidth=2)
axes[0].plot(months, temperate_growth, label='Temperate', color='#228B22', marker='s', linestyle='-.', linewidth=2)
axes[0].plot(months, rainforest_growth, label='Rainforest', color='#4682B4', marker='^', linestyle='-', linewidth=2)
axes[0].set_title("Growth Trajectories\nLuminara Plants in Different Environments", fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel("Month", fontsize=12)
axes[0].set_ylabel("Growth (cm)", fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(loc='upper left', fontsize=10, title='Environments')

# Annotate significant growth points
axes[0].annotate('Rapid Growth', xy=(6, 90), xytext=(8, 100), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
axes[0].annotate('Peak Growth Plateau', xy=(10, 70), xytext=(11, 85), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')

# Annotate start and end growth values
for start, end in zip([desert_growth[0], temperate_growth[0], rainforest_growth[0]],
                      [desert_growth[-1], temperate_growth[-1], rainforest_growth[-1]]):
    axes[0].annotate(f'{start} cm', (1, start), textcoords="offset points", xytext=(-20, -10), ha='center', fontsize=9, color='dimgray')
    axes[0].annotate(f'{end} cm', (12, end), textcoords="offset points", xytext=(15, -10), ha='center', fontsize=9, color='dimgray')

axes[0].set_xticks(months)

# Second subplot: Bar chart of leaf count
width = 0.25
axes[1].bar(months - width, desert_leaves, width=width, color='#FFD700', label='Desert')
axes[1].bar(months, temperate_leaves, width=width, color='#32CD32', label='Temperate')
axes[1].bar(months + width, rainforest_leaves, width=width, color='#4169E1', label='Rainforest')
axes[1].set_title("Leaf Count Comparison\nAmong Environments", fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel("Month", fontsize=12)
axes[1].set_ylabel("Leaf Count", fontsize=12)
axes[1].legend(loc='upper left', fontsize=10, title='Environments')

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()