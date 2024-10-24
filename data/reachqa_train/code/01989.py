import matplotlib.pyplot as plt
import numpy as np

# Data: Number of space missions in 2025
missions = [40, 35, 25, 20, 15]
countries = ['United States', 'China', 'European Space Agency', 'India', 'Russia']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    missions, labels=countries, colors=colors, startangle=140,
    autopct='%1.1f%%', pctdistance=0.85, wedgeprops=dict(width=0.3),
    textprops={'fontsize': 10, 'color': 'black'}, explode=(0.05, 0.05, 0.05, 0.05, 0.05), shadow=True)

# Customize the title and add it
ax.set_title(
    "Global Space Exploration Missions\nby Country in 2025",
    fontsize=14, weight='bold', wrap=True
)

# Create a legend outside of the pie chart
plt.legend(wedges, countries, title="Countries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()