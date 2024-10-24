import matplotlib.pyplot as plt
import numpy as np

# Names of the Seven Wonders of the Ancient World
wonders = [
    "Great Pyramid of Giza", "Hanging Gardens of Babylon",
    "Statue of Zeus at Olympia", "Temple of Artemis at Ephesus",
    "Mausoleum at Halicarnassus", "Colossus of Rhodes", 
    "Lighthouse of Alexandria"
]

# Number of tourists in thousands
tourists = np.array([450, 380, 270, 310, 200, 290, 410])

# Define colors for each wonder
colors = ['#FFCC00', '#FF6600', '#FF33CC', '#CCFF33', '#00CCFF', '#FF3366', '#66FF33']

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Creating bars
bars = ax.bar(wonders, tourists, color=colors, edgecolor='black')

# Add data annotations
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval}k', ha='center', va='bottom', fontsize=10, color='black')

# Set the title and labels
ax.set_title('Tourist Attraction in 100 AD:\nSeven Wonders of the Ancient World', fontsize=16, pad=20)
ax.set_xlabel('Wonders of the Ancient World', fontsize=12)
ax.set_ylabel('Number of Tourists (in thousands)', fontsize=12)

# Rotate x-ticks for readability
plt.xticks(rotation=45, ha='right')

# Add grid lines for the y-axis to improve readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to ensure no overlapping elements
plt.tight_layout()

# Show the plot
plt.show()