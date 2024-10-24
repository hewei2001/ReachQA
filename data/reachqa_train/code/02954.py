import matplotlib.pyplot as plt

# Define mythological creatures and their influence percentages
creatures = ['Dragon', 'Phoenix', 'Unicorn', 'Griffin', 'Kraken', 'Sphinx']
influence_percentages = [30, 20, 15, 10, 15, 10]

# Define colors for each creature
colors = ['#a83232', '#e67300', '#ffcc99', '#99ccff', '#66b3ff', '#c2c2f0']

# Define an explode pattern to highlight the 'Dragon' sector
explode = (0.1, 0, 0, 0, 0, 0)  # Highlight the first sector

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    influence_percentages,
    labels=creatures,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(edgecolor='w', linewidth=1.5),
    textprops=dict(color="black", fontsize=12)
)

# Adjust autotexts to ensure readability
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(10)
    autotext.set_weight("bold")

# Add a title, breaking it into two lines for readability
plt.title('Legends Across Continents:\nInfluence of Mythological Creatures', fontsize=16, pad=20, fontweight='bold')

# Add a legend outside the pie chart to avoid overlap
ax.legend(wedges, creatures, title="Mythical Creatures", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Adjust layout to prevent overlapping of elements
plt.tight_layout()

# Display the chart
plt.show()