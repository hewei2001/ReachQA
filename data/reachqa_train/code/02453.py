import matplotlib.pyplot as plt
import numpy as np

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

# Number of books written by each author
book_counts = [70, 500, 44, 65, 54]

# Colors for each sector
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#8e44ad']

# Create a figure with two subplots (side-by-side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Donut chart setup (ax1)
explode = (0.1, 0, 0, 0, 0)  # Highlighting Arthur C. Clarke
wedges, texts, autotexts = ax1.pie(
    influence_scores, labels=authors, autopct='%1.1f%%', startangle=140, colors=colors,
    explode=explode, wedgeprops=dict(width=0.3, edgecolor='w'), pctdistance=0.85
)
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)
ax1.set_title("Influence of Science Fiction Authors\non Futuristic Technologies", 
             fontsize=14, fontweight='bold', pad=20)

# Bar chart setup (ax2)
bar_positions = np.arange(len(authors))
ax2.bar(bar_positions, book_counts, color=colors, edgecolor='black')
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(authors, rotation=45, ha='right', fontsize=10)
ax2.set_title("Number of Books Written by Each Author", fontsize=14, fontweight='bold')
ax2.set_ylabel("Number of Books", fontsize=12)
ax2.set_xlabel("Authors", fontsize=12)

# Legends and adjustments
ax1.legend(wedges, authors, title="Authors", loc="upper left", bbox_to_anchor=(0.9, 0.9))
plt.tight_layout()

# Display plot
plt.show()