import matplotlib.pyplot as plt

# Mythical creatures and their belief percentages by continent
belief_distribution = {
    "Asia": [30, 20, 15, 5, 5, 25],  # Dragons, Unicorns, Phoenixes, Yeti, Loch Ness Monster, Chupacabra
    "Europe": [20, 30, 10, 10, 25, 5],
    "North America": [10, 10, 5, 15, 5, 55],
    "South America": [5, 5, 5, 5, 5, 75],
    "Africa": [15, 25, 20, 5, 10, 25],
    "Oceania": [5, 10, 15, 20, 30, 20]
}

creatures = ["Dragons", "Unicorns", "Phoenixes", "Yeti", "Loch Ness Monster", "Chupacabra"]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)  # Exploding the first slice for emphasis

# Plotting the pie charts
fig, ax = plt.subplots(2, 3, figsize=(14, 10))
fig.suptitle("Distribution of Belief in Mythical Creatures\nby Continent", fontsize=16, weight='bold')

for idx, (continent, beliefs) in enumerate(belief_distribution.items()):
    row, col = divmod(idx, 3)
    wedges, texts, autotexts = ax[row, col].pie(
        beliefs, labels=creatures, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True
    )
    # Customize text
    for text in texts:
        text.set_fontsize(8)
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(10)

    ax[row, col].set_title(continent, fontsize=12, weight='bold')
    ax[row, col].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Remove any extra subplot axes (if fewer data categories than subplots)
for i in range(len(belief_distribution), ax.size):
    fig.delaxes(ax.flatten()[i])

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()