import matplotlib.pyplot as plt
import numpy as np

# Define the months for x-axis
months = np.arange(1, 13)

# Distances covered in km for each rover, monthly
curiosity_distances = [0.9, 1.2, 1.5, 1.1, 1.6, 1.4, 1.5, 1.3, 1.1, 1.2, 1.4, 1.7]
opportunity_distances = [1.0, 1.3, 1.4, 1.2, 1.8, 1.7, 1.9, 1.5, 1.4, 1.6, 1.5, 1.6]
perseverance_distances = [1.5, 1.6, 1.8, 1.5, 2.0, 1.9, 2.1, 1.8, 1.7, 1.9, 2.0, 2.2]
spirit_distances = [0.8, 1.0, 1.2, 0.9, 1.3, 1.2, 1.1, 0.9, 1.0, 1.1, 1.3, 1.4]

# Standard deviation errors for distance covered
curiosity_errors = [0.1] * 12
opportunity_errors = [0.12] * 12
perseverance_errors = [0.15] * 12
spirit_errors = [0.08] * 12

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot each rover's distances with error bars
ax.errorbar(months, curiosity_distances, yerr=curiosity_errors, label='Curiosity',
            fmt='-o', capsize=5, color='blue', alpha=0.8)
ax.errorbar(months, opportunity_distances, yerr=opportunity_errors, label='Opportunity',
            fmt='-s', capsize=5, color='orange', alpha=0.8)
ax.errorbar(months, perseverance_distances, yerr=perseverance_errors, label='Perseverance',
            fmt='-^', capsize=5, color='green', alpha=0.8)
ax.errorbar(months, spirit_distances, yerr=spirit_errors, label='Spirit',
            fmt='-d', capsize=5, color='red', alpha=0.8)

# Customizing the plot
ax.set_title('Monthly Distance Coverage by Space Rovers\nAcross Planetary Terrains', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Distance Covered (km)', fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10)
ax.legend(title='Rovers', fontsize=10, loc='upper left')

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for visual appeal
plt.tight_layout()

# Show the plot
plt.show()