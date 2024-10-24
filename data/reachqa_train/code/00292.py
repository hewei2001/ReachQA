import matplotlib.pyplot as plt
import numpy as np

# Define languages and their respective distribution percentages
languages = ['Galactic Common', 'Martian Dialect', 'Venusian Script', 'Io Vernacular', 'Lunar Esperanto', 'Titanian']
distribution = [40, 25, 15, 10, 7, 3]

# Choose a color palette for the chart
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948']

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(distribution, labels=languages, autopct='%1.1f%%', startangle=140, colors=colors,
                                  pctdistance=0.85, wedgeprops=dict(width=0.3), shadow=True)

# Format text size
for text in autotexts:
    text.set_size(10)
for text in texts:
    text.set_size(10)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Customize the title
plt.title("Linguistic Diversity in Harmony-2123\nSpace Station", fontsize=14, fontweight='bold', pad=20)

# Customize legend
plt.legend(wedges, languages, title="Languages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()