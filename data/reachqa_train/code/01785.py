import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the centuries and hypothetical Language Complexity Index
centuries = np.array([5, 9, 14, 15, 17, 19, 20, 21])
complexity_index = np.array([3, 3.5, 4, 5, 6, 7, 8, 9])

# Create a smooth curve through scatter points using B-Spline
x_new = np.linspace(centuries.min(), centuries.max(), 300)
spl = make_interp_spline(centuries, complexity_index, k=3)
smooth_complexity = spl(x_new)

# Set up the plot
plt.figure(figsize=(14, 8))

# Plot scatter points
plt.scatter(centuries, complexity_index, color='indigo', s=100, label='Key Centuries', zorder=3)

# Plot smooth fitting curve
plt.plot(x_new, smooth_complexity, color='mediumslateblue', linestyle='-', linewidth=3, label='Complexity Trend', zorder=2)

# Customize plot details
plt.title("Evolution of Language Complexity\nThrough Centuries", fontsize=16, fontweight='bold')
plt.xlabel("Century", fontsize=13)
plt.ylabel("Language Complexity Index", fontsize=13)
plt.xticks(centuries, [f'{c}th Century' for c in centuries])
plt.ylim(2, 10)
plt.xlim(4, 22)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6, zorder=1)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()