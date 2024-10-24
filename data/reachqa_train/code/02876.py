import matplotlib.pyplot as plt
import numpy as np

# Data: Countries and number of space missions launched
countries = ['Asteria', 'Cosmica', 'Galaxia', 'Nova', 'Celestia', 'Orion']
missions = [45, 30, 25, 20, 15, 10]  # Number of missions

# Colors for each country
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Explode a slice to emphasize the largest contributor
explode = (0.1, 0, 0, 0, 0, 0)  # Explode the first slice (Asteria)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(missions, labels=countries, autopct='%1.1f%%', startangle=90, colors=colors,
                                  explode=explode, shadow=True, textprops=dict(color="w"))

# Enhance text appearance
plt.setp(autotexts, size=12, weight="bold")
plt.setp(texts, size=10)

# Title for the pie chart
ax.set_title('Global Space Exploration\nMissions by Country (2010-2020)', fontsize=16, fontweight='bold', color='navy')

# Add legend with mission counts
ax.legend(wedges, [f"{country}: {mission} missions" for country, mission in zip(countries, missions)],
          title="Countries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10, title_fontsize=12)

# Equal aspect ratio ensures that pie chart is a circle
ax.set_aspect('equal')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()