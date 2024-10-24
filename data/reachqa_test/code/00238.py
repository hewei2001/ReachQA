import matplotlib.pyplot as plt
import numpy as np

# Define the energy types and their corresponding percentage shares
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
percentage_shares = [35, 30, 20, 10, 5]

# Define actual energy production in TWh
production_twh = [1400, 1200, 800, 400, 200]

# Colors for each energy source
colors = ['#FFD700', '#ADD8E6', '#87CEFA', '#98FB98', '#FFB6C1']

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Define the explode setting to slightly separate the 'Solar' segment for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the donut pie chart
wedges, texts, autotexts = axes[0].pie(
    percentage_shares,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3)
)

# Adjust text properties for better readability
for text in texts:
    text.set_fontsize(11)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')

# Add a central circle to maintain the donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axes[0].add_artist(centre_circle)

# Ensure equal aspect ratio
axes[0].axis('equal')

# Add a title to the donut chart
axes[0].set_title(
    'Global Renewable Energy Sources\nPercentage Distribution (2023)',
    fontsize=13,
    fontweight='bold',
    pad=20
)

# Create a bar chart for actual production in TWh
bars = axes[1].bar(
    energy_sources,
    production_twh,
    color=colors,
    edgecolor='grey'
)

# Add text labels for each bar
for bar in bars:
    height = bar.get_height()
    axes[1].annotate(
        f'{height} TWh',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords='offset points',
        ha='center',
        va='bottom',
        fontsize=10
    )

# Set bar chart labels and title
axes[1].set_ylabel('Energy Production (TWh)', fontsize=11)
axes[1].set_title(
    'Actual Renewable Energy Production\n(Terawatt Hours)',
    fontsize=13,
    fontweight='bold',
    pad=20
)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()