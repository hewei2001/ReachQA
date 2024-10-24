import matplotlib.pyplot as plt

# Data for renewable energy sources in green cities by 2035
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
energy_distribution = [35, 25, 20, 10, 10]
colors = ['#ffcc00', '#99ccff', '#339966', '#cc6600', '#cc33cc']
explode = [0.1, 0, 0, 0, 0]  # Highlighting the Solar energy slice

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    energy_distribution,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Customize the percentage labels inside the pie chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add title and customize legend placement
plt.title("The Future of Green Cities:\nRenewable Energy Sources by 2035", fontsize=16, fontweight='bold')
plt.legend(wedges, energy_sources, title="Energy Source", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()