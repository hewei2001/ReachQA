import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import ListedColormap

# Years from 2010 to 2023
years = np.arange(2010, 2024)

# Number of research papers published each year
papers_published = np.array([150, 170, 190, 220, 260, 310, 400, 480, 590, 680, 820, 950, 1100, 1280])

# Patents filed related to quantum computing
patents_filed = np.array([10, 15, 20, 25, 30, 38, 52, 67, 85, 110, 140, 180, 230, 300])

# Annotations for specific years
annotations = {
    2013: "Quantum Error\nCorrection",
    2017: "Quantum\nSupremacy",
    2020: "Quantum Machine\nLearning Boom"
}

# Create the main figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Line plot for papers published
colors = ListedColormap(['navy', 'blue', 'dodgerblue', 'deepskyblue', 'aqua']).colors
norm = plt.Normalize(years.min(), years.max())
line = ax1.scatter(years, papers_published, c=years, cmap='cool', edgecolor='black', s=100, zorder=3)
ax1.plot(years, papers_published, linestyle='-', color='navy', linewidth=2, zorder=2)

# Annotate notable breakthroughs
for year, label in annotations.items():
    ax1.annotate(label, 
                 (year, papers_published[year-2010]), 
                 textcoords="offset points", 
                 xytext=(-40,10), 
                 ha='center',
                 fontsize=10, 
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white', alpha=0.7),
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3", color='gray'))

# Secondary y-axis for patents
ax2 = ax1.twinx()
ax2.plot(years, patents_filed, color='orange', linewidth=2, linestyle='--', label='Patents Filed', zorder=1)
ax2.set_ylabel("Number of Patents Filed", fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Title and labels
ax1.set_title("Evolution of Quantum Computing Research\nPapers Published and Patents Filed Annually (2010-2023)", fontsize=16)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Papers Published", fontsize=12, color='navy')
ax1.tick_params(axis='y', labelcolor='navy')

# Customize grid and limits
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_ylim(0, 1400)
ax1.set_xlim(years.min() - 1, years.max() + 1)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

# Legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()