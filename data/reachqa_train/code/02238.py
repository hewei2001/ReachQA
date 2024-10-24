import matplotlib.pyplot as plt

# Data for renewable energy sources in green cities by 2035
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
energy_distribution = [35, 25, 20, 10, 10]
colors = ['#FFD700', '#87CEEB', '#228B22', '#CD853F', '#DA70D6']  # Slightly altered colors for richer tones
explode = [0.1, 0, 0, 0, 0]  # Highlighting the Solar energy slice

# Create the donut chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    energy_distribution,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},
    pctdistance=0.85  # Adjusting the placement of the percentage labels
)

# Draw a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Customizing the percentage labels inside the donut chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Additional central text
ax.text(0, 0, '2035\nEnergy Mix', fontsize=14, fontweight='bold', ha='center', va='center')

# Add title and customize legend placement
plt.title("The Future of Green Cities:\nRenewable Energy Sources by 2035", fontsize=18, fontweight='bold', ha='center')
plt.legend(wedges, energy_sources, title="Energy Source", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()