import matplotlib.pyplot as plt

# Define regions and coffee flavor preferences (percentage)
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Australia']
preferences = {
    'Rich & Bold': [35, 45, 25, 15, 40, 30],
    'Fruity & Floral': [20, 10, 25, 40, 15, 25],
    'Nutty & Sweet': [30, 25, 30, 20, 30, 25],
    'Earthy & Spicy': [15, 20, 20, 25, 15, 20]
}

# Compute the total preference per region
total_preferences = {region: sum(preferences[flavor][i] for flavor in preferences) for i, region in enumerate(regions)}

# Calculate the relative proportions for each region
flavor_ratios = {flavor: [prefs[i] / total_preferences[region] for i, region in enumerate(regions)] for flavor, prefs in preferences.items()}

# Colors for each flavor
colors = ['#D2691E', '#FFB6C1', '#DAA520', '#8B4513']

# Initialize a figure
fig, axs = plt.subplots(2, 3, figsize=(16, 10))
axs = axs.flatten()

# Plot a pie chart for each region
for ax, region, idx in zip(axs, regions, range(len(regions))):
    wedges, texts, autotexts = ax.pie(
        [flavor_ratios[flavor][idx] for flavor in preferences],
        labels=[flavor for flavor in preferences],
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        explode=[0.05 if flavor_ratios['Fruity & Floral'][idx] > 0.3 else 0 for flavor in preferences]
    )
    # Beautify texts
    for text in texts + autotexts:
        text.set_fontsize(9)
        if text in autotexts:
            text.set_color('black')
            text.set_fontweight('bold')

    # Set title for each subplot
    ax.set_title(region, fontsize=11, weight='bold')

# Set the super title for the figure
fig.suptitle("Evolving Flavors: Coffee Preferences Worldwide (2023)", fontsize=18, fontweight='bold')

# Adjust layout for better spacing
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the chart
plt.show()