import matplotlib.pyplot as plt

# Define renewable energy sources and their urban usage distribution percentages
energy_sources = ['Solar Power', 'Wind Power', 'Hydroelectric Power', 'Geothermal Energy', 'Biomass Energy']
energy_distribution = [35, 25, 20, 10, 10]

# Colors for each energy sector
colors = ['#ffd700', '#87cefa', '#8a2be2', '#ff4500', '#228b22']

# Highlight the "Solar Power" sector with an explode
explode = (0.1, 0, 0, 0, 0)

# Create the figure and axis for the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    energy_distribution,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode
)

# Customize text properties for readability
plt.setp(texts, size=10, weight="bold", color='darkgreen')
plt.setp(autotexts, size=9, weight="bold", color='white')

# Set title, adjusting for length with line breaks
ax.set_title('Urban Areas: Renewable Energy Adoption in 2023', 
             fontsize=14, fontweight='bold', color='darkblue', pad=20)

# Add a legend, ensuring it does not occlude chart elements
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9, title_fontsize=11)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the chart
plt.show()