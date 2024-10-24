import matplotlib.pyplot as plt

# Data: Cuisines and their interest percentages
cuisines = [
    "Italian", "Mexican", "Japanese", "Indian",
    "French", "Mediterranean", "Chinese", "Thai",
    "American", "Middle Eastern"
]

interest_percentages = [15, 12, 10, 18, 8, 9, 11, 7, 5, 5]

# Colors for each cuisine type
colors = [
    "#FF9999", "#66B3FF", "#99FF99", "#FFCC99",
    "#FFD700", "#FF69B4", "#8A2BE2", "#40E0D0",
    "#FFA07A", "#DEB887"
]

# Explode the "Indian" cuisine slice slightly for emphasis
explode = [0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0]

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    interest_percentages,
    explode=explode,
    labels=cuisines,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w')
)

# Customizing the text labels
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')

# Add a center circle for a donut chart look
center_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', linewidth=0)
fig.gca().add_artist(center_circle)

# Title
ax.set_title(
    'Culinary Trends of 2023: Global Cuisine Interests',
    fontsize=16,
    fontweight='bold',
    pad=30
)

# Ensure the layout is adjusted well
plt.tight_layout()

# Show the plot
plt.show()