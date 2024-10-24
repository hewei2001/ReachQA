import matplotlib.pyplot as plt

# Data for EcoHaven's energy distribution
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
contributions = [35, 25, 15, 10, 15]
colors = ['#ffcc00', '#99ccff', '#66cc66', '#ff9966', '#99ff99']
explode = (0.1, 0, 0, 0, 0)  # Emphasize the largest contribution: Solar Energy

# Create the pie chart
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(contributions, 
                                   labels=energy_sources, 
                                   autopct='%1.1f%%', 
                                   startangle=140, 
                                   colors=colors, 
                                   explode=explode,
                                   wedgeprops=dict(edgecolor='w'))

# Enhance text properties
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')

# Title and legend
plt.title('EcoHaven City: Renewable Energy Distribution, 2150', fontsize=15, fontweight='bold', pad=20)
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()