import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

# Define the sectors and their corresponding funding percentages
sectors = [
    'Natural Language Processing', 
    'Computer Vision', 
    'Robotics', 
    'Machine Learning Algorithms', 
    'AI in Healthcare'
]
funding_percentages = [30, 25, 20, 15, 10]

# Define colors and use patterns for added visual complexity
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
hatches = ['/', '\\', '|', '-', '+']

# Explode the first sector slightly for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(12, 10), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    funding_percentages, 
    explode=explode, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='w', hatch=hatches), 
    pctdistance=0.8
)

# Customize text properties for better readability
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add annotations for additional insights
annotations = [
    "Leader in AI research",
    "Vision improvements",
    "Automating tasks",
    "Core ML algorithms",
    "Healthcare transformations"
]
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.radians(angle))
    y = np.sin(np.radians(angle))
    ax.annotate(
        annotations[i], xy=(x, y), xytext=(1.4*x, 1.4*y),
        arrowprops=dict(facecolor='grey', shrink=0.05),
        fontsize=10, ha='center', va='center'
    )

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Title with a clear break for readability
plt.title('Distribution of Research Funding\nin AI Sectors - 2023', fontsize=16, fontweight='bold', pad=20)

# Add a legend with icons or extra details
ax.legend(
    wedges, sectors, title="AI Sectors", loc="center left", 
    bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True
)

# Add a subtle gradient background for depth
fig.patch.set_facecolor('#f0f0f5')
ax.set_facecolor('#ffffff')
ax.patch.set_alpha(0.7)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()