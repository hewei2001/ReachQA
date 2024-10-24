import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Average comfort ratings and technology index over decades
decades = np.array([1980, 1990, 2000, 2010, 2020])
comfort_ratings = np.array([3.5, 4.0, 6.0, 7.5, 8.8])  # Ratings out of 10
technology_index = np.array([1.0, 2.0, 3.5, 4.5, 7.0])  # Hypothetical index out of 10

# Create a smooth fitting curve for comfort ratings
decades_new = np.linspace(decades.min(), decades.max(), 300)
spl_comfort = make_interp_spline(decades, comfort_ratings, k=3)
comfort_smooth = spl_comfort(decades_new)

# Create a smooth fitting curve for technology index
spl_tech = make_interp_spline(decades, technology_index, k=3)
technology_smooth = spl_tech(decades_new)

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Scatter plot for original comfort ratings
ax1.scatter(decades, comfort_ratings, color='red', label='Comfort Ratings', zorder=5, s=100)
ax1.plot(decades_new, comfort_smooth, color='blue', linestyle='-', linewidth=2, label='Comfort Trend')

# Annotate key points with decade markers
for i, (x, y) in enumerate(zip(decades, comfort_ratings)):
    ax1.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, weight='bold')

# Secondary axis for technology index
ax2 = ax1.twinx()
ax2.plot(decades_new, technology_smooth, color='green', linestyle='--', linewidth=2, label='Tech Index Trend')
ax2.scatter(decades, technology_index, color='orange', label='Technology Index', zorder=5, s=100, marker='s')

# Annotations for technology index
for i, (x, y) in enumerate(zip(decades, technology_index)):
    ax2.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9, weight='bold')

# Titles and labels
plt.title('The Evolution of Running Shoe Comfort and Technology:\nA Decadal Perspective', fontsize=16, weight='bold')
ax1.set_xlabel('Decade', fontsize=14)
ax1.set_ylabel('Comfort Rating (Out of 10)', fontsize=14, color='blue')
ax2.set_ylabel('Technology Index (Out of 10)', fontsize=14, color='green')

ax1.set_xticks(decades)
ax1.set_xticklabels([f"{d}s" for d in decades], fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax2.tick_params(axis='y', labelcolor='green')
ax1.set_xlim(decades.min() - 5, decades.max() + 5)
ax1.set_ylim(3, 10)
ax2.set_ylim(0, 8)

# Legends
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Grid
ax1.grid(visible=True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()