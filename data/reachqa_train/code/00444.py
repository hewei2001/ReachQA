import matplotlib.pyplot as plt

# Data representing the energy mix in Electroplis, 2050
energy_sources = ['Solar Energy', 'Wind Energy', 'Nuclear Energy', 'Geothermal Energy', 'Fossil Fuels']
energy_percentages = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#87CEEB', '#8A2BE2', '#FF4500', '#708090']

# Exploding the smallest sector for emphasis on Fossil Fuels
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(energy_percentages, labels=energy_sources, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='w'))

# Customizing text appearance
plt.setp(texts, size=12, color='darkblue')
plt.setp(autotexts, size=12, color='white', weight="bold")

# Adding a title to the plot, split across two lines for clarity
plt.title("Electroplis Energy Source Distribution\n(Year 2050)", fontsize=16, fontweight='bold', color='navy', pad=20)

# Add a legend to clearly link colors to energy sources
ax.legend(wedges, energy_sources, title="Energy Types", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10, title_fontsize='12')

# Adjust layout to accommodate the legend and ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()