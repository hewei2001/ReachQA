import matplotlib.pyplot as plt

# Data for mythical creature sightings
creatures = ['Dragons', 'Unicorns', 'Bigfoot', 'Loch Ness Monster', 'Chupacabra']
sightings = [35, 25, 20, 15, 5]

# Colors for each mythical creature
colors = ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9', '#92a8d1']

# Explode the pie slice for Dragons to emphasize it
explode = (0.1, 0, 0, 0, 0)

# Create a pie chart with specified visual details
plt.figure(figsize=(9, 7))
wedges, texts, autotexts = plt.pie(
    sightings, 
    labels=creatures, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    explode=explode,
    pctdistance=0.85,
    shadow=True
)

# Add a central circle for a donut-like appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title of the pie chart, split into two lines for clarity
plt.title("Mythical Creature Sightings\nWorldwide - 2023", fontsize=16, fontweight='bold')

# Beautify the percentage labels inside the pie slices
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Position the legend outside the pie chart
plt.legend(wedges, creatures, title='Creatures', loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the pie chart
plt.show()