import matplotlib.pyplot as plt
import numpy as np

# Define the fantasy lands and mythical creatures
lands = ["Dragon's Dominion", "Unicorn Valley", "Mermaid Lagoon", "Elfwood Forest"]
creatures = ["Dragons", "Unicorns", "Mermaids", "Elves", "Fairies"]

# Define the creature distribution in each land
dragon_dominion = [60, 10, 5, 15, 10]
unicorn_valley = [5, 70, 5, 10, 10]
mermaid_lagoon = [10, 5, 70, 5, 10]
elfwood_forest = [10, 10, 10, 60, 10]
distribution_data = [dragon_dominion, unicorn_valley, mermaid_lagoon, elfwood_forest]

# Define additional data for overlay line plot: average age of creatures
avg_ages = [
    [300, 50, 100, 400, 200],  # Dragon's Dominion
    [100, 250, 80, 200, 150],  # Unicorn Valley
    [150, 80, 250, 100, 120],  # Mermaid Lagoon
    [120, 100, 90, 300, 110]   # Elfwood Forest
]

# Define colors
colors = ['#ff6666', '#ffcc99', '#66b3ff', '#99ff99', '#c2c2f0']

# Create the figure for the donut pie charts
fig, ax = plt.subplots(2, 2, figsize=(16, 14), subplot_kw=dict(aspect="equal"))
ax = ax.flatten()

# Plot individual pie charts for each fantasy land
for i, data in enumerate(distribution_data):
    wedges, texts, autotexts = ax[i].pie(
        data, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.85),
        startangle=90, labels=creatures, autopct='%1.1f%%', pctdistance=0.75,
        textprops=dict(color="black", fontsize=9, weight='bold')
    )
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax[i].add_artist(center_circle)

    # Line plot overlay
    ax2 = ax[i].twinx()
    ax2.plot(creatures, avg_ages[i], color='darkblue', marker='o', linestyle='-', linewidth=2, markersize=6)
    ax2.set_ylabel('Average Age (years)', color='darkblue', fontsize=10)
    ax2.tick_params(axis='y', labelcolor='darkblue')

    # Title for each subplot
    ax[i].set_title(f'{lands[i]}', fontsize=12, pad=10)

# Add a global title
plt.suptitle("Fantasy Land Creature Distribution and Average Age", fontsize=16, fontweight='bold', y=1.02)

# Adjust layout for better fit and clarity
plt.tight_layout(rect=[0, 0.03, 0.9, 0.95])

# Add a legend to the right of the plot
fig.legend(wedges, creatures, title="Creatures", loc='center right', bbox_to_anchor=(1.2, 0.5))

# Show the chart
plt.show()