import matplotlib.pyplot as plt

# Data for the pie chart representing energy consumption in Techopolis
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Biomass', 'Fossil Fuels']
consumption_percentages = [30, 25, 20, 10, 10, 5]  # Hypothetical percentage of consumption for each energy source

# Distinct colors for each energy source to enhance visualization
colors = ['#ffd700', '#00bfff', '#87ceeb', '#ff6347', '#9acd32', '#d3d3d3']

# Create the plot
fig, ax = plt.subplots()

# Construct the pie chart with an emphasis on Solar energy
wedges, texts, autotexts = ax.pie(
    consumption_percentages, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=[0.1 if source == 'Solar' else 0 for source in energy_sources],  # Slightly explode Solar section
    shadow=True
)

# Enhance text aesthetics for clarity
plt.setp(autotexts, size=10, weight="bold", color="darkgreen")
plt.setp(texts, size=11)

# Ensure the pie chart is drawn as a perfect circle
ax.axis('equal')

# Title highlighting Techopolis' energy future with line breaks for readability
plt.title("Energy Consumption in Techopolis, 2050\nSustainable and Technological Advancements", pad=20, fontsize=14, fontweight='bold', color='darkslateblue')

# Add a legend to describe each energy source, positioned for clarity
ax.legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize='medium')

# Optimize layout to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()