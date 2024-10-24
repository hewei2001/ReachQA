import matplotlib.pyplot as plt

# Define continents and their respective attractions breakdown
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Australia', 'Antarctica']
attraction_types = ['Natural Wonders', 'Cultural Heritage', 'Tech Innovations', 'Adventure Tourism']

# Data: each sublist corresponds to the attraction distribution for a continent
data = [
    [30, 30, 25, 15],  # Asia
    [20, 35, 30, 15],  # Europe
    [25, 20, 40, 15],  # North America
    [35, 25, 20, 20],  # South America
    [40, 30, 15, 15],  # Africa
    [30, 20, 30, 20],  # Australia
    [50, 0, 20, 30]    # Antarctica
]

# Colors for each type of attraction
colors = ['#4CAF50', '#FF5733', '#3498DB', '#F1C40F']

# Create subplots for each continent
fig, axes = plt.subplots(2, 4, figsize=(18, 9))
fig.suptitle('Interstellar Tourism Attractions by Continent:\nA Glimpse into Earth’s Diverse Offerings - 2075',
             fontsize=16, fontweight='bold')

for i, ax in enumerate(axes.flat):
    if i < len(continents):
        ax.pie(data[i], labels=attraction_types, autopct='%1.1f%%', startangle=90,
               colors=colors, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 9},
               explode=(0.05, 0, 0, 0))  # Slightly explode the first segment for emphasis
        ax.set_title(continents[i], fontsize=12, fontweight='bold')
    else:
        ax.axis('off')  # Hide any extra subplot space

# Add a legend for attraction types
fig.legend(attraction_types, loc='center right', fontsize=10, title='Attraction Types', bbox_to_anchor=(1.2, 0.5))

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()