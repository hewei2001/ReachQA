import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2024)
epic_fantasy = [70, 72, 74, 78, 75, 80, 85, 83, 88, 90, 87]
urban_fantasy = [50, 55, 58, 62, 64, 68, 72, 70, 68, 65, 63]
dark_fantasy = [30, 35, 37, 40, 45, 50, 55, 53, 57, 60, 58]
historical_fantasy = [25, 30, 28, 32, 36, 38, 42, 45, 48, 50, 52]
romantic_fantasy = [10, 12, 15, 20, 22, 25, 30, 35, 33, 30, 28]

# Plot creation
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting area chart using stackplot
ax.stackplot(years, epic_fantasy, urban_fantasy, dark_fantasy, historical_fantasy, romantic_fantasy,
             labels=['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Historical Fantasy', 'Romantic Fantasy'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
             alpha=0.8)

# Customize chart
ax.set_title('Popularity Trends in Fantasy Novel Genres\nOver the Decade (2013-2023)', fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.legend(loc='upper left', title='Genres', frameon=True, fontsize=10)

# Additional styling for clarity and aesthetics
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Improving the layout
plt.tight_layout()

# Display the plot
plt.show()