import matplotlib.pyplot as plt
import numpy as np

# Data: Coffee consumption in millions of tons
consumption = [3.8, 2.9, 2.5, 2.2, 1.1, 0.6]
continents = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania']

# Colors for each continent segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#66FFCC']

# Create explode data to highlight Europe as the largest consumer
explode = (0.1, 0, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    consumption, labels=continents, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, explode=explode, shadow=True,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Customize text properties for better visibility
for text in texts + autotexts:
    text.set_fontsize(10)
    text.set_color('black')

# Add title with multiple lines for better readability
plt.title(
    'Global Coffee Consumption Distribution by Continent\n'
    '(Annual Data in Millions of Tons)', fontsize=14, weight='bold', pad=30
)

# Add a legend outside the plot
plt.legend(
    wedges, continents,
    title="Continents",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Enhance plot layout
plt.tight_layout()

# Display the plot
plt.show()