import matplotlib.pyplot as plt
import numpy as np

# Define the programming languages and their popularity on each planet
languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]
orbis_popularity = [92, 72, 80, 85, 68]

# Additional related data for trends
years = ["2021", "2022", "2023", "2024"]
pytherion_growth = [5, 7, 10, 12]
rubiark_growth = [6, 5, 8, 9]

# Define bar width and positions for each group's bars
bar_width = 0.25
r1 = np.arange(len(languages))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the figure and a grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Create the bar chart
ax1.bar(r1, xenon_popularity, color='b', width=bar_width, edgecolor='grey', label='Xenon')
ax1.bar(r2, zephyr_popularity, color='g', width=bar_width, edgecolor='grey', label='Zephyr')
ax1.bar(r3, orbis_popularity, color='m', width=bar_width, edgecolor='grey', label='Orbis')

# Add data value labels above the bars
for rects, data in zip([r1, r2, r3], [xenon_popularity, zephyr_popularity, orbis_popularity]):
    for rect, value in zip(rects, data):
        ax1.text(rect, value + 1, str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Set labels and title for the bar chart
ax1.set_xlabel('Programming Languages', fontweight='bold', fontsize=12)
ax1.set_ylabel('Popularity (%)', fontweight='bold', fontsize=12)
ax1.set_title('Programming Language Popularity\nAcross Alien Planets', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks([r + bar_width for r in range(len(languages))])
ax1.set_xticklabels(languages, rotation=30, ha='right')
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.legend(title='Planets', loc='upper right')

# Create the line chart for growth over years
ax2.plot(years, pytherion_growth, marker='o', color='c', label='Pytherion Growth')
ax2.plot(years, rubiark_growth, marker='s', color='y', label='Rubiark Growth')

# Set labels and title for the line chart
ax2.set_xlabel('Year', fontweight='bold', fontsize=12)
ax2.set_ylabel('Growth (%)', fontweight='bold', fontsize=12)
ax2.set_title('Growth of Pytherion and Rubiark\nOver the Years', fontsize=14, fontweight='bold', pad=20)
ax2.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax2.legend(title='Languages', loc='upper left')

# Ensure the layout is tight to prevent overlap
plt.tight_layout()

# Display the combined plots
plt.show()