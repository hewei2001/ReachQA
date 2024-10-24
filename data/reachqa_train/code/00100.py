import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2023
years = np.arange(2010, 2024)

# Number of research papers published each year
papers_published = np.array([150, 170, 190, 220, 260, 310, 400, 480, 590, 680, 820, 950, 1100, 1280])

# Annotations for specific years
annotations = {
    2013: "Quantum Error\nCorrection",
    2017: "Quantum\nSupremacy",
    2020: "Quantum Machine\nLearning Boom"
}

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(years, papers_published, marker='o', linestyle='-', color='navy', linewidth=2, markersize=8)

# Annotate notable breakthroughs
for year, label in annotations.items():
    plt.annotate(label, 
                 (year, papers_published[year-2010]), 
                 textcoords="offset points", 
                 xytext=(-45,15), 
                 ha='center',
                 fontsize=9, 
                 arrowprops=dict(arrowstyle='->', color='black'))

# Add title and labels
plt.title("Evolution of Quantum Computing Research\nPapers Published Annually (2010-2023)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Papers Published", fontsize=12)

# Customize grid and limits
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0, 1400)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1500, 200))

# Adjust the layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()