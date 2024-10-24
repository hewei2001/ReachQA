import matplotlib.pyplot as plt

# Extended list of energy sources with subcategories
energy_sources = [
    'Solar - Photovoltaic', 'Solar - Thermal', 
    'Wind - Onshore', 'Wind - Offshore', 
    'Hydropower - Conventional', 'Hydropower - Pumped', 
    'Biomass - Solid', 'Biomass - Liquid',
    'Geothermal', 'Tidal', 'Wave', 'Others'
]

# Corresponding percentages for each subcategory
percentages = [15.5, 14.5, 13, 12, 10, 10, 7, 6, 5, 3, 2, 2]

# Colors for each segment
colors = [
    '#FFD700', '#FFEC8B', # Solar
    '#87CEEB', '#4682B4', # Wind
    '#32CD32', '#228B22', # Hydropower
    '#D2691E', '#8B4513', # Biomass
    '#FF6347', '#6495ED', # Geothermal, Tidal
    '#1E90FF', '#B0C4DE'  # Wave, Others
]

# Explode certain slices
explode = (0.1, 0, 0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(12, 9))
wedges, texts, autotexts = plt.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, explode=explode, wedgeprops={'edgecolor': 'black'}, shadow=True
)

# Format and style the text
for text in texts + autotexts:
    text.set_fontsize(9)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontweight('bold')

# Add a multiline title
plt.title('Detailed Global Distribution of Renewable Energy Sources in 2023\nAnalyzed by Subcategories', fontsize=14, fontweight='bold', pad=20)

# Custom legend on the side
plt.legend(
    wedges, energy_sources, title="Energy Sources", loc='upper right', bbox_to_anchor=(1.2, 1),
    fontsize=10, title_fontsize='11'
)

# Ensure the pie chart is a circle and use tight layout
plt.axis('equal')
plt.tight_layout(rect=[0, 0, 0.9, 1])  # Reserve space for the legend

# Show the plot
plt.show()