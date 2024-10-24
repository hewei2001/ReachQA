import matplotlib.pyplot as plt

# Define energy sources and their distribution
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Biomass', 'Fossil Fuels', 'Nuclear']
energy_distribution = [25, 20, 15, 10, 20, 10]

# Define distinct colors for each sector
colors = ['#FFDB58', '#32CD32', '#4682B4', '#8B4513', '#808080', '#B0C4DE']

# Create a figure for the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))

# Create the donut pie chart
wedges, texts, autotexts = ax.pie(
    energy_distribution, labels=energy_sources, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05),
    wedgeprops=dict(width=0.3), shadow=True
)

# Customize text appearance for the pie chart
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Ensure the pie chart is a circle
ax.axis('equal')

# Add title to the pie chart
ax.set_title('Energy Mix in a Sustainable City\n2023', fontsize=16, fontweight='bold', pad=20)

# Add a legend for clarity
ax.legend(wedges, energy_sources, loc='center left', bbox_to_anchor=(0.9, 0.5), title="Energy Sources", fontsize='small', title_fontsize='13')

# Automatically adjust layout for a clear presentation
plt.tight_layout()

# Display the chart
plt.show()