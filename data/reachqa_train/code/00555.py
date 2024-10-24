import matplotlib.pyplot as plt

# Energy sources and their production percentages in EnergiaLand
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Nuclear Energy', 'Natural Gas', 'Coal']
production_percentages = [25, 20, 15, 10, 18, 7, 5]

# Color palette for each energy source
colors = ['#FFD700', '#87CEEB', '#00CED1', '#32CD32', '#8A2BE2', '#FF6347', '#A9A9A9']

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(production_percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90, colors=colors, explode=[0.1, 0, 0, 0, 0, 0, 0], shadow=True)

# Add title with a line break for improved readability
plt.title('Energy Production Diversity\nin EnergiaLand: 2023', fontsize=16, fontweight='bold', pad=20)

# Position the legend outside the pie chart
plt.legend(energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout for clarity and prevent overlap
plt.tight_layout()

# Display the chart
plt.show()