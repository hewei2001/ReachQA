import matplotlib.pyplot as plt

# Define the energy sources and their proportions
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
energy_proportions = [35, 30, 20, 10, 5]

# Define colors for each sector to enhance visualization
colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF8C00', '#8A2BE2']

# Explode one of the sectors to highlight it, for example, Solar energy
explode = (0.1, 0, 0, 0, 0)  # 'Solar' sector is exploded

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(energy_proportions, labels=energy_sources, autopct='%1.1f%%', startangle=140, 
                                  colors=colors, explode=explode, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

# Improve readability by styling the text
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')

# Enhance the chart with a title
plt.title('EcoLandia\'s 2023\nSustainable Energy Mix', fontsize=16, fontweight='bold', pad=20)

# Add a legend to the right of the chart
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)

# Add a descriptive note or footer
plt.figtext(0.5, 0.01, "EcoLandia focuses on clean energy reflecting its commitment to sustainability and innovation.",
            ha="center", fontsize=10, fontstyle='italic')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the pie chart
plt.show()