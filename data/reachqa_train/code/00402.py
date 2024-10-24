import matplotlib.pyplot as plt

# Data: percentage share of renewable energy sources in 2023
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
percentages = [35, 25, 18, 12, 10]  # Slightly adjusted for balance

# Colors for each renewable energy source
colors = ['#FFBB33', '#66BB6A', '#42A5F5', '#AB47BC', '#FF7043']

# Create the figure and axis for plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Creating a pie chart with a donut hole
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1 if energy == 'Solar' else 0 for energy in energy_sources],  # Emphasizing 'Solar'
    shadow=True
)

# Setting aesthetic properties for text
plt.setp(autotexts, size=10, weight='bold', color='darkblue')
plt.setp(texts, size=12)

# Ensuring the pie chart is drawn as a circle
ax.axis('equal')

# Descriptive title with line breaks for clarity
plt.title("Green Innovations:\nThe Impact of Renewable Energy Sources\non Global Power Generation (2023)", 
          pad=20, fontsize=14, fontweight='bold', color='darkgreen', ha='center')

# Adding a legend with title, positioned to the right
ax.legend(wedges, energy_sources, title="Energy Sources", loc='center left', 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize='medium', frameon=False)

# Adjust layout to avoid clipping
plt.tight_layout()

# Display the chart
plt.show()