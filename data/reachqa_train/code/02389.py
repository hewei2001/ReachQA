import matplotlib.pyplot as plt

# Transportation modalities and sub-categories
modalities = ['Warp Drive Ships', 'Hyperspace Capsules', 'Quantum Teleportation Gates', 'Ion Thruster Caravans', 'Space Elevators']
percentages = [40, 25, 20, 10, 5]

# Sub-modalities for each transportation category
sub_modalities = {
    'Warp Drive Ships': [25, 15],           # Interstellar, Intra-system
    'Hyperspace Capsules': [15, 10],        # Personal, Commercial
    'Quantum Teleportation Gates': [10, 10], # Local, Galactic
    'Ion Thruster Caravans': [5, 5],        # Cargo, Passenger
    'Space Elevators': [3, 2]               # Terrestrial, Orbital
}

# Define colors for the main categories and sub-categories
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#32CD32', '#FFD700']
sub_colors = ['#FFA07A', '#5F9EA0', '#9370DB', '#66CDAA', '#FFD700']

# Slightly emphasize the largest sections for visual effect
explode = (0.1, 0.1, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the main ring chart
wedges, texts, autotexts = ax.pie(
    percentages, labels=modalities, autopct='%1.1f%%', startangle=140,
    colors=colors, pctdistance=0.85, wedgeprops=dict(edgecolor='w', linewidth=1.5), explode=explode
)

# Sub-category ring chart on the inner ring
size = 0.3
ax.pie(
    [value for sublist in sub_modalities.values() for value in sublist], radius=1-size,
    colors=sub_colors * len(sub_modalities), startangle=140,
    wedgeprops=dict(width=size, edgecolor='w', linewidth=1.5)
)

# Add aesthetics to the chart text
plt.setp(autotexts, size=10, weight="bold", color="white")
for text in texts:
    text.set_fontsize(10)

# Add a central circle to create the doughnut effect
centre_circle = plt.Circle((0, 0), 1-size, fc='white')
ax.add_artist(centre_circle)

# Set the title with multiple lines
plt.title('Galactic Transportation Modalities in 2145\nExploring Interstellar Travel Diversity',
          fontsize=15, fontweight='bold', pad=20)

# Legend positioning to avoid overlap
ax.legend(wedges, modalities, title="Modalities", loc="center left", bbox_to_anchor=(1, 0.5))

# Use tight_layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()