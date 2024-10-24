import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# Define civilizations and their hypothetical contribution percentages
civilizations = ['Mesopotamia', 'Ancient Egypt', 'Indus Valley', 'Ancient China', 'Mesoamerican']
contributions = [25, 20, 18, 27, 10]  # Hypothetical data for illustration

# Create gradient-like colors for each civilization
colors = [
    '#e63946', '#f1faee', '#a8dadc', '#457b9d', '#2a9d8f'
]
dark_colors = [
    '#9b2226', '#a8dadc', '#457b9d', '#1d3557', '#006d5b'
]

# Create a figure for the ring chart
fig, ax = plt.subplots(figsize=(12, 9), subplot_kw=dict(aspect="equal"))

# Create the ring chart with gradient effect
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=civilizations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),
    pctdistance=0.85
)

# Add inner circle for a donut effect
inner_circle = Circle((0, 0), 0.55, color='white', zorder=1)
ax.add_artist(inner_circle)

# Enhance text readability
plt.setp(texts, size=11, fontweight='bold', color='black')
plt.setp(autotexts, size=10, color='black', fontweight='light')

# Add historical context annotations
annotations = [
    "Cuneiform", "Pyramids", "Urban Planning", "Paper Making", "Calendars"
]
for i, txt in enumerate(texts):
    txt.set_text(f"{txt.get_text()}:\n{annotations[i]}")

# Central label with thematic typography
ax.text(0, 0, 'Tech\nContributions', horizontalalignment='center',
        verticalalignment='center', fontsize=14, fontweight='bold', color='black')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Add a subtle background pattern
ax.set_facecolor("#f0ece2")

# Title of the chart, split into two lines
ax.set_title("Ancient Civilizations'\nTechnological Contributions",
             fontsize=18, fontweight='bold', pad=30)

# Adjust layout to fit all elements nicely
plt.tight_layout()

# Show the optimized chart
plt.show()