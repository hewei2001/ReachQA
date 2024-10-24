import matplotlib.pyplot as plt

# Define ecosystem names and their oxygen contribution percentages
ecosystems = ['Tropical Rainforests', 'Temperate Forests', 'Oceans', 'Wetlands', 'Grasslands']
oxygen_contribution = [33, 25, 30, 7, 5]

# Define colors for each ecosystem
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create the figure and axis for the ring chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart with a hole in the center to form a ring chart
wedges, texts, autotexts = ax.pie(
    oxygen_contribution, 
    labels=ecosystems, 
    autopct='%1.1f%%',
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),  # Define width for ring effect
    textprops=dict(color="black", fontsize=11)
)

# Central label in the ring
ax.text(0, 0, "Global\nOxygen\nProduction", horizontalalignment='center', 
        verticalalignment='center', fontsize=14, fontweight='bold', color='#555555')

# Add a title with line breaks for readability
plt.title("Earth's Breath: Ecosystem Contributions\nTo Global Oxygen Production",
          fontsize=16, fontweight='bold', pad=20)

# Customize the legend
plt.legend(wedges, ecosystems, title="Ecosystems", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the layout is tight and elements do not overlap
plt.tight_layout()

# Display the ring chart
plt.show()