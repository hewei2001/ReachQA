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

# Organize the data for plotting
distribution_data = [dragon_dominion, unicorn_valley, mermaid_lagoon, elfwood_forest]

# Define colors
colors = ['#ff6666', '#ffcc99', '#66b3ff', '#99ff99', '#c2c2f0']

# Create the figure for the donut pie charts
fig, ax = plt.subplots(2, 2, figsize=(14, 12), subplot_kw=dict(aspect="equal"))
ax = ax.flatten()

# Plot individual pie charts for each fantasy land
for i, data in enumerate(distribution_data):
    wedges, texts, autotexts = ax[i].pie(
        data, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.85),
        startangle=90, labels=creatures, autopct='%1.1f%%', pctdistance=0.75,
        textprops=dict(color="black", fontsize=9, weight='bold')
    )
    # Draw a circle to create the donut shape
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax[i].add_artist(center_circle)

    # Title for each subplot
    ax[i].set_title(f'{lands[i]}', fontsize=14, pad=20)

# Add a global title
plt.suptitle("Global Fantasy Land Distribution of Mythical Creatures", fontsize=16, fontweight='bold', y=1.02)

# Add a legend to the right of the plot
fig.legend(wedges, creatures, title="Creatures", loc='center right', bbox_to_anchor=(1.1, 0.5))

# Automatically adjust the subplot parameters for better fit
plt.tight_layout(rect=[0, 0.03, 0.9, 0.95])

# Show the chart
plt.show()