import matplotlib.pyplot as plt
import numpy as np

# Define years and sectors
years = np.array([2018, 2019, 2020, 2021, 2022])
sectors = ['Transportation', 'Energy', 'Healthcare', 'Communication']

# Percentage of technological advancement per sector per year
tech_advancement = np.array([
    [20, 15, 25, 10],  # 2018
    [25, 18, 30, 12],  # 2019
    [30, 22, 35, 15],  # 2020
    [35, 25, 40, 20],  # 2021
    [40, 28, 45, 25]   # 2022
])

# Total technological advancement per year
total_advancement = tech_advancement.sum(axis=1)

# Separate the data for each sector
transportation = tech_advancement[:, 0]
energy = tech_advancement[:, 1]
healthcare = tech_advancement[:, 2]
communication = tech_advancement[:, 3]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Create stacked bar chart
ax.bar(years, transportation, label=sectors[0], color='#1f77b4', alpha=0.8)
ax.bar(years, energy, bottom=transportation, label=sectors[1], color='#ff7f0e', alpha=0.8)
ax.bar(years, healthcare, bottom=transportation + energy, label=sectors[2], color='#2ca02c', alpha=0.8)
ax.bar(years, communication, bottom=transportation + energy + healthcare, label=sectors[3], color='#d62728', alpha=0.8)

# Overlay line plot for total technological advancement
ax.plot(years, total_advancement, color='black', marker='o', linestyle='-', linewidth=2, label='Total Advancement')

# Add data labels to the line plot
for i, txt in enumerate(total_advancement):
    ax.annotate(txt, (years[i], total_advancement[i]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=10, color='black')

# Title and labels
ax.set_title("Technological Evolution in a Smart City\n(2018 - 2022)", fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage of Technological Integration (%)', fontsize=14)

# Customize ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 151, 25))

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Components', fontsize=12)

# Adding grid for clarity
ax.grid(True, linestyle='--', alpha=0.6)

# Ensure the layout is tight
plt.tight_layout()

# Show plot
plt.show()