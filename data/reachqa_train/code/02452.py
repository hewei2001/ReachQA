import matplotlib.pyplot as plt

# Authors and their influence scores
authors = [
    "Arthur C. Clarke",
    "Isaac Asimov",
    "Philip K. Dick",
    "H.G. Wells",
    "Jules Verne"
]

# Influence scores (fictional representation)
influence_scores = [30, 25, 20, 15, 10]

# Colors for each sector
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#8e44ad']

# Explode one of the slices for emphasis
explode = (0.1, 0, 0, 0, 0)  # Highlighting Arthur C. Clarke

# Plotting the sector pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    influence_scores, labels=authors, autopct='%1.1f%%', startangle=140, colors=colors,
    explode=explode, wedgeprops=dict(width=0.3, edgecolor='w'), pctdistance=0.85
)

# Enhance text aesthetics
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)

# Title and legend
ax.set_title("Influence of Science Fiction Authors\non Futuristic Technologies", 
             fontsize=14, fontweight='bold', pad=20)
ax.legend(wedges, authors, title="Authors", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1))

# Draw circle for donut shape
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Automatically adjust layout
plt.tight_layout()

# Display plot
plt.show()