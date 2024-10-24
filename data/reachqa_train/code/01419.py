import matplotlib.pyplot as plt
import numpy as np

# Data and labels
energy_sources = ['Solar Panels', 'Wind Turbines', 'Hydroelectric Dams', 
                  'Biomass Generators', 'Geothermal Plants']
contributions = [40, 25, 15, 10, 10]  # Contribution percentages

# Define colors for each segment
colors = ['#FFDD44', '#44BBA4', '#5F4BB6', '#FF6F61', '#6CBB3C']

# Plot the donut pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(contributions, labels=energy_sources,
                                  colors=colors, autopct='%1.1f%%',
                                  startangle=90, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3), shadow=True)

# Enhance text properties for better visibility
plt.setp(autotexts, size=10, weight="bold", color='darkblue')
plt.setp(texts, size=10, weight="bold")

# Title with line breaks for better readability
ax.set_title('Ecoopolis Energy Source Distribution\nin 2050', 
             fontsize=16, weight='bold', pad=30)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis('equal')  

# Add a legend
plt.legend(wedges, energy_sources, title="Energy Sources", loc='center left', 
           bbox_to_anchor=(1, 0, 0.5, 1), fontsize='medium')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()