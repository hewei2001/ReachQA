import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2014, 2024)
north_america = [5, 8, 12, 18, 26, 35, 47, 60, 74, 90]
europe = [4, 7, 11, 17, 25, 34, 44, 55, 68, 83]
asia = [6, 10, 15, 23, 33, 45, 58, 72, 87, 105]
latin_america = [1, 3, 5, 8, 12, 17, 23, 30, 38, 47]
africa = [0.5, 1, 2, 4, 7, 11, 16, 22, 29, 37]

# Plot
plt.figure(figsize=(12, 8))

plt.plot(years, north_america, label='North America', marker='o', linestyle='-', linewidth=2, color='#1f77b4')
plt.plot(years, europe, label='Europe', marker='s', linestyle='-', linewidth=2, color='#ff7f0e')
plt.plot(years, asia, label='Asia', marker='^', linestyle='-', linewidth=2, color='#2ca02c')
plt.plot(years, latin_america, label='Latin America', marker='D', linestyle='-', linewidth=2, color='#d62728')
plt.plot(years, africa, label='Africa', marker='x', linestyle='-', linewidth=2, color='#9467bd')

# Titles and Labels
plt.title('Decade of Connectivity: Growth of High-Speed Internet Users\n(2014-2023)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Users with Gbps Internet (Millions)', fontsize=12)

# Legend and Grid
plt.legend(title='Region', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

# Improve layout
plt.xticks(years, rotation=45)  # Rotate x-ticks for better visibility
plt.yticks(np.arange(0, 110, 10))
plt.tight_layout()

# Show the plot
plt.show()