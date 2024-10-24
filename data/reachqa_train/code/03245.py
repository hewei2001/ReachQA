import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])
medieval = np.array([90, 70, 50, 20, 10, 5, 2, 1, 0])
renaissance = np.array([0, 10, 30, 50, 40, 20, 10, 5, 2])
baroque = np.array([0, 0, 5, 20, 30, 40, 30, 15, 5])
neoclassical = np.array([0, 0, 0, 0, 10, 20, 30, 40, 20])
modern = np.array([0, 0, 0, 0, 10, 15, 28, 39, 73])

# Setting up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the area chart
ax.stackplot(years, medieval, renaissance, baroque, neoclassical, modern, 
             labels=["Medieval", "Renaissance", "Baroque", "Neoclassical", "Modern"],
             colors=['#8c564b', '#d62728', '#9467bd', '#2ca02c', '#1f77b4'],
             alpha=0.8)

# Adding titles and labels
ax.set_title("Evolution of Architectural Styles in Archopolis\n(1200-2000)", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Percentage Coverage of Buildings", fontsize=14)

# Customizing the x-ticks
ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], rotation=45, ha='right', fontsize=12)

# Adding a legend
ax.legend(title="Architectural Styles", fontsize=12, loc='upper left')

# Adding gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()