import matplotlib.pyplot as plt
import numpy as np

# Decades from 1500s to 1590s
decades = np.arange(1500, 1600, 10)

# Popularity Index (from 0 to 100) for each fashion element
ruff_collars = [10, 15, 25, 35, 50, 60, 75, 85, 90, 95]
puffed_sleeves = [5, 20, 40, 55, 65, 70, 65, 50, 35, 25]
brocade_fabrics = [20, 30, 35, 45, 55, 65, 75, 80, 85, 90]

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(decades, ruff_collars, marker='o', linestyle='-', color='midnightblue', linewidth=2, label='Ruff Collars')
plt.plot(decades, puffed_sleeves, marker='s', linestyle='--', color='indianred', linewidth=2, label='Puffed Sleeves')
plt.plot(decades, brocade_fabrics, marker='^', linestyle=':', color='darkgoldenrod', linewidth=2, label='Brocade Fabrics')

# Adding data annotations
for i, val in enumerate(ruff_collars):
    plt.text(decades[i], ruff_collars[i] + 2, str(val), ha='center', va='bottom', fontsize=9, color='midnightblue')
for i, val in enumerate(puffed_sleeves):
    plt.text(decades[i], puffed_sleeves[i] + 2, str(val), ha='center', va='bottom', fontsize=9, color='indianred')
for i, val in enumerate(brocade_fabrics):
    plt.text(decades[i], brocade_fabrics[i] + 2, str(val), ha='center', va='bottom', fontsize=9, color='darkgoldenrod')

# Customize plot
plt.title('Renaissance Fashion Trends\nThrough the Decades: 1500s to 1590s', fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=14)
plt.ylabel('Popularity Index', fontsize=14)
plt.xticks(decades)
plt.yticks(np.arange(0, 101, 10))
plt.legend(title='Fashion Elements', loc='upper left', fontsize=12)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout to avoid clipping
plt.tight_layout()

# Show plot
plt.show()