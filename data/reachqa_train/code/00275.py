import matplotlib.pyplot as plt
import numpy as np

# Define the programming languages and their popularity on each planet
languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]
orbis_popularity = [92, 72, 80, 85, 68]

# Define bar width and positions for each group's bars
bar_width = 0.25
r1 = np.arange(len(languages))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.bar(r1, xenon_popularity, color='b', width=bar_width, edgecolor='grey', label='Xenon')
ax.bar(r2, zephyr_popularity, color='g', width=bar_width, edgecolor='grey', label='Zephyr')
ax.bar(r3, orbis_popularity, color='m', width=bar_width, edgecolor='grey', label='Orbis')

# Add data value labels above the bars
for rects, data in zip([r1, r2, r3], [xenon_popularity, zephyr_popularity, orbis_popularity]):
    for rect, value in zip(rects, data):
        ax.text(rect, value + 1, str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adding labels and title
ax.set_xlabel('Programming Languages', fontweight='bold', fontsize=12)
ax.set_ylabel('Popularity (%)', fontweight='bold', fontsize=12)
ax.set_title('Programming Language Popularity\nAcross Alien Planets', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks([r + bar_width for r in range(len(languages))])
ax.set_xticklabels(languages)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=30, ha='right')

# Adding a legend
plt.legend(title='Planets', loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()