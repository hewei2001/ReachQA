import matplotlib.pyplot as plt
import numpy as np

# Data setup
bees_visits = [50, 20, 40, 10, 30]
butterflies_visits = [10, 15, 5, 25, 10]
hummingbirds_visits = [5, 30, 5, 20, 15]
flowers = ['Roses', 'Lilies', 'Sunflowers', 'Tulips', 'Daisies']

# Additional metric: Average size of pollinators (as a fictional example)
pollinator_sizes = {'Bees': [1, 0.8, 0.9, 0.5, 0.6],
                    'Butterflies': [0.6, 0.7, 0.5, 0.9, 0.6],
                    'Hummingbirds': [0.4, 1.0, 0.4, 0.8, 0.7]}

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each pollinator group with enhanced visuals
ax.scatter(flowers, bees_visits, color='gold', s=np.array(bees_visits) * 10, alpha=0.7,
           edgecolor='black', linewidth=0.5, label='Bees', marker='o')
ax.scatter(flowers, butterflies_visits, color='coral', s=np.array(butterflies_visits) * 10, alpha=0.7,
           edgecolor='black', linewidth=0.5, label='Butterflies', marker='^')
ax.scatter(flowers, hummingbirds_visits, color='lightblue', s=np.array(hummingbirds_visits) * 10, alpha=0.7,
           edgecolor='black', linewidth=0.5, label='Hummingbirds', marker='s')

# Annotate points
for i, flower in enumerate(flowers):
    ax.annotate(f"{bees_visits[i]}", (flowers[i], bees_visits[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9)
    ax.annotate(f"{butterflies_visits[i]}", (flowers[i], butterflies_visits[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9)
    ax.annotate(f"{hummingbirds_visits[i]}", (flowers[i], hummingbirds_visits[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9)

# Customize plot
ax.set_title('Diversity of Pollinators & Floral Preferences\nin Urban Gardens', fontsize=14, fontweight='bold')
ax.set_xlabel('Flower Types', fontsize=12)
ax.set_ylabel('Average Visits per Hour', fontsize=12)
ax.set_ylim(0, max(bees_visits) + 10)  # Add some padding to y-limit
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
ax.legend(title='Pollinator Groups', loc='upper right', fontsize=10)

# Create secondary plot for the average size
ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

# Plotting additional metric with a line plot
for key, sizes in pollinator_sizes.items():
    ax2.plot(flowers, sizes, linestyle='--', linewidth=1.5, label=f'{key} Size', alpha=0.5)

ax2.set_ylabel('Average Pollinator Size', fontsize=12)
ax2.legend(loc='lower center', fontsize=10, ncol=3)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()