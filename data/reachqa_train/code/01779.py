import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch

# Topics and corresponding fictional interest data
topics = [
    'Mars Colonization',
    'Search for Extraterrestrial Intelligence',
    'Habitability of Exoplanets',
    'Microbial Life on Icy Moons',
    'Evolution in Extreme Environments'
]

interest_percentages = [25, 20, 30, 15, 10]

# Gradient colors
colors = ['#FF6F61', '#FF6F61', '#88B04B', '#F7CAC9', '#92A8D1']
cmap = plt.get_cmap('coolwarm')

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Create wedges with gradient colors
wedges, texts, autotexts = ax.pie(
    interest_percentages,
    labels=topics,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1 if percentage > 20 else 0.05 for percentage in interest_percentages],
    shadow=True  # Set shadow parameter directly in pie()
)

# Apply gradient colors to wedges
for i, wedge in enumerate(wedges):
    wedge.set_facecolor(cmap(i / len(wedges)))

# Customizing annotation text style and additional annotations
for i, autotext in enumerate(autotexts):
    autotext.set_color('black')
    autotext.set_weight('bold')
    if interest_percentages[i] > 20:
        autotext.set_text(f"{autotext.get_text()}\n(High Interest)")
    autotext.set_fontsize(10)

# Central circle for donut shape
centre_circle = plt.Circle((0,0),0.70,fc='white', linewidth=0)
ax.add_artist(centre_circle)

# Title and context
plt.title("Astrobiology Interests Among\nSpace Enthusiasts in 2050", fontsize=16, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Legend outside of plot
ax.legend(wedges, topics, title="Topics", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Enhance layout to avoid text overlap
plt.subplots_adjust(left=0.1, right=0.85)

# Display the chart
plt.show()