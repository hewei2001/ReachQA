import matplotlib.pyplot as plt
import numpy as np

# Define the themes and their respective distribution in percentages
themes = ['Technological Utopia', 'Environmental Apocalypse', 'Cyborg Society', 'Space Exploration', 'Post-Human Evolution']
distribution = np.array([30, 20, 15, 25, 10])

# Define distinct colors for each theme for visual differentiation
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Optional: Explode the first slice for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the sector pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(distribution, labels=themes, autopct='%1.1f%%', startangle=140, colors=colors,
                                  explode=explode, textprops=dict(color="black"))

# Customize the appearance of the text on wedges
plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=9)

# Set the title of the chart, breaking it into two lines for clarity
ax.set_title("Distribution of Themes in Futuristic Literature\n(Last Decade)", fontsize=14, fontweight='bold', pad=20)

# Add a legend to explain the colors used for each theme
ax.legend(wedges, themes, title="Themes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent label occlusion
plt.tight_layout()

# Display the chart
plt.show()