import numpy as np
import matplotlib.pyplot as plt

# Months over a year (January to December)
months = np.arange(1, 13)

# Growth data in centimeters (cm) for each environment
desert_growth = np.array([5, 8, 12, 15, 17, 18, 19, 19, 20, 21, 22, 23])
temperate_growth = np.array([10, 15, 20, 30, 40, 50, 55, 60, 65, 70, 72, 75])
rainforest_growth = np.array([15, 25, 35, 50, 70, 90, 100, 105, 110, 115, 118, 120])

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plot each growth line with distinct styles and colors
plt.plot(months, desert_growth, label='Desert', color='#FFA500', marker='o', linestyle='--', linewidth=2)
plt.plot(months, temperate_growth, label='Temperate', color='#228B22', marker='s', linestyle='-.', linewidth=2)
plt.plot(months, rainforest_growth, label='Rainforest', color='#4682B4', marker='^', linestyle='-', linewidth=2)

# Add title and labels
plt.title("Growth Trajectories of Luminara Plants\nunder Diverse Environmental Conditions", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Growth (cm)", fontsize=14)

# Enhance readability with a grid
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate significant growth points
plt.annotate('Rapid Growth', xy=(6, 90), xytext=(8, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black')

plt.annotate('Peak Growth Plateau', xy=(10, 70), xytext=(11, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='green')

# Add a legend to identify environments
plt.legend(loc='upper left', fontsize=12, title='Environments')

# Annotate start and end growth values for clarity
for i, (start, end) in enumerate(zip([desert_growth[0], temperate_growth[0], rainforest_growth[0]],
                                     [desert_growth[-1], temperate_growth[-1], rainforest_growth[-1]])):
    plt.annotate(f'{start} cm', (1, start), textcoords="offset points", xytext=(-20,-10), ha='center', fontsize=10, color='dimgray')
    plt.annotate(f'{end} cm', (12, end), textcoords="offset points", xytext=(15,-10), ha='center', fontsize=10, color='dimgray')

# Set ticks for x-axis
plt.xticks(months)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()