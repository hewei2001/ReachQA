import matplotlib.pyplot as plt
import numpy as np

# Define decades from the 1970s to the 2020s
decades = np.arange(1970, 2030, 10)

# Average building heights (in meters) for each city across the decades
new_york_heights = [240, 290, 310, 350, 380, 400]
hong_kong_heights = [150, 250, 300, 330, 360, 400]
dubai_heights = [0, 150, 260, 320, 420, 600]
shanghai_heights = [120, 180, 250, 330, 410, 500]
london_heights = [110, 130, 160, 200, 310, 350]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the line chart for each city
ax.plot(decades, new_york_heights, marker='o', linestyle='-', color='b', linewidth=2, label='New York')
ax.plot(decades, hong_kong_heights, marker='s', linestyle='--', color='r', linewidth=2, label='Hong Kong')
ax.plot(decades, dubai_heights, marker='^', linestyle='-.', color='g', linewidth=2, label='Dubai')
ax.plot(decades, shanghai_heights, marker='D', linestyle=':', color='purple', linewidth=2, label='Shanghai')
ax.plot(decades, london_heights, marker='*', linestyle='-', color='orange', linewidth=2, label='London')

# Titles and labels
ax.set_title('The Evolution of Urban Skyline Heights\n(1970s-2020s)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('Avg Height of Tallest Buildings (meters)', fontsize=14)
ax.set_xticks(decades)

# Grid lines for readability
ax.grid(True, linestyle='--', which='both', color='gray', alpha=0.5)

# Add legend
ax.legend(title='Cities', loc='upper left', fontsize=12)

# Highlight key observations with annotations
ax.annotate('Dubai Explosion', xy=(2020, 600), xytext=(2010, 500),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='g')
ax.annotate('Shanghai Growth', xy=(2020, 500), xytext=(1990, 350),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='purple')

# Adjust layout for visibility
plt.tight_layout()

# Show the plot
plt.show()