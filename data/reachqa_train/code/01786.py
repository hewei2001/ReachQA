import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define original data: centuries and Language Complexity Index
centuries = np.array([5, 9, 14, 15, 17, 19, 20, 21])
complexity_index = np.array([3, 3.5, 4, 5, 6, 7, 8, 9])

# New data: Cultural Influence Index (hypothetical)
cultural_influence = np.array([2, 3, 3.8, 4.5, 5.5, 6.5, 7.5, 8.5])

# Create a smooth curve for Language Complexity using B-Spline
x_new = np.linspace(centuries.min(), centuries.max(), 300)
spl_complexity = make_interp_spline(centuries, complexity_index, k=3)
smooth_complexity = spl_complexity(x_new)

# Set up the plot
plt.figure(figsize=(14, 8))

# Plot scatter points for Language Complexity
plt.scatter(centuries, complexity_index, color='indigo', s=100, label='Key Centuries', zorder=3)

# Plot smooth curve for Language Complexity
plt.plot(x_new, smooth_complexity, color='mediumslateblue', linestyle='-', linewidth=3, label='Complexity Trend', zorder=2)

# Overlay: Bar Plot for Cultural Influence
plt.bar(centuries, cultural_influence, width=0.5, color='lightcoral', alpha=0.6, label='Cultural Influence Index', zorder=1)

# Customize plot details
plt.title("Evolution of Language Complexity and Cultural Influence\nThrough Centuries", fontsize=16, fontweight='bold')
plt.xlabel("Century", fontsize=13)
plt.ylabel("Index Value", fontsize=13)
plt.xticks(centuries, [f'{c}th Century' for c in centuries], rotation=45)
plt.ylim(0, 10)
plt.xlim(4, 22)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6, zorder=0)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()