import matplotlib.pyplot as plt
import numpy as np

# Define salary data for various cities
cities = ['New York', 'Tokyo', 'Paris', 'Dubai', 'Sydney']
salaries = [
    [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    [60, 65, 70, 72, 78, 80, 82, 88, 95, 100, 102, 110],
    [55, 60, 65, 68, 70, 72, 75, 80, 85, 90, 95, 98],
    [50, 55, 60, 65, 70, 78, 82, 90, 100, 110, 120, 130],
    [68, 72, 74, 76, 78, 80, 85, 88, 90, 94, 98, 102]
]

# Create a horizontal boxplot
plt.figure(figsize=(12, 8))
boxprops = dict(linestyle='-', linewidth=2)
flierprops = dict(marker='o', color='red', alpha=0.5)
medianprops = dict(linestyle='-', linewidth=2.5, color='orange')

bp = plt.boxplot(salaries, vert=False, patch_artist=True, labels=cities,
                 boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, notch=True)

# Color each box differently
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Titles and labels
plt.title("Architectural Salary Distribution Across Key Global Cities\nInsight into Variability of Earnings", 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Salary in Thousands (USD)", fontsize=12)
plt.ylabel("Cities", fontsize=12)

# Customizing the grid and layout
plt.grid(linestyle='--', alpha=0.7, axis='x')
plt.xticks(np.arange(50, 140, step=10))
plt.yticks(fontsize=11)
plt.tight_layout()

# Add a note
plt.figtext(0.1, 0.02, "Note: Data is illustrative and does not represent actual current salaries.", 
            fontsize=9, color='grey', ha='left')

# Display the plot
plt.show()