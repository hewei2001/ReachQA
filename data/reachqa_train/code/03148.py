import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal', 'Ocean']
energy_share = [30, 25, 20, 15, 5, 5]

# Colors for the pie chart
colors = ['#FFD700', '#87CEEB', '#00FA9A', '#8B4513', '#FF6347', '#4682B4']

# Explode the slices with varying degrees
explode = (0.1, 0.05, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 8))

# Pie chart
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=explode, shadow=True,
    textprops=dict(color='black', weight='bold')
)

# Enhanced text styling
plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=12)

# Title setup
ax.set_title(
    "Global Renewable Energy Mix in 2050:\nA Visionary Outlook for a Sustainable Future", 
    fontsize=16, fontweight='bold', pad=30, multialignment='center'
)

# Add an annotation for a specific insight
ax.annotate('Solar Energy leads with\nsignificant potential growth', xy=(0.9, 0.5), xytext=(1.3, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkblue', weight='bold')

# Legend customization
ax.legend(
    wedges, energy_sources, title="Energy Sources", loc="center left", 
    bbox_to_anchor=(1.2, 0.5, 0.5, 1), fontsize=10
)

# Final layout adjustment
plt.tight_layout()

# Display the plot
plt.show()