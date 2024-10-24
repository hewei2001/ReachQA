import matplotlib.pyplot as plt

# Data for the percentage of travelers visiting each ancient wonder
wonders = [
    "Great Pyramid of Giza",
    "Hanging Gardens\nof Babylon",
    "Statue of Zeus\nat Olympia",
    "Temple of Artemis\nat Ephesus",
    "Mausoleum\nat Halicarnassus",
    "Colossus of Rhodes",
    "Lighthouse of Alexandria"
]

percentages = [35, 15, 10, 12, 8, 10, 10]

# Colors for each section
colors = ['#FFDD44', '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#034F84']

# Explode the 'Great Pyramid of Giza' slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=wonders,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.75,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Add a center circle for the donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Improve the aesthetics of the labels and percentages
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Title for the donut pie chart
plt.title('Traveler Interest in Ancient Wonders\n2023 Survey Results', pad=30, fontsize=15, fontweight='bold')

# Legend for the chart
ax.legend(wedges, wonders, title="Ancient Wonders", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the pie chart is displayed as a circle
ax.set_aspect('equal')

# Automatically adjust layout to fit everything properly
plt.tight_layout()

# Show the plot
plt.show()